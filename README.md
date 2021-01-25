# find-my-bunk
An application web scraper written in Python that displays and stores information scraped from airbnb listings

## Pseudocode
```
for url in urls:
    loop through each response:
        return property name
        return property type
        return number of bedrooms and bathrooms
        return list of amenities

        write return responses to json for parsing to front end
```

## Installation
### It is recommended that this program is run in a python virtual enviroment
To set up a virtual enviroment for python:<br>

```
Ensure you have the python virtualenv package installed
Run the commands:
    virtualenv name-of-your-environment -p python3
    source name-of-your-environment/bin/activate
```
<br>
You can find a list of requirements in the requirements.txt file in the root of the repo.

Modules installed:
- requests-html: I chose this library as it was lightweight and renders javascript without which the data could not be scraped.

How to install modules:<br><br>
`pip install -r requirements.txt`

## MVP:
- Please write some code that scrapes: <br><br>
-- property name <br>
-- property type (e.g Apartment) <br>
-- number of bedrooms + bathrooms <br>
-- list of the amenities.

- from the following 3 urls: <br><br>
-- `https://www.airbnb.co.uk/rooms/33571268` <br>
-- `https://www.airbnb.co.uk/rooms/33090114` <br>
-- `https://www.airbnb.co.uk/rooms/40558945` <br>

## Extensions:
- To dockerize this and make it MUCH MORE easier for installing
- Typescript frontend for (hopefully) pretty display of data
- Store the returned information in MongoDB or Dynamo
- Host on AWS because cause that's fun!
- Set up TDD

## Problems encountered:
- Biggest problem was discovering which solution would be best, I spent a lot of time deciding if Selenium or Requests-HTML were more appropriate.
- Accessing the CSS selector on the live site which I could then save to a variable.
- Hosting using BeanStalk as it is only intended to serve one language at a time.

## Author Notes
- Keep as vanilla as possible
- Simple design for accessibility
- Intended to make a Parent class which I could then make instances of for different sites, eg. airbnb, expedia and tripadvisor but I got carried away writing the actual solution.

Resources:<br><br>
https://requests.readthedocs.io/projects/requests-html/en/latest/ <br>
https://www.w3schools.com/python/default.asp <br>
https://www.codecademy.com/courses/learn-web-scraping
