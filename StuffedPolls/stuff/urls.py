from django.conf.urls import url
from .views import IndexView, AnyPageView, HordeCharacterView, AllianceCharacterView, HordeView, AllianceView


app_name = 'stuff'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)', AnyPageView.as_view(), name='page'),
    url(r'^faction', AnyPageView.as_view(), name='factions'),
    url(r'^race', AnyPageView.as_view(), name='races'),
    url(r'^horde/(?P<pk>[0-9]+)', HordeView.as_view(), name='hordecharacter'),
    url(r'^characters/horde', HordeCharacterView.as_view(), name='horde'),
    url(r'^alliance/(?P<pk>[0-9]+)', AllianceView.as_view(), name='alliancecharacter'),
    url(r'^characters/alliance', AllianceCharacterView.as_view(), name='alliance')
]
