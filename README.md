# kwɪəri

![Alt text](/app/app.png?raw=true "kwɪəri")

# Summary

Web app consists of two main parts.

1) Python app server, calls Telstra WiFi Location API & protects consumer key & secret

Requires authorisation so be sure to set your `CONSUMER_KEY` and `CONSUMER_SECRET` in the app.py script. 

```
'client_id': 'CONSUMER_KEY',
'client_secret': 'CONSUMER_SECRET',
```

2) Web App using Google Maps APIs and Flask API (Python App) to present Wifi Locations on a map.

Be sure to set the `var url = "http://localhost:5000/markers"` to your own server within the `js/kwieri.js` script.

# Build

`docker build -t kwieri ./kwieri`

# Deploy

`docker run -d --name kwieri -p 80:80 -p 5000:5000 -i -t kwieri`

# Python Flask API

Request

```
curl -X "GET" "http://localhost:5000/markers?lat=-37.818822&long=144.953949&radius=100" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

Response

```
[
  {
    "address": "bus waiting room",
    "city": "docklands",
    "lat": -37.818822,
    "long": 144.953949,
    "state": "vic"
  },
  {
    "address": "sthn conc wait rm",
    "city": "docklands",
    "lat": -37.818822,
    "long": 144.953949,
    "state": "vic"
  },
  {
    "address": "bay 58 bus term",
    "city": "docklands",
    "lat": -37.818822,
    "long": 144.953949,
    "state": "vic"
  },
  {
    "address": "600 collins st, near",
    "city": "melbourne",
    "lat": -37.81892,
    "long": 144.95491,
    "state": "vic"
  },
  {
    "address": "66 spencer st, near",
    "city": "melbourne",
    "lat": -37.819515,
    "long": 144.954524,
    "state": "vic"
  }
]
```

# Need more scale?

HAProxy Load Balancer

```
frontend kwieri_app_fe
    bind *:80
    default_backend kwieri_app_be

backend kwieri_app_be
    balance leastconn
    option httpclose
    option forwardfor
    server app1 kwieri_1:80
    server app2 kwieri_2:80
    server app3 kwieri_3:80
    server app4 kwieri_4:80

frontend kwieri_api_fe
    bind *:5550
    default_backend kwieri_api_be

backend kwieri_api_be
    balance leastconn
    option httpclose
    option forwardfor
    server api1 kwieri_1:5551
    server api2 kwieri_2:5552
    server api3 kwieri_3:5553
    server api4 kwieri_4:5554
```

Docker Containers

```
docker run -d --name kwieri_1 -p 8091:80 -p 5551:5000 -i -t kwieri
docker run -d --name kwieri_2 -p 8092:80 -p 5552:5000 -i -t kwieri
docker run -d --name kwieri_3 -p 8093:80 -p 5553:5000 -i -t kwieri
docker run -d --name kwieri_4 -p 8094:80 -p 5554:5000 -i -t kwieri
```