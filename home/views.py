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
            time=data["time"],
        )
        connection_already_in_db = Connection.objects.filter(departure_from=connection.departure_from, arrival_at=connection.arrival_at, time=connection.time)
        if connection_already_in_db.exists():
            reminder = Reminder(
                connection=connection_already_in_db.first(),
                date=data["date"],
                time=data["reminder_time"]
            )
            reminder.save()
        else:
            reminder = Reminder(
                connection=connection,
                date=data["date"],
                time=data["reminder_time"]
            )
            connection.save()
            reminder.save()
    return render(request, "home/home.html", context)



