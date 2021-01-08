from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.searchdeezer, name='search'),
    path('download/', views.downloaddeezer, name='download')
]
