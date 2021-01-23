from models import scraper

scraper = scraper.Scraper

def main(scraper):
    airbnb_urls = [
                'https://www.airbnb.co.uk/rooms/33571268',
                'https://www.airbnb.co.uk/rooms/33090114',
                'https://www.airbnb.co.uk/rooms/40558945'
                ]
    
    scraper(airbnb_urls)
    
if __name__ == '__main__':
  main(scraper)