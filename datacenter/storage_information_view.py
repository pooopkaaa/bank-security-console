from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь

    all_visits = Visit.objects.all()
    non_closed_visits = all_visits.filter(leaved_at=None)
    print(non_closed_visits)
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
