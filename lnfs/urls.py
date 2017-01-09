from django.conf.urls import patterns, include, url
from django.contrib import admin
from lnfsapp import views
from home import views
from calendario import views
#from usuario import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
#from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^calendario/', include('calendario.urls')),
    url(r'^lnfsapp/', include('lnfsapp.urls')),
    #url(r'^usuario/registro$', 'usuario.views.signup', name='signup'),
    #url(r'^usuario/login$', login, {'template_name': 'login.html', }, name="login"),
    #url(r'^usuario/logout$', logout, {'template_name': 'menuPrincipal.html', }, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
