from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

        # def __init__(self, *args, **kwargs):
        #     super(SignUpForm, self).__init__(*args, **kwargs)
        #     self.fields['email'].widget.attrs['placeholder'] = 'email'
        #     self.fields['username '].widget.attrs['placeholder'] = 'username'
        #     self.fields['password1 '].widget.attrs['placeholder'] = 'password'

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            # 'password1': forms.TextInput(attrs={'placeholder': 'password'}),
        }

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ("Password")}),
            self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ("Confirm Password")}),

