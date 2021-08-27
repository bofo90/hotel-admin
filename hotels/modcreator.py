import requests, csv

from django.conf import settings

from .models import City, Hotel

def download_from_api(url):
    """
    Read files from url and create data. Return -1 if files could not be found.
    """
    with requests.Session() as s:
        download = s.get(url, auth=(settings.CSV_USERNAME, settings.CSV_PASSWORD))
        if (download.status_code == 401):
            return -1
        
        decoded = download.content.decode('utf-8')
        csv_data = csv.reader(decoded.splitlines(), delimiter=';')
        return list(csv_data)


def create_city_models():
    """
    Create models of cities with code and name from list
    """
    list_cities = download_from_api(settings.CITY_CSV)

    if list_cities == -1:
        print("Could not retrieve city-data from api.")
    else:
        for elem in list_cities:
            city, _ = City.objects.get_or_create(
                code=elem[0],
                name=elem[1],
            )
        print("City-data retrieved correctly.")


def create_hotel_models():
    """
    Create models of hotels with code, name and link to a city
    """
    list_hotels = download_from_api(settings.HOTEL_CSV)

    if list_hotels == -1:
        print("Could not retrieve hotel-data from api.")
    else:
        for elem in list_hotels:
            city = City.objects.get(code=elem[0])
            hotel, _ = Hotel.objects.get_or_create(
                city = city,
                name = elem[2],
                code = elem[1],
            )
        print("Hotel-data retrieved correctly.")

