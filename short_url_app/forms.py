from django import forms
from .models import UrlHandler

# Accept user input for the original full length URL.
class OriginalURLForm(forms.ModelForm):
    original_url = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}), label= 'Original URL')

    class Meta:
        model = UrlHandler
        fields = ['original_url']


# Render different form for get request to Expand the shortened URL
class ShortURLForm(forms.ModelForm):
    url_suffix = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}), label= 'Insert 7 character URL shortcut.')

    class Meta:
        model = UrlHandler
        fields = ['url_suffix']