from django.conf.urls import url
from .views import CharacterView, HordeView, AllianceView, Start, RaceView, ClassView, FactionView

app_name = 'stuff'

urlpatterns = [
    url(r'^$', Start.as_view(), name='start'),
    url(r'^horde/(?P<pk>[0-9]+)', HordeView.as_view(), name='horde'),
    url(r'^alliance/(?P<pk>[0-9]+)', AllianceView.as_view(), name='alliance'),
    url(r'^characters', CharacterView.as_view(), name='characters'),
    url(r'^races', RaceView.as_view(), name='race'),
    url(r'^classes', ClassView.as_view(), name='class'),
    url(r'^factions', FactionView.as_view(), name='faction')
]
