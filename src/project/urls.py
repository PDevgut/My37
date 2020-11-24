"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based view
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path

from framework.utils import read_static


def index(_request:HttpRequest) -> HttpResponse:
    base = read_static("_base.html")
    base_html = base.content.decode()
    index_html = read_static("index.html").content.decode()

    result = base_html.format(xxx=index_html)
    result = result.encode()
    return HttpResponse(result)

def styles(_request:HttpRequest) -> HttpResponse:
    result = read_static("styles.css").content
    return HttpResponse(result, content_type="text/css")


urlpatterns = [
    path('', index),
    path('s/styles.css/', styles),
    path('admin/', admin.site.urls),
]
