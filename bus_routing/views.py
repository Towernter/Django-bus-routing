from django.shortcuts import render, redirect
from bus_routing import models
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .routes import*
from.models import Bus, Route, Driver
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import csv
from fpdf import FPDF
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

	context = {'count_buses': count_buses, 
				'count_drivers': count_drivers, 
				'count_routes': count_routes,
				'available_drivers': get_available_drivers(),
				'available_buses': get_available_buses(),
				'routes': get_routes()
				}

	#generate_timetable()
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


def get_available_drivers():
	alist = Driver.objects.filter(is_available=True)
	return alist


def get_available_buses():
	alist = Bus.objects.filter(is_available=True)
	return alist


def get_routes():
	alist = Route.objects.all()
	return alist


def allocate(drivers,buses):
    i = 0
    if len(drivers) == 0 or len(buses) == 0:
        return []
    if len(drivers) < len(buses):
        buses = sorted(buses)
        buses.reverse()
        buses = buses[:len(drivers)]
        for driver in drivers:
            buses[i].setdriver(driver.getname())
            i += 1
        return buses
    if len(buses) < len(drivers):
        drivers = drivers[:len(buses)]
        for driver in drivers:
            buses[i].setdriver(driver.getname())
            i += 1
        return buses
    if len(buses) == len(drivers):
        for driver in drivers:
            buses[i].setdriver(driver.getname())
            i += 1
        return buses


def generate_timetable(request):
	bus_list = []
	drivers_list = []
	routes_list = []

	for b in get_available_buses():
		b1=Buses(b.bus_name,b.capacity,True,"")
		bus_list.append(b1)

	for d in get_available_drivers():
		d1=Drivers(d.name,True)
		drivers_list.append(d1)

	for r in get_routes():
		r1=Routes(r.destination,r.estimated_people,r.time)
		routes_list.append(r1)

	allocate_list = allocate(drivers_list, bus_list)
	timetable_list = []
	timetable_list = finder(routes_list,allocate_list)

	a = datetime.datetime(100,1,1,7,30,00)
	timetable_list2 = []
	for i in timetable_list:
		timetable_list2.append([i[0],i[1],i[2],str(addSecs(a, i[3]*60)),str(addSecs(a, i[4]*60))])


	data = [['DESTINATION', 'BUS', 'DRIVER', 'DEPARTURE TIME', 'RETURN TIME']
	    ]
	for i in timetable_list2:
		data.append(i)
	for i in data:
		print(data)
	simple_table(data)

	return redirect('index')



def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


def simple_table(data):
	spacing=1 
	pdf = FPDF()
	pdf.set_font("Arial", size=10)
	pdf.add_page()

	col_width = pdf.w / 5.5
	row_height = pdf.font_size
	for row in data:
	    for item in row:
	        pdf.cell(col_width, row_height*spacing,
	                 txt=item, border=1)
	    pdf.ln(row_height*spacing)

	pdf.output('time_table.pdf')
	return data