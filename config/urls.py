from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("simja/", include('simja.urls')),
    path("askpage/", include('askpage.urls')),
]
