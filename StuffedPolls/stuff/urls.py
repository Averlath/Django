from django.conf.urls import url
from .views import IndexView, AnyPageView, HordeCharacterView, AllianceCharacterView, CharactersView


app_name = 'stuff'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)', AnyPageView.as_view(), name='list'),
    url(r'^faction', AnyPageView.as_view(), name='list'),
    url(r'^race', AnyPageView.as_view(), name='list'),
    url(r'^character/(?P<pk>[0-9]+)', HordeCharacterView.as_view(), name='list'),
    url(r'^character/(?P<pk>[0-9]+)', AllianceCharacterView.as_view(), name='list'),
    url(r'^characters', CharactersView.as_view(), name='characters')
]
