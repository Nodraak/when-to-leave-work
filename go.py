#!/usr/bin/env python3

import datetime
import json
import math
import requests


URL = "https://v5.bvg.transport.rest/stops/900220383/departures?direction=900053301"
BUS_SPEED_KMPH = 30
NOW = datetime.datetime.utcnow().astimezone()


def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2

    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))


"""
response = requests.get(URL)
assert response.status_code == 200, response.status_code
data = json.loads(response.text)
assert len(data) >= 1, len(data)
"""

data = json.loads(open("test.json").read())


for d in data:
    line = d["line"]["name"]
    stop_name = d["stop"]["name"]
    destination = d["destination"]["name"]
    when = datetime.datetime.fromisoformat(d["when"])
    plannedWhen = datetime.datetime.fromisoformat(d["plannedWhen"])
    delay_str = "delay: -" if (d["delay"] is None) else "delay: %.1f min" % (d["delay"]/60)
    stop_loc = (d["stop"]["location"]["latitude"], d["stop"]["location"]["longitude"])
    cur_loc = (d["currentTripPosition"]["latitude"], d["currentTripPosition"]["longitude"])
    dist_km = haversine(cur_loc, stop_loc)/1000

    when_diff_sec = (when - NOW).total_seconds()
    estimated_time_from_dist = dist_km/(BUS_SPEED_KMPH/60)

    print("%s: %s -> %s" % (line, stop_name, destination))
    print("In: %d:%02d (%s)" % (when_diff_sec/60, when_diff_sec%60, when.time()))
    print("  Dist: %.1f km (est: %.1f min)" % (dist_km, estimated_time_from_dist))
    print("  Planned: %s (%s)" % (plannedWhen.time(), delay_str))
    print()
