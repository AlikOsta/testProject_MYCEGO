from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .services import YaDiskAPI



def file_list(request):
    """
    Отображает список файлов с Яндекс.Диска по публичному ключу.

    Args: request: HTTP запрос Django
    Returns: HttpResponse: Отрендеренный шаблон со списком файлов
    context:
        files (List): Список файлов с Яндекс.Диска
        public_key (str): Публичный ключ, введенный пользователем
    """

    public_key = request.GET.get('public_key', '')
    files = []
    if public_key:
        files = YaDiskAPI.get_file(public_key)

    context = {
        'files': files,
        'public_key': public_key,
    }

    return render(request, 'app/file_list.html', context)


def download_file(request) -> HttpResponse:
    """
    Обрабатывает запрос на скачивание файла.
    Перенаправляет пользователя на прямую ссылку для скачивания.

    Args: request: HTTP запрос Django

    Returns:
        HttpResponseRedirect: Редирект на URL скачивания
        HttpResponse: Сообщение об ошибке при неверном запросе

    Query Parameters:
        public_key (str): Публичный ключ Яндекс.Диска
        path (str): Путь к файлу на Яндекс.Диске
    """

    public_key = request.GET.get("public_key", "")
    path = request.GET.get("path", "")

    if public_key and path:
        download_url = YaDiskAPI.download_file(public_key, path)
        return HttpResponseRedirect(download_url)
    
    return HttpResponse("Invalid request", status=400)