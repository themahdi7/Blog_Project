from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password'}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        else:
            raise forms.ValidationError('Please enter a correct username or password!', code='invalid_info')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Email'}))
    password = forms.CharField(min_length=8,
                               widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password'}))
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={'class': 'input100', 'placeholder': 'Confirm password'}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password == password2:
            return password2

        raise forms.ValidationError('Passwords does not match')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'inputFirstname', 'type': 'text',
                       'placeholder': 'Enter your username'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputLastname', 'type': 'text',
                                                'placeholder': 'Enter your last name'})
        }
