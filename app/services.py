import requests
from typing import List, Dict, Optional
from requests.exceptions import RequestException

class YaDiskAPI:
    """
    Класс для работы с публичным API Яндекс.Диска.
    Предоставляет методы для получения списка файлов и их скачивания.
    """

    BASE_URL = "https://cloud-api.yandex.net/v1/disk/public/resources"

    @staticmethod
    def get_file(public_key: str) -> List[Dict]:
        """
        Получает список файлов по публичному ключу.
        Args: public_key (str): Публичный ключ Яндекс.Диска
        Returns: List[Dict]: Список файлов с их метаданными
        """

        params={
            "public_key": public_key
            }

        response = requests.get(YaDiskAPI.BASE_URL, params)
        response.raise_for_status()
        data = response.json()
        items = data.get("_embedded", {}).get("items", [])
        return items
    
    @staticmethod
    def download_file(public_key: str, path: str) -> str:
        """
        Получает ссылку для скачивания файла.
        Args:
            public_key (str): Публичный ключ Яндекс.Диска
            path (str): Путь к файлу
        Returns: str: URL для скачивания файла
        """

        params={
            "public_key": public_key, 
            "path": path
            }

        response = requests.get(f"{YaDiskAPI.BASE_URL}/download", params)
        response.raise_for_status()
        download_url = response.json().get("href")
        
        return download_url
