import json
import random
from django.utils import timezone
from dashboard.models import driver

def update_points():
    time_now = timezone.now()
    with open("jobs/points/points.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        data_alfreds = data['alfreds']
        for up_data in data_alfreds:
            new_lat = random.randint(0,100) # to generate a random number from 0 to 100
            new_lng = random.randint(0,100)
            up_data['lat'] = str(new_lat)
            up_data['lng'] = str(new_lng)
            up_data['lastUpdate'] = str(time_now)
        
        jsonFile.seek(0)  # To move the cursor back to the begining
        json.dump(data, jsonFile) # places the data into the jsonFile
        jsonFile.truncate() # just in case the data is smaller that the previous one