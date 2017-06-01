from django.conf.urls import url
from rango2 import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^about/', views.about, name='about'),

]
