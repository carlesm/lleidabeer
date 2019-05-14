from influxdb import InfluxDBClient
from time import sleep
import datetime
import json

jsontext = """[
    {
        "measurement" : "%s",
        "time" : "%s",
        "fields":{
            "value": %f
        }
    }
]
"""

def savedata():
    now = datetime.datetime.utcnow()
    textnow = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    jsonmsg = jsontext % ("sensor2", textnow, 12.1)
    print(jsonmsg)
    jsondata = json.loads(jsonmsg)
    influxdb.write_points(jsondata)
    jsonmsg = jsontext % ("sensor3", textnow, 16.1)
    print(jsonmsg)
    jsondata = json.loads(jsonmsg)
    influxdb.write_points(jsondata)

influxdb = InfluxDBClient(database="sensortemp")


while True:
    savedata()
    sleep(5)