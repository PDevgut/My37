from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView

from applications.blog import views

urlpatterns = [
    path("", views.AllPostsView.as_view()),
    path("new/", views.NewPostView.as_view()),
    path("<int:pk>/", views.PostView.as_view(), name='post'),
    path("<int:pk>/delete/", csrf_exempt(views.DeleteView.as_view())),
    path("<int:pk>/update/", csrf_exempt(views.UpdateView.as_view())),
]