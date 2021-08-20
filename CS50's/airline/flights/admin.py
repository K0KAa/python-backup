from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Flight,Airport,Passenger
from . import models
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display =("id","origin","destination","duration")
class PasengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger,PasengerAdmin)
