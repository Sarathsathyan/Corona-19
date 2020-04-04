from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm, Textarea
from .models import rescue
from .models import contact



class AddInternship(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    user_phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    class Meta:
        model = rescue
        fields = ['name','address','user_phone']


class EmContact(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))


    class Meta:
        model = contact
        fields = ['name','address','phone','typeHelp','address']
