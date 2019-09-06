from django.shortcuts import render, Http404, HttpResponse
from django.utils import timezone
from django.views.generic import View
from django.db.models import ObjectDoesNotExist
from devices.models import Device
from streaks.models import Streak
from .models import Checkin
import uuid

class CheckinView(View):

    def get(self, request, checkin_identifier=None):
        if not checkin_identifier:
            raise Http404("No identifier provided.")

        try:
            checkin_identifier_uuid = uuid.UUID(checkin_identifier)
        except ValueError:
            raise Http404("Checkin identifier does not fit required format.")

        try:
            device = Device.objects.get(checkin_identifier=checkin_identifier_uuid)
        except ObjectDoesNotExist:
            raise Http404("No device found.")

        ip_address = request.META.get('REMOTE_ADDR')
        last_device_streak = Streak.objects.filter(device=device).order_by('-updated')

        if not last_device_streak.count():
            streak = Streak.objects.create(device=device, ip_address=ip_address)
        elif last_device_streak.first().ip_address != ip_address:
            streak = Streak.objects.create(device=device, ip_address=ip_address)
        else:
            streak = last_device_streak.first()

        Checkin.objects.create(device=device, streak=streak, ip_address=ip_address)

        return HttpResponse("Success")


def get_device_information(device):
    context = {'device_name': device.name}

    last_checkin = Checkin.objects.filter(device=device).order_by('-created').first()
    # context['current_ip'] = last_checkin.ip_address
    context['last_checkin'] = last_checkin

    current_streak = last_checkin.streak
    current_streak_start = current_streak.checkin_set.all().order_by('created').first().created
    context['current_streak_start'] = current_streak_start

    first_checkin = Checkin.objects.filter(device=device).order_by('created').first()
    context['checking_in_since'] = first_checkin.created

    unique_ip_addresses = Streak.objects.filter(device=device).count()
    context['unique_ip_addresses'] = unique_ip_addresses

    checkins_in_last_24_hours = Checkin.objects.filter(device=device, created__gte=(timezone.now() - timezone.timedelta(hours=24))).count()
    context['checkins_in_last_24_hours'] = checkins_in_last_24_hours

    return context


class CurrentIP(View):

    def get(self, request):

        devices = Device.objects.filter(checkin__isnull=False).distinct()
        device_list = []
        for device in devices:
            device_list.append(get_device_information(device))

        return render(request, 'device_list.html', {'devices': device_list})
