# %%
#!python -m venv .venv
#!pip install suntime
#!pip install geopy
#!pip install pipreqs
#!pip install pyinstaller

#some of the code here is adapted from https://www.geeksforgeeks.org/create-a-gui-to-get-sunset-and-sunrise-time-using-python/

# %% [markdown]
# # Imports

# %%
from datetime import datetime, date, timedelta
import time as sleepy  # need to call it something else because 'time' collides with datetime stuff
import os
from suntime import Sun
from geopy.geocoders import Nominatim
from IPython.display import clear_output


# %%
print("""
 ______  ____  ___ ___    ___  _      __ __      ______  ____  ___ ___    ___ 
|      ||    ||   |   |  /  _]| |    |  |  |    |      ||    ||   |   |  /  _]
|      | |  | | _   _ | /  [_ | |    |  |  |    |      | |  | | _   _ | /  [_ 
|_|  |_| |  | |  \_/  ||    _]| |___ |  ~  |    |_|  |_| |  | |  \_/  ||    _]
  |  |   |  | |   |   ||   [_ |     ||___, |      |  |   |  | |   |   ||   [_ 
  |  |   |  | |   |   ||     ||     ||     |      |  |   |  | |   |   ||     |
  |__|  |____||___|___||_____||_____||____/       |__|  |____||___|___||_____|
   A universal time format to draw ire.  
     By Jeff Industries and Fabrication
       MIT License    
         v0.3 released 2022-10-03
""")

# %% [markdown]
# # Helpful vars and funcs
# some of these are probably unused

# %%
#most days have 86,400 seconds (I KNOW)
tradtional_hours_in_day = 24
traditional_minutes_daily = 1440
traditional_seconds_daily = 86400

new_hours_in_day = 100
new_minutes_in_day = 10000
new_seconds_in_day = 1000000


# %%
def convertUTCto180thMeridian(in_datetime): 
    return in_datetime - timedelta(hours= 12)

    
def timeAt180thMeridian(): 
    '''Gets current time at 180th meridian in traditional datetime format'''
    return datetime.utcnow() - timedelta(hours=12)

def convertToTimely(in_time): 
    """Returns a decimal, always <= 1.0."""
    
    conv_total_seconds = in_time.hour * 3600 + in_time.minute *60 + in_time.second
    conv_time_decimal = conv_total_seconds / traditional_seconds_daily

    return conv_time_decimal

    
def calc_sunrise(): 
    return convertToTimely(
        convertUTCto180thMeridian(
            sun.get_sunrise_time()
        )
    )

def calc_sunset(): 
    return convertToTimely(
        convertUTCto180thMeridian(
            sun.get_sunset_time()
        )
    )

# %% [markdown]
# # Sun

# %%
# Nominatim API to get latitude and longitude
# User agent is name of app, probably so they can block if it gets too many requests. 
geolocator = Nominatim(user_agent="timely_time")

# %%
location = None

while location is None:  #this is a stupid way to do this, but geolocator will return a blank string if city not found
    place = str(input("Enter city name: ").lower())
    location = geolocator.geocode(place)
    
    
    # latitude and longitude fetch
    latitude = location.latitude
    longitude = location.longitude

    #sun object we'll pass to the sunrise/set calculators
    sun = Sun(latitude, longitude)

    if location is None:
        print("No cities found named: ", place, "It's either too small or misspelled.\n------\n\n") 

print("Success!\n\t", location, latitude, longitude)



# %% [markdown]
# # Time Output
# could definitely be optimized by not constantly re-calcing the sunrise/sunset

# %%
while True: 
    # Clear the output in jupyter
    
    clear_output(wait=True)
    # Clear the output on standard out
    os.system('cls')


    timely_time = convertToTimely(timeAt180thMeridian())
    sunrise = calc_sunrise()
    sunset = calc_sunset()
    
    #doing fancy stuff with f-strings here to make sure that the float's always represented as 4 digits
    print(f"""
{location.address}
Global Time  = {timely_time*100:.2f}
☼▲ = {sunrise*100:.2f} || ☼▼ = {sunset*100:.2f}
"""
    )
    sleepy.sleep(4) 

# %% [markdown]
# # Installation nonsense
# Things in here will generally be commented out, except when making new version.

# %%
#!pipreqs --encoding=utf8 --force

# %%
#!pyinstaller "base_100_time_v0.3.py" -y


