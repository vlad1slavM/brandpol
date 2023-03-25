from contollers.get_cites import get_city_names


cites = get_city_names('static/russian-cities.json')

url = 'https://mediakit-portals.shkulevholding.ru/our-team'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/50.0.2661.102 Safari/537.36'}
