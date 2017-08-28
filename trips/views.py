from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import User, Vehicle


def index(request):
    return HttpResponse("Hi, you're at the trips index")

def user_profile(request, user_id):
    user = User.objects.get(pk = user_id)
    vehicle_list = user.vehicle_set.all()
    context = {
        'user': user,
        'vehicle_list': vehicle_list,
    }
    return render(request, 'users/profile.html', context)

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'vehicles/detail.html', {'vehicle': vehicle})
