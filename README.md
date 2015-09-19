# kwɪəri

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

# Reference App

![Alt text](/app/app.png?raw=true "kwɪəri")
