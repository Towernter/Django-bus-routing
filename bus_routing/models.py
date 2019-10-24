from django.db import models


class Route(models.Model):
    destination=models.CharField(max_length=50)
    distance=models.DecimalField(max_digits=50,decimal_places=2)
    estimated_people=models.IntegerField()
    route_name=models.CharField(max_length=20)
    time_line=models.IntegerField()
    def __str__(self):
        return self.destination+"       "+self.route_name

class Driver(models.Model):
    name=models.CharField(max_length=50)
    driver_number=models.CharField(max_length=50)
    def __str__(self):
        return self.name+""+self.driver_number

class Bus(models.Model):
    bus_name=models.CharField(max_length=50)
    capacity=models.IntegerField()
    def __str__(self):
        return self.bus_name+" "+str(self.capacity)




