from django.conf.urls import url, include, patterns
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', views.menuPrincipal, name='menuPrincipal'),
]
