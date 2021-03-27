from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def passcard_info_view(request, passcode):
    # Программируем здесь
    visits = Visit.objects.filter(passcard__passcode = passcode).exclude(leaved_at = None)
    this_passcard_visits = []
    
    for visit in visits:
        this_passcard_visits.append({
            "entered_at": timezone.localtime(visit.entered_at),
            "duration": visit.get_duration(visit.leaved_at),
            "is_strange": visit.is_visit_long()
        })
    
    context = {
        "passcard": Passcard.objects.get(passcode = passcode),
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
