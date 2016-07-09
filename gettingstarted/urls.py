"""nagar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shakha import views
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()


app_name = 'shakha'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # ex: /
    url(r'^$', views.home, name='home'),
    # ex: /about/
    url(r'^about/', views.nagar_about, name='nagar_about'),
    # ex: /shakha/5/
    url(r'^shakha/(?P<shakha_id>[0-9]+)/$', views.index, name='index'),
    # ex: /shakha/5/swaymsevak/
    url(r'^shakha/(?P<shakha_id>[0-9]+)/swaymsevak/$', views.shakha_swaymsevak, name='shakha_swaymsevak'),
        # ex: /shakha/5/ganvesh/
    url(r'^shakha/(?P<shakha_id>[0-9]+)/ganvesh/$', views.shakha_ganvesh, name='shakha_ganvesh'),
        # ex: /shakha/5/shikshit/
    url(r'^shakha/(?P<shakha_id>[0-9]+)/shikshit/$', views.shakha_shikshit, name='shakha_shikshit'),
        # ex: /shakha/5/ghosh/
    url(r'^shakha/(?P<shakha_id>[0-9]+)/ghosh/$', views.shakha_ghosh, name='shakha_ghosh'),
        # ex: /shakha/5/gat/
    url(r'^shakha/(?P<shakha_id>[0-9]+)/gat/$', views.shakha_gat, name='shakha_gat'),
        # ex: /shakha/5/sankhya/
    # url(r'^shakha/(?P<shakha_id>[0-9]+)/sankhya/$', views.shakha_sankhya, name='shakha_sankhya'),

    # ex: /swaymsevak/5/
    url(r'^swaymsevak/(?P<shakha_id>[0-9]+)/$', views.swaymsevak_detail, name='swaymsevak_detail'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
