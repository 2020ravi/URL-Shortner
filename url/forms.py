from django import forms
class Url(forms.Form):
    url = forms.CharField(label="URL", widget=forms.URLInput(attrs={'id': 'longurl', "placeholder":"http://site.com"}))
