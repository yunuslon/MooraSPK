from django.conf.urls import url
from soalkimia import views

urlpatterns = [
	url (r'^$', views.ListSoalKimiaView.as_view(), name='view'),
    url(r'^simpan/$', views.SimpanHasilTesKimView.as_view(), name='simpan'),


	]