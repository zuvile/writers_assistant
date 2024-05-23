from django import forms
from .models import Novel


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.FileField()


class CharacterSearchForm(forms.Form):
    name = forms.CharField(max_length=200)
    novels = Novel.objects.all()
    choices = {}
    for novel in novels:
        choices[novel] = novel

    novel = forms.ChoiceField(choices=choices)
