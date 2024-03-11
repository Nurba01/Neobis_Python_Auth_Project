from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class UserCreationForm(UserCreationForm):

    # add email field
    email = forms.EmailField(
        label=('Email'),
        max_length=100,
        widget=forms.EmailInput(attrs={'autocomplete' : 'email'}),

    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
