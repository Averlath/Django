from django.conf.urls import url
from .views import IndexView, AnyPageView, HordeCharacterView, AllianceCharacterView, HordeView, AllianceView

from django.conf import settings
from django.conf.urls.static import static

app_name = 'stuff'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)', AnyPageView.as_view(), name='page'),
    url(r'^horde/(?P<pk>[0-9]+)', HordeView.as_view(), name='hordecharacter'),
    url(r'^horde/characters', HordeCharacterView.as_view(), name='horde'),
    url(r'^alliance/(?P<pk>[0-9]+)', AllianceView.as_view(), name='alliancecharacter'),
    url(r'^alliance/characters', AllianceCharacterView.as_view(), name='alliance')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
