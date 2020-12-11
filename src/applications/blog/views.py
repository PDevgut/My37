from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView
from django.views.generic import ListView
from applications.blog.models import Post

class AllPostsView(ListView):
    template_name = "blog/index.html"
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.session.get("name")
        address = self.request.session.get("address")
        context.update(
            {
                "address": address or "xz",
                "name": name or "Bro",
            }
        )
        return context


class NewPostView(CreateView):
    model = Post
    fields = ["title","content"]
    success_url = "/b/"

class PostView(DetailView):
    template_name = "blog/post.html"
    model = Post


class UpdateView(UpdateView):
    template_name = "blog/post_form.html"
    model = Post
    success_url = "/b/"

class DeleteView(DeleteView):
    http_method_names = ["post"]
    model = Post
    success_url = "/b/"



