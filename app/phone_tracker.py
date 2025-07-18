import phonenumbers
from phonenumbers import timezone, carrier, geocoder
from work_with_json import found_operator


def phone_found(phone_number: str) -> dict[str, str]:
    """
    Получает информацию о телефонном номере.

    Аргументы:
        phone_number (str): Телефонный номер в формате с международным кодом, например '+7XXXXXXXXXX'.

    Возвращает:
        dict[str, str]: Словарь с информацией о номере, содержащий следующие ключи:
            - "Город": название часового пояса или города, связанного с номером.
            - "Страна": страна, к которой принадлежит номер.
            - "Оператор": название мобильного оператора.
              Если стандартная библиотека phonenumbers не смогла определить оператора,
              используется пользовательская функция found_operator для поиска оператора по коду из JSON.
    """
    phone_info = phonenumbers.parse(phone_number)

    city = timezone.time_zones_for_geographical_number(phone_info)[0].split('/')[1]
    region = geocoder.description_for_number(phone_info, "en")
    operator = carrier.name_for_number(phone_info, "en")

    if not operator:
        operator = found_operator(phone_number)

    if not operator:
        operator = 'Не удалось найти данные'
    if not city:
        city = 'Не удалось найти данные'
    if not region:
        region = 'Не удалось найти данные'

    result_list_info = {
        "City": city,
        "Country": region,
        "Operator": operator
    }

    return result_list_info

