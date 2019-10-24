from django.shortcuts import render, redirect
from bus_routing import models
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from.models import Bus, Route, Driver
from .forms import (
    SignUpForm,
    DriverForm,
    BusForm,
    RouteForm
    )


@login_required
def index(request):
	count_buses = Bus.objects.count()
	count_drivers = Driver.objects.count()
	count_routes = Route.objects.count()

	context = {'count_buses': count_buses, 'count_drivers': count_drivers, 'count_routes': count_routes}

	return render(request, 'bus_routing/index.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


