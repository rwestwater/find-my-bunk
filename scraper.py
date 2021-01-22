# libraries to be imported
from requests_html import HTMLSession

# initialising html session class for multiple sites at the same time
session = HTMLSession()
# headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

url = 'https://www.airbnb.co.uk/rooms/33090114'
response = session.get(url)

# sleep gives us a little time buffer between actions, allows mutliple scroll to catch all info on page 
response.html.render(sleep=1, keep_page=True, scrolldown=5)

property_name = response.html.search('span')
print(property_name)

# for name in property_name:
#     property = {'property name': name.text}
#     print(property_name)

property_type = ""
number_of_bedrooms = ""
number_of_bathrooms = ""
list_all_amenities = ""