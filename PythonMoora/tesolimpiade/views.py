from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import TesOlimpiade,Siswa,HasilTes
from django.contrib.auth.mixins import LoginRequiredMixin
from tesolimpiade import helpers
from tesolimpiade.forms import HasilTesForm



class HarusLogin(LoginRequiredMixin):
    login_url = '/login/'



class ListTesOlimpiadeView(HarusLogin,View):
    template_name = 'tesolimpiade/index.html'
      

    def get(self, request):
        tp = TesOlimpiade.objects.all()
        tesolimpiade = helpers.SleksiSoalBio(tp).as_matrix()
       
        data = {
        'tesolimpiade2' : tesolimpiade,
        'tesolimpiade': {
               'total': len(tesolimpiade)
                # 'email':

                },

                }

        return render(request, self.template_name, data)

class SimpanHasilTesView(HarusLogin, View):
    template_name = 'tesolimpiade/index.html'

    def post(self, request):
        form = HasilTesForm(request.POST or None)
        if form.is_valid():
            hasiltes = HasilTes()
            # hasiltes.user = request.user
            hasiltes.siswa_id = request.user.siswa.id
            hasiltes.nilai = form.cleaned_data['nilai']
            hasiltes.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Simpan  nilai berhasil')
        return redirect('/tesolimpiade/')


