from django.contrib import admin
from trips.models import Trip


class TripAdmin(admin.ModelAdmin):
    """Trip model admin."""

    list_display = [
        "trip_id",
        "tripduration",
        "starttime",
        "stoptime",
        "start_station_id",
        "start_station_name",
        "start_station_latitude",
        "start_station_longitude",
        "end_station_id",
        "end_station_name",
        "end_station_latitude",
        "end_station_longitude",
        "bikeid",
        "membership_type",
        "usertype",
        "birth_year",
        "gender",
    ]


admin.site.register(Trip, TripAdmin)
