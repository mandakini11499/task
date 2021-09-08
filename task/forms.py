from django import forms
from task.models import UserModel

class UserForm(forms.ModelForm):
    password=forms.CharField(max_length=50,widget=forms.PasswordInput())
    class Meta:
        model=UserModel
        fields="__all__"
