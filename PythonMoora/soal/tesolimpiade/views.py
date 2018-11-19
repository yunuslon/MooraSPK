from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karakter,NilaiAkademik,HasilTes,Siswa,Plomba,Kelas,TesOlimpiade
from soal.tesolimpiade import helpers
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from library.view import ManagementAccessView

# Create your views here.


class ListSoalOlimpiadeView(ManagementAccessView):
  def get(self, request):
        template = 'tesolimpiade/index.html'
        tp = TesOlimpiade.objects.all()
        soalbio = helpers.SleksiSoalBio(tp).as_matrix()
        data = {
            'soalbio' : soalbio,
          
        }
        return render(request, template, data)
