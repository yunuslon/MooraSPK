from django import forms
from orm.models import  Siswa


class SiswaForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    nama = forms.CharField(max_length=30)
    jenis_kelamin = forms.CharField(max_length=30)
    tanggal_lahir = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    email = forms.CharField(max_length=30)
    
        
    class Meta:
        model = Siswa


