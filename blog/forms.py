from django import forms
from .models import Messages
class ContactForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['name','email','message']
