import requests

class YaDiskAPI:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk/public/resources"

    @staticmethod
    def get_file(public_key):
        '''Получает файл по публичному ключу'''
        response = requests.get(YaDiskAPI.BASE_URL, params={"public_key": public_key})
        response.raise_for_status()
        data = response.json()
        items = data.get("_embedded", {}).get("items", [])
        return items
