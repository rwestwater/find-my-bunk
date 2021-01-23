# libraries to be imported
from requests_html import HTMLSession

class Scraper():

    property_name = ""
    property_type = ""
    number_of_bedrooms = int
    number_of_bathrooms = int
    list_all_amenities = {}
    
    # initialise the class (constructor)
    def __init__(self, airbnb_urls):
        # initialising html session class
        self.session = HTMLSession()
        self.run_everything(airbnb_urls)

            
    def get_property_name(self, response):
        property_name = response.html.find('#site-content > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > div > section > div > div._mbmcsn > h1')
        print(property_name[0].text)

    def get_property_type(self, response):
        property_type = response.html.find('#site-content > div > div._qcb6sd > div:nth-child(2) > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div._jro6t0 > div._tqmy57 > div._1qsawv5 > p')
        print(property_type)
        # print(property_type[0].text)

    def get_number_of_bedrooms(self, response):
        number_of_bedrooms = response.html.find('#site-content > div > div._qcb6sd > div:nth-child(2) > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div:nth-child(2) > span:nth-child(3)')
        print(number_of_bedrooms[0].text)

    def get_number_of_bathrooms(self, response):
        number_of_bathrooms = response.html.find('#site-content > div > div._qcb6sd > div:nth-child(2) > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div:nth-child(2) > span:nth-child(7)')
        print(number_of_bathrooms[0].text)

    def get_list_of_amenities(self, response):
        list_of_amenities = response.html.find('#site-content > div > div._qcb6sd > div:nth-child(2) > div:nth-child(8) > div > div > div > div:nth-child(2) > div._1byskwn')
        print(list_of_amenities[0].text)

    def run_everything(self, airbnb_urls):
        for url in airbnb_urls:
            response = self.session.get(url)

            # sleep gives us a little time buffer between actions, allows mutliple scroll to catch all info on page 
            response.html.render(sleep=1, keep_page=True, scrolldown=2)
            self.get_property_name(response)
            self.get_property_type(response)
            self.get_number_of_bedrooms(response)
            self.get_number_of_bathrooms(response)
            # self.get_list_of_amenities(response)

