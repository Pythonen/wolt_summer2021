from utils import is_older_than_4mo


def new_restaurants(restaurants: list) -> dict:
    """Gets the newest restaurants from the given list 

    Args:
        restaurants (list): list of restaurant objects

    Returns:
        dict: Object with title and array of 10 restaurants
    """
    temp = sorted(
        restaurants, key=lambda r: (r['online'], r['launch_date']), reverse=True)
    newest_restaurants = list(filter(
        lambda r: is_older_than_4mo(r['launch_date']) == False, temp))[:10]
    return {"title": "New Restaurants", "restaurants": newest_restaurants}


def popular_restaurants(restaurants: list) -> dict:
    """Gets the most popular restaurants from the given list

    Args:
        restaurants (list): List of restaurants

    Returns:
        dict: Object with title and array of 10 restaurants
    """

    popular_restaurantes = sorted(
        restaurants, key=lambda r: (r['online'], r['popularity']), reverse=True)[:10]
    return {"title": "Popular Restaurants", "restaurants": popular_restaurantes}


def nearby_restaurants(restaurants: list) -> dict:
    """Nearby restaurants from restaurants.json. Emphasis on wheter the restaurant is open or not. 

    Args:
        restaurants (list): List of restaurants that are at most 1.5km away.

    Returns:
        list: Sorted list of restaurants
    """
    restaurantes = sorted(
        restaurants, key=lambda r: r['online'], reverse=True)[:10]

    return {"title": "Nearby Restaurants", "restaurants": restaurantes}
