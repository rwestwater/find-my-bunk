# libraries to be imported
from requests_html import HTMLSession
import run_scraper

class Scraper(urls):

    property_name = ""
    property_type = ""
    number_of_bedrooms = int
    number_of_bathrooms = int
    list_all_amenities = {}

    # initialise the class (constructor)
    def __init__():
        # initialising html session class
        session = HTMLSession()
        headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

        url = 'https://www.airbnb.co.uk/rooms/33571268'
        response = session.get(url)

        # sleep gives us a little time buffer between actions, allows mutliple scroll to catch all info on page 
        response.html.render(sleep=1, keep_page=True, scrolldown=2)

        property_name = response.html.find('#site-content > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > div > section > div > div._mbmcsn > h1')
        print(property_name[0].text)

        # def run_through_urls(urls):
            # for url in urls:

                # def_get_property_name
                # def_get_property_type
                # def_get_number_of_bedrooms
                # get_number_of_bathrooms
                # get_dict_of_amenities

        # for name in property_name:
        #     property = {'property name': name.text}
        #     print(property_name)