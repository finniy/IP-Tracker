import json


def found_operator(phone_number: str) -> str:
    # Ищет оператора по коду (трем цифрам после кода страны) в JSON-файле
    operator_number = phone_number[2:5]
    with open('phone_codes.json', 'r', encoding='utf-8') as json_file:
        for key, value in json.load(json_file).items():
            if key == operator_number:
                return value
