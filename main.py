from flask import Flask, request, render_template
from utils import getDistanceFromLatLonInKm
from query_restaurants import new_restaurants, nearby_restaurants, popular_restaurants
import requests
import json

app = Flask(__name__)


@app.route('/discovery')
def query() -> json:
    """Endpoint to make requests

    Returns:
        response: JSON object of the restaurants
    """
    url = 'https://raw.githubusercontent.com/woltapp/summer2021-internship/main/restaurants.json'
    response = requests.get(url)
    text_form = json.loads(response.text)

    if not request.args:
        return json.dumps(text_form)

    lat_arg = float(request.args['lat'])
    lon_arg = float(request.args['lon'])

    return json.dumps(handle_json_query(text_form, lat_arg, lon_arg))


def handle_json_query(text_form: str, guestlat: float = 60.169857, guestlon: float = 24.938379) -> dict:
    """Queries the restaurants.json given in GitHub.

    Args:
        text_form (str)           : restaurants response from the endpoint 
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
            restaurants_in_range.append(restaurant)

    restaurants_in_range.sort(key=lambda r: getDistanceFromLatLonInKm(
        r['location'][1], r['location'][0], guestlat, guestlon))

    restaurants = {
        "sections": [
            popular_restaurants(restaurants_in_range),
            new_restaurants(restaurants_in_range),
            nearby_restaurants(restaurants_in_range)
        ]
    }

    restaurants['sections'] = list(
        filter(lambda r_list: len(r_list['restaurants']) != 0, restaurants['sections']))
    return restaurants


if __name__ == '__main__':
    app.run(debug=True)
