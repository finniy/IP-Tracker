import requests


def get_info_by_ip(ip: str) -> dict | str:
    try:
        ip_stock_info = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        ip_using_info = {
            'country': ip_stock_info['country'],
            'region': ip_stock_info['regionName'],
            'city': ip_stock_info['city'],
            'provider': ip_stock_info['isp'],
        }
        return ip_using_info

    except requests.exceptions.ConnectionError:
        return "Connection Error"


def get_static_map_url(lat: float, lon: float, zoom: int = 9) -> str:
    return f"https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&size=450,450&z={zoom}&l=map&pt={lon},{lat},pm2rdm"
