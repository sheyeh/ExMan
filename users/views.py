from authtools.views import LoginView, LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from . import models
from expenses import models as exp_models


class CustomAuthenticationForm(AuthenticationForm):
    def clean_username(self):
        return self.cleaned_data['username'].strip().lower()


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class AddAccountView(LoginRequiredMixin, CreateView):
    model = models.Account
    fields = (
        'name',
    )
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OneAccountView(LoginRequiredMixin, DetailView):
    model = exp_models.Account

    def total(self):
        return sum(x.amount for x in self.get_object().expense_set.all())

class AccountView(LoginRequiredMixin, ListView):
    model = models.Account

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def total(self):
        qs = self.get_queryset()
        return qs
