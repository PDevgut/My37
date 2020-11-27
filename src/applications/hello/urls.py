from django.urls import path

from applications.hello import views
from applications.hello.views import hello

urlpatterns = [
    path('', hello),
    path("greet/", views.view_hello_greet),
    path("reset/", views.view_hello_reset),
]