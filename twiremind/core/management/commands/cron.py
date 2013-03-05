from django.core.management.base import BaseCommand, CommandError
from twiremind.core.models import Reminder
from twiremind.helpers.dm import send_direct_message

from django.utils.timezone import now


class Command(BaseCommand):
    def handle(self, *args, **options):
        reminders = Reminder.objects.all().filter(processed=False).filter(scheduled_time__lte=now())
        print str(len(reminders)) + " reminders found!"
        for reminder in reminders:
            try:
                send_direct_message(reminder.user.username, reminder.message)
            except Exception, ex:
                print "Couldn't send the direct message: " + str(ex)

            reminder.processed = True
            reminder.save()

