from django import forms
from django.views.generic import FormView
from django.views.generic import RedirectView


class HelloForm(forms.Form):
    name = forms.CharField()
    address= forms.CharField()

class HelloView(FormView):
    template_name = "hello/hello.html"
    success_url = "/h/"
    form_class = HelloForm
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

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        address = form.cleaned_data["address"]
        self.request.session["name"] = name
        self.request.session["address"] = address
        return super().form_valid(form)


class HelloResetView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.request.session.clear()
        return "/h/"