var kwɪəri = {
    /*
     * Retrieve markers from local API
     */
    retrieveWifiMarkers: function() {'use strict';
        var url = "http://localhost:5000/markers", 
		headers = {}, 
        data = {
            "lat": googleMaps.myLatLng['lat'],
            "long": googleMaps.myLatLng['lng'],
            "radius": googleMaps.myLatLng['radius']
        };
        $.ajax({
            url: url,
            method: 'GET',
            headers: headers,
            contentType: 'application/json',
            dataType: 'json',
            data: data,
            success: function(data, status, jqXHR) {
            	// Clear existing results
            	$('#results').replaceWith('<div id="results"></div>');		                	
                for (var i = 0; i < data.length; i ++) {
                	// Update results div with new address
                	$('#results').append('<span style="font-weight: bold;font-size:large;">'+(i+1)+')</span> '+data[i]['address']+' ');
                	// Add markers to map
    				googleMaps.markers[i] = googleMaps.setMarker(data[i]['address'], i, data[i]['lat'], data[i]['long']);
                }
            },
            error: function(jqXHR, status, error) {
                console.log(status + ", " + error);
                console.log(jqXHR);
            },
            complete: function() {
            },
            timeout: 30000
        });
    },
    /*
     * Initialise list of markers
     */
    init: function() {'use strict';
		kwɪəri.retrieveWifiMarkers();
    }		    
};