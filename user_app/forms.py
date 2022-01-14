from http.client import ImproperConnectionState
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("__all__")