import phonenumbers
from phonenumbers import timezone, carrier, geocoder
from app.work_with_json import found_operator


def phone_found(phone_number: str) -> dict[str, str]:
    # Получает информацию о телефоне: город, страна и оператор
    phone_info = phonenumbers.parse(phone_number)

    city = timezone.time_zones_for_geographical_number(phone_info)[0].split('/')[1]
    region = geocoder.description_for_number(phone_info, "en")
    operator = carrier.name_for_number(phone_info, "en")

    # Если оператор не найден стандартным способом — ищем через JSON
    if not operator:
        operator = found_operator(phone_number)

    # Если данные не найдены, ставим заглушку
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


def format_phone_info(result_list_info: dict) -> str:
    # Форматирует информацию о телефоне в читаемый текст
    result_text = (
        f"📞 Результаты по номеру:\n\n"
        f"Страна: {result_list_info['Country']}\n"
        f"Город: {result_list_info['City']}\n"
        f"Оператор: {result_list_info['Operator']}"
    )
    return result_text
