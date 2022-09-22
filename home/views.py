from math import remainder
from django.shortcuts import render

from .forms import SearchForm
from .models import Station, Connection, Reminder

def home_view(request):
    form = SearchForm(request.POST or None)
    stations = Station.objects.all()
    tags = [station.name for station in stations]
    context = {
        "form": form,
        "tags": tags
    }
    if form.is_valid():
        data = form.cleaned_data
        connection = Connection(
            departure_from=data["departure_from"],
            arrival_at=data["arrival_at"],
            departure_time=data["departure_time"],
        )
        connection_already_in_db = Connection.objects.filter(departure_from=connection.departure_from, arrival_at=connection.arrival_at, departure_time=connection.departure_time)
        if connection_already_in_db.exists():
            existing_connection = connection_already_in_db.first()
            reminder = Reminder(
                connection=existing_connection,
                departure_date=data["departure_date"],
                reminder_time=data["reminder_time"],
                email=data["email"]
            )
            reminder.save()
        else:
            new_connection = connection
            reminder = Reminder(
                connection=new_connection,
                departure_date=data["departure_date"],
                reminder_time=data["reminder_time"],
                email=data["email"]
            )
            connection.save()
            reminder.save()
        reminder.remind()
    return render(request, "home/home.html", context)



