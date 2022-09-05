from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=50)


class Connection(models.Model):
    departure_from = models.CharField(max_length=50)
    arrival_at = models.CharField(max_length=50)
    time = models.TimeField()


class Reminder(models.Model):
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
