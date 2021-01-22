# find-my-bunk
A web scraper written in Python and Typescript that displays information scraped from airbnb listings
Readmes are used as brain dumps until I complete the project and then I come back and make it shiny for other users.

Python backend for web scraper
Typescript frontend for (hopefully) pretty display of data
MongoDB... Dynamo maybe for data storage
Host on AWS cause that's fun!

Packages installed:
- Requests: 
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

TL;DR - Access a URL and pull out the data from that page

- BeautifulSoup 4:
Lets us parse the data and pick particular items from the return requests

MVP:
Please write some code that scrapes property name, property type (e.g Apartment), number of bedrooms, bathrooms and list of the amenities.

Extensons:
