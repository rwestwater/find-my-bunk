# libraries to be imported
import os
import json
import sys
from requests_html import HTMLSession

class Scraper():

    # initialise the class (constructor)
    def __init__(self, airbnb_urls):

        try:
            # if jsons result dir doesn't exist, make it
            if not os.path.exists('./json_results/'):
                os.makedirs('./json_results/')
        except Exception as exception:
            print(("\nJson folder could not be created:\n{}\n").format(exception))

        try:
            # initialising html session class
            self.session = HTMLSession()
            # passes in the urls from find_my_bunk
            self.run_everything(airbnb_urls)
        except Exception as exception:
            print(("\nFatal error - session not started. Exiting script:\n{}\n").format(exception))
            sys.exit()

    # find all the elements on the page
    def get_all_info(self, response):
        try:
            # returns a string
            all_property_info = response.html.find('#site-content > div > div')
            # split the returned string into lists
            all_property_info = all_property_info[0].text.splitlines()
            return all_property_info
        except Exception as exception:
            print(("\nSite information not retrieved. Exiting script:\n{}\n").format(exception))

    def create_results_json(self, property_name):
        try:
            # creates json file with the property name as the filename
            open(('json_results/{}.json'.format(property_name)), 'wb')
        except Exception as exception:
            print(("\nJson results file could not be created:\n{}\n").format(exception))

    def get_property_name(self, all_property_info):
        try:
            # take the name from the first position in the list
            property_name = all_property_info[0]
            # pass property name to create json
            self.create_results_json(property_name)
            return property_name
        except Exception as exception:
            print(("\nCannot retrieve property name:\n{}\n").format(exception))

    def get_property_type(self, all_property_info):
        try:
            # iterate through list, if string in all_property_info == 'hosted', return result
            property_type_index_position = [
                                            i for i,
                                            str in enumerate(all_property_info)
                                            if 'hosted' in str
                                            ]
            # takes the first result of index position
            property_type_index_position = int(property_type_index_position[0])
            # helps us find the property type in the all_property_info list es result = [12]
            property_type = all_property_info[property_type_index_position]
            return property_type
        except Exception as exception:
            print(("\nSearch for property type failed:\n{}\n").format(exception))

    def get_number_of_beds_and_baths(self, all_property_info):
        try:
            bedrooms_index_position = [
                                        i for i,
                                        str in enumerate(all_property_info)
                                        if 'guests' in str
                                        ]
            bedrooms_index_position = int(bedrooms_index_position[0])
            number_of_bedrooms = all_property_info[bedrooms_index_position]
            # split list at dot to access individual items
            number_of_bedrooms = number_of_bedrooms.split("·")
            return number_of_bedrooms
        except Exception as exception:
            print(("\nSearch for number of beds/bathrooms failed:\n{}\n").format(exception))

    def get_list_of_amenities(self, all_property_info):
        try:
            amenities_index_position = [
                                        i for i,
                                        str in enumerate(all_property_info)
                                        if 'Amenities:' in str
                                        ]
            amenities_index_position = int(amenities_index_position[0])
            list_of_amenities = all_property_info[amenities_index_position]
            return list_of_amenities
        except Exception as exception:
            print(("\nSearch for amenities failed:\n{}\n").format(exception))

    def run_everything(self, airbnb_urls):
        try:
            for url in airbnb_urls:
                # cycle through all urls passed in by the runner script
                response = self.session.get(url)
                property_info_dict = {}

                # sleep gives us a little time buffer between actions
                response.html.render(sleep=5, keep_page=True)
                # set response to info variable for easy access
                info = self.get_all_info(response)
                property_name = self.get_property_name(info)
                property_type = self.get_property_type(info)
                number_of_beds_and_baths = self.get_number_of_beds_and_baths(info)
                list_of_amenities = self.get_list_of_amenities(info)

                property_info_dict["property_name"] = property_name
                property_info_dict["property_type"] = property_type
                property_info_dict["number_of_beds_and_baths"] = number_of_beds_and_baths
                property_info_dict["list_of_amenities"] = list_of_amenities

                try:
                    # open the relevent json file
                    with (open(('json_results/{}.json'.format(property_name)), 'w')) as json_file:
                        # write the json to the file opened
                        json.dump(property_info_dict, json_file)
                except Exception as exception:
                    print(("\nCannnot parse json to result file:\n{}\n").format(exception))

        except Exception as exception:
            print(("\nCannot access urls. Exiting script:\n{}\n").format(exception))
            sys.exit()
