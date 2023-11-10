import scrapy
import json
from engine.items import EngineItem
from urllib.parse import urljoin

class SemanticScholor(scrapy.Spider):
    name = 'Scholar'
    start_urls = ['https://en.wikipedia.org']  # Base URL  https://response2you.com/search/search/

    '''def parse(self, response):
        
        # Extract URLs from the page
        #url= response.css('a::attr(href)').extract()
        #extracted_urls =urljoin('response.url','url')
        #extracted_urls=urljoin('response.url','extracted_urls1')
        extracted_urls = [urljoin(response.url, url) for url in response.css('a::attr(href)').extract()]
        for url in extracted_urls:
            yield {
                'url': url
                }
        with open('urls.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['URL'])  # Add a header row
            for url in extracted_urls:
                csvwriter.writerow([url])
            # Follow links to other pages (crawl)
        for next_page in response.css('a::attr(href)').extract():
            yield response.follow(next_page, self.parse)'''
    '''def parse(self, response):
        # Extract URLs from the page
        extracted_urls = [urljoin(response.url, url) for url in response.css('a::attr(href)').extract()]
        
        # Write URLs to a CSV file
        with open('urls.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['URL'])  # Add a header row
            for url in extracted_urls:
                csvwriter.writerow([url])  # Wrap url in a list to write it as a single value in a cell

        # Follow links to other pages (crawl)
        for next_page in response.css('a::attr(href)').extract():
            yield response.follow(next_page, self.parse)    ''' 
    def parse(self, response):
        # Extract URLs from the page
        extracted_urls = [urljoin(response.url, url) for url in response.css('a::attr(href)').extract()]

        # Create a list of dictionaries
        url_data = [{'url': url} for url in extracted_urls]

        # Write the data to a JSON file
        with open('urls.json', 'w') as jsonfile:
            json.dump(url_data, jsonfile)

        # Follow links to other pages (crawl)
        for next_page in response.css('a::attr(href)').extract():
            yield response.follow(next_page, self.parse)

