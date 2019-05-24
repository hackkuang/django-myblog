"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blogapp/', include('blogapp.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include

from myblog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('extraapps.DjangoUeditor.urls')),      # 添加DjangoUeditor的URL
    path('media/<str:path>/', serve, {'document_root': settings.MEDIA_ROOT}),

]
