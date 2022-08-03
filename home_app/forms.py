from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'style': "text-transform:none", 'class': 'col-md-6 col-sm-12', 'placeholder': 'your name'}))
    subject = forms.CharField(max_length=150, label='', widget=forms.TextInput(
        attrs={'style': "text-transform:none", 'class': 'col-md-12 col-sm-12', 'placeholder': 'subject'}))
    body = forms.CharField(label="", widget=forms.Textarea(
        attrs={'style': "text-transform:none", 'class': 'col-lg-12', 'placeholder': 'Your Message'}))
