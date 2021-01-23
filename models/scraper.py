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

    def get_all_info(self, response):
        all_property_info = response.html.find('#site-content > div > div')
        all_property_info = all_property_info[0].text.splitlines()
        return all_property_info
       
    def get_property_name(self, all_property_info):
        property_name = all_property_info[0]
        print("Property name: " + property_name)

    def get_property_type(self, all_property_info):
        property_type_index_position = [i for i, str in enumerate(all_property_info) if 'hosted' in str]
        property_type_index_position = int(property_type_index_position[0])
        property_type = all_property_info[property_type_index_position] 
        print("Property type: " + property_type)

    def get_number_of_bedrooms(self, all_property_info):
        bedrooms_index_position = [i for i, str in enumerate(all_property_info) if 'guests' in str]
        bedrooms_index_position = int(bedrooms_index_position[0])
        number_of_bedrooms = all_property_info[bedrooms_index_position] 
        print("Number of bedrooms: " + number_of_bedrooms)

    def get_number_of_bathrooms(self, all_property_info):
        bathrooms_index_position = [i for i, str in enumerate(all_property_info) if 'guests' in str]
        bathrooms_index_position = int(bathrooms_index_position[0])
        number_of_bathrooms = all_property_info[bathrooms_index_position]
        print("Number of bathrooms: " + number_of_bathrooms) 

    def get_list_of_amenities(self, all_property_info):
        list_of_amenities = response.html.find('#site-content > div > div._qcb6sd > div:nth-child(2) > div:nth-child(8) > div > div > div > div:nth-child(2) > div._1byskwn', first=True)
        print(list_of_amenities.text)

    def run_everything(self, airbnb_urls):
        for url in airbnb_urls:
            response = self.session.get(url)

            # sleep gives us a little time buffer between actions, allows mutliple scroll to catch all info on page 
            response.html.render(sleep=5, keep_page=True)
            info = self.get_all_info(response)
            self.get_property_name(info)
            self.get_property_type(info)
            self.get_number_of_bedrooms(info)
            # self.get_number_of_bathrooms(info)
            # self.get_list_of_amenities(info)

