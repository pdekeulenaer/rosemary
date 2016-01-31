#from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Calendar(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)

    def __str__(self):
        return "%s (by %s)" % (self.name , self.owner.first_name)
    #def init_slots(self, start_day, end_day, start_time, end_time, increment):


class Appointment(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=400)
    party_size = models.IntegerField(default=1)

    start = models.DateTimeField('starting time')
    end = models.DateTimeField('ending time')

    def __str__(self):
        return self.purpose

class Timeslot(models.Model):
    calendar = models.ForeignKey(Calendar)
    slot_start = models.DateTimeField('start')
    slot_end = models.DateTimeField('end')
    capacity = models.IntegerField(default=1)
    free = models.BooleanField(default=True)
