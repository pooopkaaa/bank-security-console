from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    # Программируем здесь

    all_visits = Visit.objects.all()
    non_closed_visits = all_visits.filter(leaved_at=None)
    non_closed_visits_info = []
    for non_closed_visit in non_closed_visits:
        non_closed_visits_info.append({
            'entered_at' : timezone.localtime(non_closed_visit.entered_at),
            'who_entered': non_closed_visit.passcard.owner_name, 
            'duration': non_closed_visit.get_duration()
        })
    print(non_closed_visits_info)
    context = {
        "non_closed_visits": non_closed_visits_info,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
