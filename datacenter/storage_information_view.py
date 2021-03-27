from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    # Программируем здесь
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        non_closed_visits.append({
            'entered_at': timezone.localtime(visit.entered_at),
            'who_entered': visit.passcard.owner_name,
            'duration': visit.get_duration(timezone.now()),
            'is_strange': visit.is_visit_long()
        })

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
