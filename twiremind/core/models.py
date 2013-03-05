from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User)
    message = models.TextField(max_length=140)
    scheduled_time = models.DateTimeField()
    processed = models.BooleanField()

    def is_past_due(self):
        if now() > self.scheduled_time:
            return True
        else:
            return False

    def __unicode__(self):
        status = ""
        if self.processed:
            status = status + "SENT: "
        else:
            status = status + "PENDING: "

        status = status + str(self.user) + " (" + str(self.scheduled_time) + ")"

        return status