from django import forms
from django.contrib.auth.models import User
from .models import Message


class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Destinatario"
    )

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']