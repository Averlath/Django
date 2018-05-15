from django.views.generic import ListView, DetailView, TemplateView
from .models import HordeCharacter, AllianceCharacter


class Start(TemplateView):
    template_name = 'stuff/start.html'


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


class RaceView(TemplateView):
    template_name = 'stuff/races.html'


class FactionView(TemplateView):
    template_name = 'stuff/factions.html'


class ClassView(TemplateView):
    template_name = 'stuff/classes.html'
