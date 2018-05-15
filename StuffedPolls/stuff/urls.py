from django.conf.urls import url
from .views import HordeCharacterView, AllianceCharacterView, HordeView, AllianceView, Start, RaceView, ClassView, FactionView

from django.conf import settings
from django.conf.urls.static import static

app_name = 'stuff'

urlpatterns = [
    url(r'^$', Start.as_view(), name='start'),
    url(r'^horde/(?P<pk>[0-9]+)', HordeView.as_view(), name='hordecharacter'),
    url(r'^horde/characters', HordeCharacterView.as_view(), name='horde'),
    url(r'^alliance/(?P<pk>[0-9]+)', AllianceView.as_view(), name='alliancecharacter'),
    url(r'^alliance/characters', AllianceCharacterView.as_view(), name='alliance'),
    url(r'^races', RaceView.as_view(), name='race'),
    url(r'^classes', ClassView.as_view(), name='class'),
    url(r'^factions', FactionView.as_view(), name='faction')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
