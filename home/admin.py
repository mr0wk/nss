from django.contrib import admin
from .models import Station, Connection, Reminder


class StationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Station, StationAdmin)


class ConnectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Connection, ConnectionAdmin)


class ReminderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reminder, ReminderAdmin)
