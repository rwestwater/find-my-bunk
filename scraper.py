import requests
from ghost import Ghost
from bs4 import BeautifulSoup

ghost = Ghost()

url = 'https://www.airbnb.co.uk/rooms/33571268'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

page = requests.get(url, headers=headers)

ghost.open(url)
current_state = ghost.content

# creating a BeautifulSoup Obj to play around with
soup = ghost.BeautifulSoup(page.content, 'html.parser')

property_name = soup.find(id="TITLE_DEFAULT")
property_type = ""
number_of_bedrooms = ""
number_of_bathrooms = ""
list_all_amenities = ""

print (current_state)