from django.conf.urls import url
from soal.tesolimpiade import views


urlpatterns = [
    url (r'^$', views.ListSoalOlimpiadeView.as_view(), name='view'),
    # url (r'^biologi$', views.ListBiologiView.as_view(), name='biologi'),
 
]