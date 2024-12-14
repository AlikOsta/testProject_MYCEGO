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
    
    @staticmethod
    def download_file(public_key, path):
        """Скачивание файла"""
        response = requests.get(f"{YaDiskAPI.BASE_URL}/download", params={"public_key": public_key, "path": path})
        response.raise_for_status()
        download_url = response.json().get("href")

        if not download_url:
            raise Exception("Ссылка для скачивания не найдена в ответе API.")
        
        return download_url
