from django import forms
from django.utils.translation import ugettext_lazy as _


class ClaimForm(forms.Form):
    travel_date = forms.DateField(label=_("travel date"))
    planned_departure_time = forms.CharField(label=_("planned depature time"))
    depature_station = forms.CharField(label=_("depature station"))
    arrival_station = forms.CharField(label=_("arrival station"))
