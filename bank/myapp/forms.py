from django import forms
from .models import *
class TransferForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender', 'receiver', 'amount']