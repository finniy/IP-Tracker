import re


def is_valid_ip_first(ip: str) -> bool:
    # Проверяет, правильный ли формат IP-адреса
    pattern_for_ip = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}' \
                     r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'
    if re.fullmatch(pattern_for_ip, ip, flags=re.IGNORECASE):
        return True
    else:
        return False


def is_valid_ip_second(ip_stock_info: dict) -> bool:
    # Проверяет статус в словаре, если 'success' — IP валидный
    if ip_stock_info['status'] == 'success':
        return True
    else:
        return False
