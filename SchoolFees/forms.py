from django import forms
from django.forms import ModelForm
from SchoolFees.models import *

class StudentForm(ModelForm):
    class Meta:
        model = Fee_balance
        fields = "__all__"

