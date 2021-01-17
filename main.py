from flask import Flask, request
from utils import nearby_restaurants, getDistanceFromLatLonInKm, popular_restaurants, is_older_than_4mo, new_restaurants
import requests

import json

app = Flask(__name__)

url = 'https://raw.githubusercontent.com/woltapp/summer2021-internship/main/restaurants.json'

response = requests.get(url)

text_form = json.loads(response.text)


@app.route('/discovery')
def query():
    """Endpoint to make requests

    Returns:
        response: JSON object of the restaurants
    """
    lat_arg = float(request.args['lat'])
    lon_arg = float(request.args['lon'])
    print(lat_arg, lon_arg)

    return json.dumps(handle_json_query(lat_arg, lon_arg))


def handle_json_query(guestlat: float = 60.169857, guestlon: float = 24.938379) -> dict:
    """Queries the restaurants.json given in GitHub.

    Args:
        guestlat (float, optional): url argument for latitude. Defaults to 60.169857.
        guestlon (float, optional): url argument for longitude. Defaults to 24.938379.

    Returns:
        dict: returns new object consisting of 3 lists of restaurants
    """

    wolt_json = text_form['restaurants']
    restaurants_in_range = []
    for restaurant in wolt_json:
        lon = float(restaurant['location'][0])
        lat = float(restaurant['location'][1])
        distance = getDistanceFromLatLonInKm(guestlat, guestlon, lat, lon)
        if(distance is not None):
            print(distance, restaurant['name'])
            restaurants_in_range.append(restaurant)
    restaurants_in_range.sort(key=lambda r: getDistanceFromLatLonInKm(
        r['location'][1], r['location'][0], guestlat, guestlon))
    restaurants = {
        "sections": [
            {
                "title": "Popular restaurants",
                "restaurants": popular_restaurants(restaurants_in_range)
            },
            {
                "title": "New Restaurants",
                "restaurants": new_restaurants(restaurants_in_range)
            },
            {
                "title": "Nearby Restaurants",
                "restaurants": nearby_restaurants(restaurants_in_range)
            }
        ]
    }
    return restaurants


if __name__ == '__main__':
    app.run(debug=True)
