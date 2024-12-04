from django.db import models


class Trip(models.Model):
    """Trip model from snowflake database."""

    trip_id = models.BigAutoField(blank=True, primary_key=True)
    tripduration = models.DateTimeField(blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    stoptime = models.DateTimeField(blank=True, null=True)
    start_station_id = models.BigIntegerField(blank=True, null=True)
    start_station_name = models.TextField(blank=True, null=True)
    start_station_latitude = models.FloatField(blank=True, null=True)
    start_station_longitude = models.FloatField(blank=True, null=True)
    end_station_id = models.BigIntegerField(blank=True, null=True)
    end_station_name = models.TextField(blank=True, null=True)
    end_station_latitude = models.FloatField(blank=True, null=True)
    end_station_longitude = models.FloatField(blank=True, null=True)
    bikeid = models.BigIntegerField(blank=True, null=True)
    membership_type = models.TextField(blank=True, null=True)
    usertype = models.TextField(blank=True, null=True)
    birth_year = models.BigIntegerField(blank=True, null=True)
    gender = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TRIP"
