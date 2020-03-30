import requests
from bs4 import BeautifulSoup

page_name = "https://www.autovit.ro/autoturisme/?search%5Border%5D=created_at%3Adesc"
page_at = 0
number_of_pages = 10


class Car:
    def __init__(self, url, title, price, photos, description):
        self.url = url
        self.title = title
        self.price = price
        self.photos = photos
        self.description = description


def get_scraping_page_url():
    global page_at, page_name
    page_at += 1
    return page_name + "&page=" + str(page_at)


def get_page_html(page_url):
    response = requests.get(page_url)
    return BeautifulSoup(response.text, 'html.parser')


def get_all_vehicles_url(page_html):
    offers = page_html.findAll("article",
                               class_="adListingItem offer-item is-row promoted is-active has-feature-shop ds-ad-card-experimental")
    offers_links = []
    for offer in offers:
        offers_links.append(offer.findAll("a", class_="offer-title__link")[0]['href'])
    return offers_links


def get_car_information(car_url):
    car_html = get_page_html(car_url)
    car_title = car_html.findAll("span", class_="offer-title big-text fake-title")[0].text.rstrip().lstrip()
    photos_url_html = car_html.findAll("img", class_="lazyload")
    car_photos = set()
    for photo_url_html in photos_url_html:
        car_photos.add(photo_url_html['data-src'])
    car_description = car_html.findAll("div", class_="offer-description__description")[0].text
    car_price = car_html.findAll("span", class_="offer-price__number")[0].text.rstrip().lstrip()
    return Car(car_url, car_title, car_price, car_photos, car_description)


def get_one_announcements_page_data(url):
    car_urls = get_all_vehicles_url(get_page_html(url))
    cars = []
    for car_url in car_urls:
        cars.append(get_car_information(car_url))
    return cars


def get_all_announcements():
    global number_of_pages
    cars = []
    for i in range(number_of_pages):
        cars.append(get_one_announcements_page_data(get_scraping_page_url()))
    return cars


get_all_announcements()