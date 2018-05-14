from django.views.generic import ListView, DetailView
from .models import Page, HordeCharacter, AllianceCharacter


class IndexView(ListView):
    template_name = 'stuff/pages_list.html'
    model = Page


class AnyPageView(DetailView):
    template_name = 'stuff/page.html'
    model = Page


class HordeCharacterView(ListView):
    template_name = 'stuff/horde_list.html'
    model = HordeCharacter
    context_object_name = 'horde'


class HordeView(DetailView):
    template_name = 'stuff/horde_char.html'
    model = HordeCharacter


class AllianceCharacterView(ListView):
    template_name = 'stuff/alliance_list.html'
    model = AllianceCharacter
    context_object_name = 'alliance'


class AllianceView(DetailView):
    template_name = 'stuff/alliance_char.html'
    model = AllianceCharacter
