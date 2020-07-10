from . import views
from django.urls import path

urlpatterns = [
    path('', views.ytb_down, name='home'),
    path('download/', views.yt_download, name='download'),
    path('sorry/', views.sorry, name='sorry'),
    path('download_complete/<res>', views.download_complete, name='download_complete'),
]