from django.views.generic import ListView, DetailView, TemplateView
from .models import HordeCharacter, AllianceCharacter, Faction, Class, AllianceRaces, HordeRaces


class Start(TemplateView):
    template_name = 'stuff/start.html'


class CharacterView(ListView):
    template_name = 'stuff/character_list.html'
    model = HordeCharacter

    def count(self):
        dict = {}
        highest = 0
        for element in HordeCharacter.objects.all(), AllianceCharacter.objects.all():
            if element.race in dict:
                dict[element.race] += 1
            else:
                dict[element.race] = 1
            for race in dict:
                if dict[race] > highest:
                    highest = race
                else:
                    pass
        return highest

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['alliance_list'] = AllianceCharacter.objects.all()
        ctx['num_alliance'] = AllianceCharacter.objects.count()
        ctx['num_horde'] = HordeCharacter.objects.count()
        ctx['num_total'] = AllianceCharacter.objects.count() + HordeCharacter.objects.count()
        ctx['highest'] = self.count()
        return ctx



class HordeView(DetailView):
    template_name = 'stuff/horde_char.html'
    model = HordeCharacter


class AllianceView(DetailView):
    template_name = 'stuff/alliance_char.html'
    model = AllianceCharacter


class RaceView(ListView):
    template_name = 'stuff/races.html'
    model = AllianceRaces

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['horde_list'] = HordeRaces.objects.all()
        return ctx


class FactionView(ListView):
    template_name = 'stuff/factions.html'
    model = Faction


class ClassView(ListView):
    template_name = 'stuff/classes.html'
    model = Class
