from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new_plot', views.new_plot, name = 'new_plot'),
	url(r'^$', views.index, name = 'index'),
]