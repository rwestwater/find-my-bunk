# libraries to be imported
from requests_html import HTMLSession
import os
import json

class Scraper():

    # initialise the class (constructor)
    def __init__(self, airbnb_urls):

        try: 
            if not os.path.exists('./json_results/'): # if jsons result dir doesn't exist
                os.makedirs('./json_results/') # make it
        except Exception as e:
            print(("\nJson folder could not be created:\n{}\n").format(e))

        try:
            self.session = HTMLSession() # initialising html session class
            self.run_everything(airbnb_urls) # passes in the urls from find_my_bunk
        except Exception as e:
            print(("\nFatal error - session not started. Exiting script:\n{}\n").format(e))
            exit()

    # find all the elements on the page
    def get_all_info(self, response):
        try: 
            all_property_info = response.html.find('#site-content > div > div') # returns a string
            all_property_info = all_property_info[0].text.splitlines() # split the returned string into lists
            return all_property_info
        except Exception as e:
            print(("\nSite information not retrieved, please check element paths, exitting:\n{}\n").format(e))

    def create_results_json(self, property_name):
        try:
            open(('json_results/{}.json'.format(property_name)), 'wb') # creates json file with the property name as the filename
        except Exception as e:
            print(("\nJson results file could not be created:\n{}\n").format(e))
       
    def get_property_name(self, all_property_info):
        try:
            property_name = all_property_info[0] # take the name from the first position in the list
            self.create_results_json(property_name) # pass property name to create json
            return property_name
        except Exception as e:
            print(("\nCannot retrieve property name:\n{}\n").format(e))

    def get_property_type(self, all_property_info):
        try:
            # i for i (iterates through list), if string in all_property_info == 'hosted', return result
            property_type_index_position = [i for i, str in enumerate(all_property_info) if 'hosted' in str]
            property_type_index_position = int(property_type_index_position[0]) # takes the first result of index position
            property_type = all_property_info[property_type_index_position] # helps us find the property type in the all_property_info list es result = [12]
            return property_type
        except Exception as e:
            print(("\nSearch for property type failed, check index position exists:\n{}\n").format(e))

    def get_number_of_beds_and_baths(self, all_property_info):
        try:
            bedrooms_index_position = [i for i, str in enumerate(all_property_info) if 'guests' in str]
            bedrooms_index_position = int(bedrooms_index_position[0])
            number_of_bedrooms = all_property_info[bedrooms_index_position] 
            number_of_bedrooms = number_of_bedrooms.split("·") # split list at dot to access individual items
            return number_of_bedrooms
        except Exception as e:
            print(("\nSearch for number of beds/bathrooms failed, check index position exists:\n{}\n").format(e))

    def get_list_of_amenities(self, all_property_info):
        try:
            amenities_index_position = [i for i, str in enumerate(all_property_info) if 'Amenities:' in str]
            amenities_index_position = int(amenities_index_position[0])
            list_of_amenities = all_property_info[amenities_index_position] 
            return list_of_amenities
        except Exception as e:
            print(("\nSearch for amenities failed, check index position exists:\n{}\n").format(e))

    def run_everything(self, airbnb_urls):
        try:
            for url in airbnb_urls:
                response = self.session.get(url)
                property_info_dict = {}

                # sleep gives us a little time buffer between actions
                response.html.render(sleep=5, keep_page=True)
                info = self.get_all_info(response)
                property_name = self.get_property_name(info)
                property_type = self.get_property_type(info)
                number_of_beds_and_baths = self.get_number_of_beds_and_baths(info)
                list_of_amenities = self.get_list_of_amenities(info)
                print("___________________")

                property_info_dict["property_name"] = property_name
                property_info_dict["property_type"] = property_type
                property_info_dict["number_of_beds_and_baths"] = number_of_beds_and_baths
                property_info_dict["list_of_amenities"] = list_of_amenities

                try:
                    with (open(('json_results/{}.json'.format(property_name)), 'w')) as json_file:
                        json.dump(property_info_dict, json_file)
                except Exception as e:
                    print(("\nCannnot parse json to result file:\n{}\n").format(e))

        except Exception as e:
            print(("\nCannot access urls, please check they are correct. Exiting script:\n{}\n").format(e))
            exit()