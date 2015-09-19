# kwɪəri

# Reference App

![Alt text](/app/app.png?raw=true "kwɪəri")

# Summary

This app consists of two main parts.

1) A Python app serving client requests for Wifi Location & protecting API keys & secrets

Main bit: The markers route is the part that calls the Telstra WiFi API and returns a JSON object of markers. Returns empty if none. Requires OAuth token so be sure to set your client id and secret.

```
@app.route('/markers', methods = ['GET', 'OPTIONS'])
```

2) A Web App making requests for WiFi Locations when the lense is moved or a new location is specified (click)

Main bit: On load the kwɪəri object is initialised and a default location is used to set markers. In the processes `kwɪəri.retrieveWifiMarkers()` is fired making an ajax call to the python API.

```
retrieveWifiMarkers: function() {'use strict';
		        var url = "http://localhost:5550/markers", 
```

# Build

`docker build -t kwieri ./kwieri`

# Deploy

`docker run -d -v $HOME/docker/kwieri/app/www:/app/www -v $HOME/docker/k1:/var/log/apache2 -v $HOME/docker/kwieri/k1:/app/kwieri --name kwieri1 -p 8091:80 -p 5551:5000 -i -t kwieri`

# API

```
curl -X "GET" "http://localhost:5550/markers?lat=-37.818822&long=144.953949&radius=100" \
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
