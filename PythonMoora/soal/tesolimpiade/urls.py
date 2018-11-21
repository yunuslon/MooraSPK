from django.conf.urls import url
from soal.tesolimpiade import views


urlpatterns = [

# Biologi
    url (r'^$', views.ListSoalOlimpiadeBioView.as_view(), name='view'),
    url (r'^addbio$', views.AddSoalBioView.as_view(), name='addbio'),
    url (r'^savebio$', views.SaveBiologiView.as_view(), name='savebio'),
    url (r'^editbio/(?P<id>\d+)$', views.UbahBioView.as_view(), name='editbio'),
    url (r'^updatebio/(?P<id>\d+)$', views.UpdateBioView.as_view(), name='updatebio'),
    url (r'^detailbio/(?P<id>\d+)$', views.DetailBiologiView.as_view(), name='detailbio'),
    url(r'^hapusbio/(?P<id>\d+)$', views.HapusBiologiView.as_view(), name='hapusbio'),

# Fisika
    url (r'^fisika$', views.ListSoalOlimpiadeFisView.as_view(), name='fisika'),
    url(r'^hapusfis/(?P<id>\d+)$', views.HapusFisikaView.as_view(), name='hapusfis'),

# Kimia
    url (r'^kimia$', views.ListSoalOlimpiadeKimView.as_view(), name='kimia'),
    url(r'^hapuskim/(?P<id>\d+)$', views.HapusKimiaView.as_view(), name='hapuskim'),

# Matematika
    url (r'^matematika$', views.ListSoalOlimpiadeMatView.as_view(), name='matematika'),
    url(r'^hapusmat/(?P<id>\d+)$', views.HapusMatematikaView.as_view(), name='hapusmat'),
 
]