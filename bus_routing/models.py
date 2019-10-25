from django.db import models


class Route(models.Model):
    destination = models.CharField(max_length=50)
    distance = models.DecimalField(max_digits=50,decimal_places=2)
    estimated_people = models.IntegerField()
    route_name = models.CharField(max_length=20)
    time = models.IntegerField()

    def __str__(self):
        return self.destination


class Driver(models.Model):
    name = models.CharField(max_length=50)
    driver_number =  models.CharField(max_length=50)
    is_available = models.BooleanField(default = False)

    def __str__(self):
        return self.name


class Bus(models.Model):
    asigned_to = models.ForeignKey(Driver, on_delete=models.SET_NULL, blank=True, null=True, default = None)
    bus_name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default = False)

    def __str__(self):
        return self.bus_name




