from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь

    all_passcards = Passcard.objects.all()
    active_passcards = all_passcards.filter(is_active=True)
    context = {
        "active_passcards": active_passcards,
    }
    return render(request, 'active_passcards.html', context)
