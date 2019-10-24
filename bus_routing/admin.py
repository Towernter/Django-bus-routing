from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Driver)

