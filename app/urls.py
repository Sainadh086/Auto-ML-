from django.conf.urls import url,include
from . import views

urlpatterns = [
                url('q/$',views.index,name = 'index'),
                url('upload/$', views.upload_csv, name='upload'),
		#url('upload1', views.upload, name  = 'upload'),
		url('ml/$', views.ml, name = 'ml'),
		url('ml1/$',views.ml1),
              ]




