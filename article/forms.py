from django import forms
from .models import Articles
class Articleforms(forms.ModelForm):
    class Meta:
        model=Articles
        fields=["title","content","article_image"]