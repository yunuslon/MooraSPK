from django import forms
from orm.models import Tesolimpiade
# from django.contrib.auth.models import User


class TesolimpiadeForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    jenjang = forms.CharField(max_length=30)
    no = forms.IntegerField( required=False, initial=0)
    gambar = forms.forms.CharField(max_length=30)
    pertayaan = forms.CharField( max_length=500)
    jawbanA = forms.CharField( max_length=300)
    jawbanB = forms.CharField( max_length=300)
    jawbanC = forms.CharField( max_length=300)
    jawbanD = forms.CharField( max_length=300)
    jawbanE = forms.CharField( max_length=300)
    kunci = forms.CharField( max_length=30)

    
    # user = forms.CharField(User, initial=0)
    class Meta:
        model = Tesolimpiade


