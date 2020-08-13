import os

import youtube_dl
from django.shortcuts import render
from pytube import YouTube
from youtube_dl import YoutubeDL



url = ''


def ytb_down(request):
    return render(request, 'ytb_main.html')


def yt_download(request):
    global url
    """метод request берет всю инфу со страницы, затем GET берет из формы input и get получает введенную инфу"""
    url = request.GET.get('url')  # url это name='url' в форме input так назвал
    """создаем объект, что бы узнать какое видео качать"""
    yt = YouTube(url)
    """создаем пустой список, куда будем добавлять элементы из цикла for"""
    resolutions = []
    """берем все полученные данные с url"""
    strm_all = yt.streams.filter(progressive=True, file_extension='mp4').all()
    for i in strm_all:
        resolutions.append(i.resolution)
    """метод dict.fromkeys нужен что бы удалить лишние значения из списка"""
    resolutions = list(dict.fromkeys(resolutions))
    embed_link = url.replace("watch?v=", "embed/")
    print(resolutions)
    print((embed_link))
    return render(request, 'yt_download.html', {'rsl': resolutions, 'embd': embed_link})



def download_complete(request, res):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    print(f'DIRECT :', f'{dirs}/Downloads')
    if request.method == 'POST':
        ydl = YoutubeDL()

        with youtube_dl.YoutubeDL(dict(forceurl=True)) as ydl:
            r = ydl.extract_info(url, download=False)
            media_url = r['formats'][-1]['url']
        return render(request, 'download_complete.html', {'media_url': media_url})
    else:
        pass



def sorry(request):
    return render(request, 'sorry.html')

