from . import views
from django.urls import path

urlpatterns = [
    path('', views.ytb_down, name='home'),
    path('download/', views.yt_download, name='download'),
    path('sorry/', views.sorry, name='sorry'),
    path('download_complete/<res>', views.download_complete, name='download_complete'),
    path('music/', views.ytb_music, name='music'),
    path('music_download/', views.music_download, name='music_download'),
    path('music_download_complete/', views.download_music_complete, name='download_music'),
]