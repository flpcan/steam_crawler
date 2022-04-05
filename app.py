from selenium import webdriver
from writer import write
import csv
import time



driver = webdriver.Firefox()
f = open("links.csv")
csv_reader = csv.reader(f)
chars = "['']"
for line in csv_reader:
    url = str(line).strip(chars)

    driver.get(url)

    try:
        #Add more sleep and wont block the requests
        
        time.sleep(1)
        search_name = driver.find_element_by_id("largeiteminfo_item_name")
        search_price = driver.find_element_by_class_name('market_commodity_order_summary')
        outer_name = search_name.get_attribute("innerHTML")
        price_name = search_price.get_attribute("textContent")
        price = price_name.split()

        item_name = outer_name
        item_price = price[5]

        write(item_name,item_price)


    finally:
        print("ok")
