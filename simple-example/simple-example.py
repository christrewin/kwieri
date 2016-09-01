import requests

def get_oauth_token(auth_url='https://api.telstra.com/v1/oauth/token', 
                                scope='WIFI', grant_type='client_credentials',
                                client_id='<id_param>', client_secret='<secret_param>'):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    # HTTP body is populated with pre-set or passed-in function parameters
    data = 'client_id={}&client_secret={}&grant_type={}&scope={}' \
        .format(client_id, client_secret, grant_type, scope)
    # Make request and return response object
    r = requests.post(auth_url, headers=headers, data=data)
    return r
    

def get_ten_records(token, lat='-37.818496', longi='144.953240', radius_m='100'):
    # note that max radius is 2000m
    bearer_token = 'Bearer {}'.format(str(token))
    headers = {
        'Authorization': bearer_token,
    }
    r = requests.get('https://api.telstra.com/v1/wifi/hotspots?lat={}&long={}&radius={}'.format(lat, longi, radius_m), 
        headers=headers)
    return r


if __name__ == '__main__':
    # Get bearer token and make wifi records call with it
    # Could set an expiry timer to reduce number of auth calls
    full_token = get_oauth_token()
    records = get_ten_records(full_token.json()['access_token'])
    
    # Print out HTTP codes from the auth and records API calls
    print('token code: {}'.format(str(full_token.status_code)))
    print('records code: {}'.format(str(records.status_code)))
    
    # Print out stringified JSON results
    print('token response: {}'.format(str(full_token.json())))
    print('records response: {}'.format(str(records.json())))
