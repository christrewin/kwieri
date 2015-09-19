# kwɪəri

# Reference App

![Alt text](/app/app.png?raw=true "kwɪəri")

# Summary

This app consists of two main parts.

1) A Python app serving client requests for Wifi Location & protecting API keys & secrets

Main bit: The markers route is the part that calls the Telstra WiFi API and returns a JSON object of markers.

```
@app.route('/markers', methods = ['GET', 'OPTIONS'])
```

Note: Requires OAuth token so be sure to set your `CONSUMER_KEY` and `CONSUMER_SECRET` in the app.py script. 

```
'client_id': 'CONSUMER_KEY',
'client_secret': 'CONSUMER_SECRET',
```

2) A Web App making requests for WiFi Locations when the lense is moved or a new location is specified (click)

Main bit: On load the kwɪəri object is initialised and a default location is used to set markers. In the processes `kwɪəri.retrieveWifiMarkers()` is fired making an ajax call to the python API.

```
retrieveWifiMarkers: function() {'use strict';
    var url = "http://localhost:5000/markers", 
```

Note: be sure to set the `var url = "http://localhost:5000/markers"` to your own server within the `js/kwieri.js` script.

# Build

`docker build -t kwieri ./kwieri`

# Deploy

`docker run -d --name kwieri -p 80:80 -p 5000:5000 -i -t kwieri`

# API

```
curl -X "GET" "http://localhost:5000/markers?lat=-37.818822&long=144.953949&radius=100" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

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
