from django import forms
from .models import Bride, UserInfo, Cart
from django.contrib.auth.models import User


class BrideCreate(forms.ModelForm):
    class Meta:
        model = Bride
        fields = '__all__'


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class CartCreate(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')
        help_texts = {
            'username': None,
        }
