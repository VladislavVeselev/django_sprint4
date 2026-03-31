from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm


class RegistrationView(CreateView):
    """Регистрация нового пользователя."""
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('blog:index')