from re import I
from django.db import models

from .tasks import send_delay_info_email_task

from delay_scraper import scrape_connection_delay


class Station(models.Model):
    name = models.CharField(max_length=50)


class Connection(models.Model):
    departure_from = models.CharField(max_length=50)
    arrival_at = models.CharField(max_length=50)
    departure_time = models.TimeField()

    def get_connection_delay(self, departure_date):
        data = {
            "departure_from": self.departure_from,
            "arrival_at": self.arrival_at,
            "departure_date": departure_date,
            "departure_time": self.departure_time
        }
        return scrape_connection_delay(data)


class Reminder(models.Model):
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    # departure_date can also be treated as Reminder date and since Connection is not date restricted, departure_date is stored in Reminder
    departure_date = models.DateField()
    reminder_time = models.TimeField()
    email = models.EmailField()

    def remind(self):
        context = {
            'email_address': [self.email],
            'departure_from': self.connection.departure_from,
            'arrival_at': self.connection.arrival_at,
            'departure_time': self.connection.departure_time,
            'connection_delay': self.connection.get_connection_delay(self.departure_date)
        }
        send_delay_info_email_task.delay(context)
