# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'https://www.airbnb.co.uk/s/Edinburgh-Old-Town--Edinburgh/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=february&date_picker_type=calendar&place_id=ChIJc1I_X4XHh0gRV9nOqdrZAnk&query=Edinburgh%20Old%20Town%2C%20Edinburgh&checkin=2021-01-24&checkout=2021-01-31&source=search_blocks_selector_p1_flow&search_type=search_query'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'lxml')

for item in soup.select('[itemprop=itemListElement]'):
    try:
        print(item.select('a')[0]['aria-label'])

    except Exception as e:
        print('Error found {e}') %e