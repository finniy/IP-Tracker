import json

def found_operator(phone_number: str) -> str:
    """
    Определяет название оператора мобильной связи по коду оператора в телефонном номере.

    Аргументы:
        phone_number (str): Телефонный номер в международном формате, например '+7XXXXXXXXXX'.

    Возвращает:
        str: Название оператора, соответствующего коду из номера.
             Если код не найден в JSON-файле, функция вернёт None.
    """
    operator_number = phone_number[2:5]
    with open('phone_codes.json', 'r', encoding='utf-8') as json_file:
        for key, value in json.load(json_file).items():
            if key == operator_number:
                return value
