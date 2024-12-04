
copy into snowflake_django.backend.trip(
    tripduration, 
    starttime, 
    stoptime, 
    start_station_id, 
    start_station_name, 
    start_station_latitude, 
    start_station_longitude, 
    end_station_id, 
    end_station_name, 
    end_station_latitude, 
    end_station_longitude, 
    bikeid, 
    membership_type, 
    usertype, 
    birth_year, 
    gender
)
from @citibike_trips 
    file_format=csv
    PATTERN = '.*csv.*'
;