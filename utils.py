import math
import datetime
from dateutil import relativedelta


def is_older_than_4mo(date: str) -> bool:
    """Checks whether the given date is older than 4 months or not.

    Args:
        date (str): Date in string format (e.g. "2020-03-21")

    Returns:
        bool: True if the date is older than 4 months, False if otherwise.
    """

    date_today = datetime.date.today()
    opening_date = datetime.datetime.strptime(str(date), '%Y-%m-%d')
    r = relativedelta.relativedelta(opening_date, date_today)
    if(abs(r.months) > 4):
        return True
    return False


def getDistanceFromLatLonInKm(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates the distance between two coordinate points.

    https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

    Args:
        lat1 (float): argument latitude
        lon1 (float): argument longitude
        lat2 (float): latitude from restaurants.json
        lon2 (float): longitude from restaurants.json

    Returns:
        float: distance if it's less or equal to 1.5km
    """
    R = 6371
    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    if (d <= 1.5):
        return d
