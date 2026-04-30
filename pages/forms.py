from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Page


class PageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'content', 'image']