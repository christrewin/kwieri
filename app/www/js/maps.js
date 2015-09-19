var googleMaps = {
	map: 0,
	focusRadius: null,
	markerIcon: "img/icon.png",
	markers: [],
    /*
     * Default Map Center
     */
    myLatLng: {
    	lat: -37.818822, 
    	lng: 144.953949,
    	radius: 260
    },
	// Sets the map on all markers in the array.
	setMapOnAll: function(map) {'use strict';
		for (var i = 0; i < googleMaps.markers.length; i++) {
			googleMaps.markers[i].setMap(map);
		}
	},
	// Removes the markers from the map, but keeps them in the array.
	clearMarkers: function() {'use strict';
		googleMaps.setMapOnAll(null);
	},
	// Deletes all markers in the array by removing references to them.
	deleteMarkers: function() {'use strict';
		googleMaps.clearMarkers();
		googleMaps.markers = [];
	},
	// Deletes all markers in the array by removing references to them.
	setRadius: function() {'use strict';
		googleMaps.focusRadius = new google.maps.Circle({
			strokeColor: '#FF0000',
			strokeOpacity: 0.8,
			strokeWeight: 2,
			fillColor: '#FF0000',
			fillOpacity: 0.15,
			map: googleMaps.map,
			draggable: true,
			center: googleMaps.myLatLng,
				radius: googleMaps.myLatLng['radius']
		});

		googleMaps.focusRadius.addListener('dragend', function() {
        	googleMaps.deleteMarkers();
            googleMaps.myLatLng['lat'] = googleMaps.focusRadius.getCenter().lat();
            googleMaps.myLatLng['lng'] = googleMaps.focusRadius.getCenter().lng();
            kwɪəri.retrieveWifiMarkers();					
		});
	},
    /*
     * creates a marker for the map and returns it
     * by default, the marker does NOT show on the map
     */
    setMarker: function(name, number, lat, lng) {'use strict';
        var image, size, marker;
        size = Math.round(Math.pow(2,googleMaps.map.getZoom()/2.9));
        image = {
            url: googleMaps.markerIcon,
            size: new google.maps.Size(size, size), //size
            scaledSize: new google.maps.Size(size, size) // scaled size (required for Retina display icon)
        };
        if (typeof number === null) {
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(lat,lng),
                map: googleMaps.map,
                draggable: true,
                title: name,
                icon: image
            });
        } else {
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(lat,lng),
                map: googleMaps.map,
                draggable: true,
                title: name,
                number: number,
                icon: image
            });
        }
        marker.setDraggable(false);
        $('#map-canvas div.gmnoprint[alarm="true"]').css({
            "border-radius" : size + "px",
        });;
        return marker;
    },
    /*
     * creates the google map
     */
    init: function() {'use strict';
        var element, options;
        element = $('#map-canvas')[0];
        options = {
            center: googleMaps.myLatLng,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        googleMaps.map = new google.maps.Map(element, options);

        // update map when window is resized
        google.maps.event.trigger(googleMaps.map, 'resize');

        google.maps.event.addListener(googleMaps.map, 'click', function(event) {
        	googleMaps.deleteMarkers();
            googleMaps.myLatLng['lat'] = event.latLng.lat();
            googleMaps.myLatLng['lng'] = event.latLng.lng();
        	googleMaps.focusRadius.setMap(null);
        	googleMaps.setRadius();
            kwɪəri.retrieveWifiMarkers();
        });

        // set initial radius, this is draggable
        googleMaps.setRadius();
    }
};