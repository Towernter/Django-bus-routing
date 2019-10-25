from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from.models import Bus, Route, Driver


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class BusForm(forms.ModelForm):
    bus_name = forms.CharField(max_length=50)
    capacity = forms.IntegerField()
    is_available = forms.BooleanField()

    class Meta:
        model = Bus
        fields = ('bus_name', 'capacity', 'is_available')


class DriverForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    driver_number = forms.CharField(max_length=50)
    is_available = forms.BooleanField()

    class Meta:
        model = Driver
        fields = ('name', 'driver_number', 'is_available')


class RouteForm(forms.ModelForm):
	destination = forms.CharField(max_length=50)
	distance = forms.DecimalField(max_digits=50,decimal_places=2)
	estimated_people = forms.IntegerField()
	route_name = forms.CharField(max_length=20)
	time = forms.IntegerField()
    
    
	class Meta:
	    model = Route
	    fields = ('destination', 'distance', 'estimated_people', 'route_name', 'time')