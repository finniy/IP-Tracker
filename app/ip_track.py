import requests
from app.check_valid_ip import is_valid_ip_second

def get_info_by_ip(ip: str, zoom: int = 9) -> tuple[dict | str, str | None]:
    # Получает данные по IP с внешнего API и возвращает информацию и ссылку на карту
    try:
        ip_stock_info = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        if is_valid_ip_second(ip_stock_info):  # Проверяем, валиден ли IP
            map_url = get_static_map_url(ip_stock_info, zoom)  # Получаем ссылку на карту
            ip_using_info = {
                'country': ip_stock_info['country'],
                'region': ip_stock_info['regionName'],
                'city': ip_stock_info['city'],
                'provider': ip_stock_info['isp'],
            }
            return ip_using_info, map_url
        else:
            return 'IP-adress not found', None

    except requests.exceptions.ConnectionError:
        # Ошибка соединения с интернетом
        return "Connection Error", None


def get_static_map_url(ip_stock_info: dict, zoom: int = 9) -> str:
    # Формирует URL для статичной карты по координатам из данных IP
    lon = ip_stock_info['lon']
    lat = ip_stock_info['lat']
    return f"https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&size=450,450&z={zoom}&l=map&pt={lon},{lat},pm2rdm"


def format_ip_info(ip_info: dict) -> str:
    # Форматирует информацию по IP в красивый текст для вывода
    return (
        "🌐 Информация по IP-адресу:\n\n"
        f"Страна: {ip_info['country']}\n"
        f"Регион: {ip_info['region']}\n"
        f"Город: {ip_info['city']}\n"
        f"Провайдер: {ip_info['provider']}"
    )
