from django.urls import path

from . import views

app_name = 'askpage'

urlpatterns = [
    path('', views.index, name='index'),
]