from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    public_key = request.GET.get("public_key", "")
    path = request.GET.get("path", "")

    if public_key and path:
        download_url = YaDiskAPI.download_file(public_key, path)
        return HttpResponseRedirect(download_url)
    
    return HttpResponse("Invalid request", status=400)