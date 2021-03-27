from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    # Программируем здесь

    all_visits = Visit.objects.all()
    non_closed_visits = all_visits.filter(leaved_at=None)
    for non_closed_visit in non_closed_visits:
        print('Зашёл в хранилище, время по Москве:', timezone.localtime(non_closed_visit.entered_at), sep='\n')
        print('Находится в хранилище:', timezone.now() - timezone.localtime(non_closed_visit.entered_at), sep='\n')
        print('Имя:', non_closed_visit.passcard.owner_name, sep='\n')
    
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
