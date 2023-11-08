from django import forms
from django.forms import ModelForm
from register.models import *

class RegForm(ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

