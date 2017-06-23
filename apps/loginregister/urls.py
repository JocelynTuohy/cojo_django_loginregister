from django.conf.urls import url
from . import views
app_name = 'loginregister'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^validate$', views.validate, name='validate'),
    url(r'^register$', views.register, name='register'),
    url(r'^verify$', views.verify, name='verify'),
    url(r'^login$', views.login, name='login')
]