from django.views.generic import ListView, DetailView

from .models import Page, Character, HordeCharacter, AllianceCharacter


class IndexView(ListView):
    template_name = 'stuff/pages_list.html'
    model = Page



class AnyPageView(DetailView):
    template_name = 'stuff/page.html'
    model = Page


class HordeCharacterView(DetailView):
    template_name = 'stuff/page.html'
    model = HordeCharacter


class AllianceCharacterView(DetailView):
    template_name = 'stuff/page.html'
    model = AllianceCharacter


class CharactersView(ListView):
    template_name = 'stuff/pages_list.html'
    model = Character