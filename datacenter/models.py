from django.db import models
from django.utils import timezone
from django.utils import dateparse

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
    
    def _format_duration(self, duration_sec):
        hours = duration_sec // 3600
        minutes = (duration_sec % 3600) // 60
        return "{:.0f}ч {:.0f}мин".format(hours, minutes)

    def get_duration(self, time):
        duration_sec = (time - timezone.localtime(self.entered_at)).total_seconds()
        return self._format_duration(duration_sec)
