from django import forms
from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model=ChatMessage
        fields=('content',)
        widget={
            'content': forms.Textarea(attrs={
                'class':'w-full py-4 px-4 rounded-xl border-8 border-indigo-600'

            })
        }