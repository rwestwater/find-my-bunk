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
You can find a list of requirements in the requirements.txt file in the root of the repo.

Modules installed:
- requests-html: I chose this library as it was lightweight and renders javascript without which the data could not be scraped.

How to install modules:
`pip install -r requirements.txt`
`pip install requests-html`

## MVP:
- Please write some code that scrapes: 
-- property name
-- property type (e.g Apartment) 
-- number of bedrooms + bathrooms
-- list of the amenities.

- from the following 3 urls:
-- `https://www.airbnb.co.uk/rooms/33571268`
-- `https://www.airbnb.co.uk/rooms/33090114`
-- `https://www.airbnb.co.uk/rooms/40558945`

## Extensions:
- To dockerize this and make it MUCH MORE easier for installing
- Typescript frontend for (hopefully) pretty display of data
- Store the returned information in MongoDB or Dynamo
- Host on AWS because cause that's fun!

Resources:
https://requests.readthedocs.io/projects/requests-html/en/latest/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://www.codecademy.com/courses/learn-web-scraping