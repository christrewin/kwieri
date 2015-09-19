# Program: app.py
# Author: Chris Trewin (chris.trewin@gmail.com)
# Date: 19/09/2015
# Version: 0.0.1

from flask import Flask, url_for, json, make_response, request, current_app, Response
import requests
from requests.auth import AuthBase
from datetime import timedelta
from functools import update_wrapper

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error=None):
	obj = {
		'status': 400,
		'message': 'Not Found: ' + request.url
	}
	message = json.dumps(obj)
	resp = Response(message, status=400, mimetype=request.headers['Content-Type'])
	resp.headers['Server'] = 'kwieri'
	resp.headers['Version'] = '0.0.1'
	return resp


@app.errorhandler(404)
def not_found(error=None):
	obj = {
		'status': 404,
		'message': 'Not Found: ' + request.url
	}
	message = json.dumps(obj)
	resp = Response(message, status=404, mimetype=request.headers['Content-Type'])
	resp.headers['Server'] = 'kwieri'
	resp.headers['Version'] = '0.0.1'
	return resp


@app.errorhandler(500)
def internal_error(error=None):
	obj = {
		'status': 500,
		'message': 'Not Found: ' + request.url
	}
	message = json.dumps(obj)
	resp = Response(message, status=500, mimetype=request.headers['Content-Type'])
	resp.headers['Server'] = 'kwieri'
	resp.headers['Version'] = '0.0.1'
	return resp


app.error_handler_spec[None][400] = bad_request
app.error_handler_spec[None][404] = not_found
app.error_handler_spec[None][500] = internal_error

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

class OAuth(AuthBase):
    def __init__(self, token):
        # setup any auth-related data here
        self.token = token

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = "Bearer "+self.token
        return r


def retrieveToken():
	url = "https://api.telstra.com/v1/oauth/token"
	headers = {'user-agent': 'kwieri/0.0.1'}
	payload = {
		'client_id': 'CONSUMER_KEY',
		'client_secret': 'CONSUMER_SECRET',
		'grant_type': 'client_credentials',
		'scope': 'WIFI'
	}
	r = requests.get(url, params=payload)
	return r.json()


def retrieveMarkers(lat, long, radius):
	access_token = retrieveToken()['access_token']
	print(access_token)
	url = "https://api.telstra.com/v1/wifi/hotspots"
	headers = {
		'user-agent': 'kwieri/0.0.1'
	}
	payload = {
		'lat': lat,
		'long': long,
		'radius': radius
	}
	r = requests.get(url, params=payload, auth=OAuth(access_token))
	print(r.request.headers)
	print(r.json())
	return r.json()


'''
Markers
'''
@app.route('/markers', methods = ['GET', 'OPTIONS'])
@crossdomain(origin='*')
def api_markers():

    if 'lat' in request.args:
        lat = request.args['lat']

    if 'long' in request.args:
        long = request.args['long']

    if 'radius' in request.args:
        radius = request.args['radius']

	obj = retrieveMarkers(lat, long, radius)
	resp = Response(json.dumps(obj), status=200, mimetype='application/json')
	resp.headers['Server'] = 'kwieri'
	resp.headers['Version'] = '0.0.1'
	return resp


if __name__ == '__main__':
    app.run()
