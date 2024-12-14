from django.shortcuts import render
from .services import YaDiskAPI



def file_list(request):
    public_key = request.GET.get('public_key', '')
    files = []
    if public_key:
        files = YaDiskAPI.get_file(public_key)

    context = {
        'files': files,
        'public_key': public_key,
    }

    return render(request, 'app/file_list.html', context)


def download_file(request):
    pass