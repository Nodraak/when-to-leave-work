# README

*Query the BVG APIs to find out the optimal time to leave work in order to minimize waiting time in the cold.*

## API status

https://stats.uptimerobot.com/57wNLs39M/784879513

## API output

https://v5.vbb.transport.rest/locations?results=1&query=Kleinmachnow,%20Albert-Einstein-Ring%20Nord

```json
[
    {
        "type": "stop",
        "id": "900000220383",
        "name": "Kleinmachnow, Albert-Einstein-Ring Nord",
        "location": {
            "type": "location",
            "id": "900220383",
            "latitude": 52.408595,
            "longitude": 13.189342
        },
        "products": {
            "suburban": false,
            "subway": false,
            "tram": false,
            "bus": true,
            "ferry": false,
            "express": false,
            "regional": false
        },
        "stationDHID": "de:12069:900220383"
    }
]
```

https://v5.vbb.transport.rest/locations?results=1&query=Wannsee

```json
[
    {
        "type": "stop",
        "id": "900000053301",
        "name": "S Wannsee",
        "location": {
            "type": "location",
            "id": "900053301",
            "latitude": 52.421728,
            "longitude": 13.178932
        },
        "products": {
            "suburban": true,
            "subway": false,
            "tram": false,
            "bus": true,
            "ferry": true,
            "express": true,
            "regional": true
        },
        "stationDHID": "de:11000:900053301"
    }
]
```

https://v5.bvg.transport.rest/stops/900220383/departures?direction=900053301

```json
[
    {
        "tripId": "1|84514|0|86|12122022",
        "stop": {
            "type": "stop",
            "id": "900000220383",
            "name": "Kleinmachnow, Albert-Einstein-Ring Nord",
            "location": {
                "type": "location",
                "id": "900220383",
                "latitude": 52.408595,
                "longitude": 13.189342
            },
            "products": {
                "suburban": false,
                "subway": false,
                "tram": false,
                "bus": true,
                "ferry": false,
                "express": false,
                "regional": false
            },
            "stationDHID": "de:12069:900220383"
        },
        "when": "2022-12-12T22:17:00+01:00",
        "plannedWhen": "2022-12-12T22:17:00+01:00",
        "delay": null,
        "platform": "2",
        "plannedPlatform": null,
        "prognosisType": "prognosed",
        "direction": "S Wannsee",
        "provenance": null,
        "line": {
            "type": "line",
            "id": "620",
            "fahrtNr": "4407",
            "name": "620",
            "public": true,
            "adminCode": "RPM",
            "productName": "Bus",
            "mode": "bus",
            "product": "bus",
            "operator": {
                "type": "operator",
                "id": "regiobus-potsdam-mittelmark-gmbh",
                "name": "regiobus Potsdam Mittelmark GmbH"
            },
            "symbol": null,
            "nr": 620,
            "metro": false,
            "express": false,
            "night": false
        },
        "remarks": [
            {
                "type": "hint",
                "code": "bf",
                "text": "barrierefrei"
            },
            {
                "id": "181831",
                "type": "warning",
                "summary": "Es gilt Maskenpflicht!",
                "text": "Bitte tragen Sie eine FFP2-Maske in den Fahrzeugen.\n<a href=\"https://www.vbb.de/corona\" target=\"_blank\" rel=\"noopener\">Weitere Informationen</a>",
                "icon": {
                    "type": "HIM0",
                    "title": null
                },
                "priority": 100,
                "products": {
                    "suburban": true,
                    "subway": true,
                    "tram": true,
                    "bus": true,
                    "ferry": true,
                    "express": true,
                    "regional": true
                },
                "company": "VBB",
                "categories": [
                    0
                ],
                "validFrom": "2022-11-16T07:28:00+01:00",
                "validUntil": "2023-12-09T23:59:00+01:00"
            },
            {
                "type": "status",
                "code": "text.realtime.stop.scheduled.dep.time.changed",
                "text": "Achtung: Änderung der Fahrplanzeiten möglich"
            }
        ],
        "origin": null,
        "destination": {
            "type": "stop",
            "id": "900000053301",
            "name": "S Wannsee",
            "location": {
                "type": "location",
                "id": "900053301",
                "latitude": 52.421728,
                "longitude": 13.178932
            },
            "products": {
                "suburban": true,
                "subway": false,
                "tram": false,
                "bus": true,
                "ferry": true,
                "express": true,
                "regional": true
            },
            "stationDHID": "de:11000:900053301"
        },
        "currentTripPosition": {
            "type": "location",
            "latitude": 52.394886,
            "longitude": 13.208579
        }
    }
]
```
