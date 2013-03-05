# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import datetime

# Helpers
from twiremind.helpers.pin import generate_pin
from twiremind.helpers.dm import send_direct_message

# Models
from django.contrib.auth.models import User
from twiremind.core.models import Reminder


def front(request):
    return render_to_response('front.html', context_instance=RequestContext(request))


def register(request):
    if request.method == "POST":
        screen_name = request.POST.get('screen_name')
        if screen_name:
            user, created = User.objects.get_or_create(username=screen_name)
            pin = generate_pin()
            user.set_password(pin)
            user.save()
            if created:
                send_direct_message(screen_name,
                                    "Welcome to TwiRemind.Me :) Your PIN: " + str(pin) + ". You can login now!")

            else:
                send_direct_message(screen_name,
                                    "Your PIN has been reset. New PIN: " + str(pin) + ". You can login now!")

            return redirect("/")

        else:
            return render_to_response("no_username.html", context_instance=RequestContext(request))
    else:
        return render_to_response("register.html", context_instance=RequestContext(request))


def home(request):
    if not request.user.is_authenticated():
        return redirect("/")
    else:
        if request.method == "POST":
            action = False
            try:
                message = request.POST.get("message")

                days = request.POST.get("days")
                if days is not None and days != '':
                    days = int(days)
                else:
                    days = 0

                hours = request.POST.get("hours")
                if hours is not None and hours != '':
                    hours = int(days)
                else:
                    hours = 0

                mins = request.POST.get("mins")
                if mins is not None and mins != '':
                    mins = int(mins)
                else:
                    mins = 0

                if hours > 0 or days > 0 or mins > 0:
                    if message is not None and message != '':
                        time = datetime.datetime.now() + datetime.timedelta(days=days, hours=hours, minutes=mins)
                        reminder = Reminder(user=request.user, message=message, scheduled_time=time, processed=False)
                        reminder.save()
                        action = True
                else:
                # print "No entries amde"
                    pass
            except Exception, ex:
                print ex

            try:
                pin = request.POST.get("pin")
                print pin
                if pin is not None and pin != "":
                    user = request.user
                    user.set_password(pin)
                    user.save()
                    send_direct_message(user.username, "Your PIN has been updated to: " + str(pin))
                    action = True

            except:
                pass

            if action:
                return redirect("/home?status=ok")
            else:
                return redirect("/home")
        else:
            status = request.GET.get("status")
            my_reminders = Reminder.objects.all().filter(user=request.user)
            return render_to_response("home.html", {"reminders": my_reminders, "status": status},
                                      context_instance=RequestContext(request))


def delete(request):
    if not request.user.is_authenticated():
        return redirect("/")
    else:
        id = int(request.GET.get("id"))
        if id > 0:
            try:
                reminder = Reminder.objects.get(pk=id)
            except:
                pass
            if reminder.user == request.user:
                reminder.delete()
                return redirect("/home?status=ok")
            else:
                return redirect("/home")
        else:
            return redirect("/home")
