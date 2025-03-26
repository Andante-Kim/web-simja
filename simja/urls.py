from django.urls import path

from . import views

app_name = 'simja'

urlpatterns = [
    path('', views.index, name='index'),
]