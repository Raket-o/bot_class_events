"""
Модуль запросов информации по отелям
"""
import json
import re
import logging
from logging import Logger
from config_data import config
from datetime import date, timedelta
from requests import request


URL_COUNTRY = "https://hotels4.p.rapidapi.com/get-meta-data"
URL_CITIES = "https://hotels4.p.rapidapi.com/locations/search"
URL_CITY_AREA = "https://hotels4.p.rapidapi.com/locations/v2/search"
URL_HOTELS = "https://hotels4.p.rapidapi.com/properties/v2/list"
URL_DETAL_HOTEL = "https://hotels4.p.rapidapi.com/properties/v2/detail"

logger: Logger = logging.getLogger("logger_main.get_meta_data")



def list_country() -> list[list[str, int]]:
    """
    Функция list_country. Делает запрос и парсит список стран.
    :return: список[кортеж[название страны | 0]] - в кортеже второй элемент обязателен,
            для функции создания кнопок
    """
    response = request("GET", URL_COUNTRY, headers=config.HAEDERS_RAPID, timeout=10)

    data = json.loads(response.text)
    print(data)
    lst_country = [(i_country["name"], 0)
                   for i_country in data
                   if not re.findall(r'_', i_country["name"])]
    lst_country.append(("AMERICA", 0))

    return lst_country



def list_cities(user_country: str = None) -> list[tuple[str, int]]:
    """
    Функция list_country. Принимает на вход название страну. Делает запрос и парсит список городов.
    :return: кортеж[кортеж[название города, ид_города]]
    """
    querystring = {"query": user_country, "locale": "en_EN"}
    response = request("GET", URL_CITIES, headers=config.HAEDERS_RAPID, params=querystring, timeout=10)
    data = json.loads(response.text)

    lst_city = []
    country = str(data['term'])
    if data['suggestions'][0]['group'] == 'CITY_GROUP':
        lst_city = tuple((i_city['name'], i_city['destinationId'])
                         for i_city in data['suggestions'][0]['entities']
                         if country.capitalize() in i_city['caption'])

    return lst_city


def list_cities_area(user_city: str = None) -> tuple[tuple[str, int]]:
    """
    Функция list_cities_area. Принимет на вход название города. Делает запрос и парсит список округов.
    :return: кортеж[кортеж[название округа, ид_округа]]
    """
    querystring = {"query": user_city, "locale": "en_US", "currency": "USD"}
    response = request("GET", URL_CITY_AREA, headers=config.HAEDERS_RAPID, params=querystring, timeout=10)
    data = json.loads(response.text)

    # lst_city_area = []
    # for i in data["suggestions"]:
    #     for j in i["entities"]:
    #         geoId = j["geoId"]
    #         name_area = j["name"]
    #         lst_city_area.append((name_area, geoId))

    lst_city_area = tuple((j["name"], j["geoId"]) for i in data["suggestions"] for j in i["entities"])

    return lst_city_area


def list_hotels(regionId: int,
                checkIn: date,
                checkOut: date,
                sort: str,
                qty_hotels: int) -> tuple[tuple[str, int, int], ...]:
    """
    Функция list_hotels. Принимет на вход ид_округа, дату заезда, дату выезда,
    метод сортировки и кол-во отелей которые нужно вывести.
    Делает запрос и парсит список отелей.
    :return: кортеж[кортеж[название отеля, ид_отеля, стоимость номера за сутки]]
    """

    payload = {
        "currency": "RUB",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": regionId},
        "checkInDate": {
            "day": checkIn.day,
            "month": checkIn.month,
            "year": checkIn.year
        },
        "checkOutDate": {
            "day": checkOut.day,
            "month": checkOut.month,
            "year": checkOut.year
        },
        "rooms": [
            {
                "adults": 1,
                # "children": [{"age": 5}, {"age": 7}]
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": qty_hotels,
        "sort": sort,
        # "sort": "PRICE_HIGH_TO_LOW",
        # "filters": {"price": {
        #     "max": 1500,
        #     "min": 100
        # }}
    }

    response = request("POST", URL_HOTELS, json=payload, headers=config.HAEDERS_RAPID, timeout=10)
    data = json.loads(response.text)
    print(data)

    try:
        lts_hotels = tuple((i["name"], i["id"], i["price"]["options"][0]["formattedDisplayPrice"])
                        for i in data["data"]["propertySearch"]["properties"])
    except IndexError as err:
        logger.error("list_hotels", err)
        lts_hotels = [(i["name"], i["id"], "temporarily unavailable")
                      for i in data["data"]["propertySearch"]["properties"]]

    return lts_hotels


def detal_hotel(id_hotel: int) -> [str, tuple[float, float], float, list[str, ...]]:
    """
    Функция detal_hotel. Принимет на вход ид_отеля.
    Делает запрос и парсит список делати отеля.
    :return: название отеля, кортеж_коордит[широти,долгота], рейтинг отеля, список[URL фотографий]
    """

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        # "siteId": 300000001,
        "propertyId": id_hotel
    }

    response = request("POST", URL_DETAL_HOTEL, json=payload, headers=config.HAEDERS_RAPID, timeout=10)
    print(response.text)
    data = json.loads(response.text)
    name_hotel = data["data"]["propertyInfo"]["summary"]["name"]

    try:
        rating_hotel = data["data"]["propertyInfo"]["summary"]["overview"]["propertyRating"]["rating"]
    except TypeError as err:
        logger.error("detal_hotel", err)
        rating_hotel = "temporarily unavailable"

    coord_hotel, *_ = tuple(
        (i["mapMarker"]["latLong"]["latitude"], i["mapMarker"]["latLong"]["longitude"])
        for i in data["data"]["propertyInfo"]["summary"]["map"]["markers"]
        if i["mapMarker"]["icon"] == "HOTEL"
    )

    photos = tuple(
        i["images"][0]["image"]["url"]
        for i in data["data"]["propertyInfo"]["propertyGallery"]["imagesGrouped"]
    )

    print(name_hotel)
    print(coord_hotel)
    print(rating_hotel)
    print(photos)

    return name_hotel, coord_hotel, rating_hotel, photos
