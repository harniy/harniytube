import os
from django.shortcuts import render
from pytube import YouTube



url = ''


def ytb_down(request):
    return render(request, 'ytb_main.html')


def ytb_music(request):
    return render(request, 'ytb_music.html')


def yt_download(request):
    global url
    try:
        """метод request берет всю инфу со страницы, затем GET берет из формы input и get получает введенную инфу"""
        url = request.GET.get('url')  # url это name='url' в форме input так назвал
        """создаем объект, что бы узнать какое видео качать"""
        obj = YouTube(url)
        """создаем пустой список, куда будем добавлять элементы из цикла for"""
        resolutions = []
        """берем все полученные данные с url"""
        strm_all = obj.streams.filter(progressive=True, file_extension='mp4').all()
        for i in strm_all:
            resolutions.append(i.resolution)
        """метод dict.fromkeys нужен что бы удалить лишние значения из списка"""
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = url.replace("watch?v=", "embed/")
        return render(request, 'yt_download.html', {'rsl': resolutions, 'embd': embed_link})
    except:
        return render(request, 'sorry.html')

def music_download(request):
    global url
    try:
        """метод request берет всю инфу со страницы, затем GET берет из формы input и get получает введенную инфу"""
        url = request.GET.get('url')  # url это name='url' в форме input так назвал
        """создаем объект, что бы узнать какое видео качать"""
        obj = YouTube(url)
        """создаем пустой список, куда будем добавлять элементы из цикла for"""
        resolutions = []
        """берем все полученные данные с url"""
        strm_all = obj.streams.get_by_itag(140)
        resolutions.append(strm_all)
        """метод dict.fromkeys нужен что бы удалить лишние значения из списка"""
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = url.replace("watch?v=", "embed/")
        return render(request, 'ytb_music_download.html', {'rsl': resolutions, 'embd': embed_link})
    except:
        return render(request, 'sorry.html')

def download_complete(request, res):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    print(f'DIRECT :', f'{dirs}/Downloads')
    if request.method == 'POST':

        YouTube(url).streams.get_by_resolution(res).download(homedir + '/Downloads')
        return render(request, 'download_complete.html')
    else:
        return render(request, 'sorry.html')


def download_music_complete(request):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    print(f'DIRECT :', f'{dirs}/Downloads')
    if request.method == 'POST':
        YouTube(url).streams.get_by_itag(140).download(homedir + '/Downloads')
        return render(request, 'download_music_complete.html')
    else:
        return render(request, 'sorry.html')

def sorry(request):
    return render(request, 'sorry.html')

