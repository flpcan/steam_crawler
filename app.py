from selenium import webdriver
import time


driver = webdriver.Firefox()

driver.get("https://steamcommunity.com/market/listings/730/Snakebite%20Case")

try:
    time.sleep(1)
    search_name = driver.find_element_by_id("largeiteminfo_item_name")
    search_price = driver.find_element_by_class_name('market_commodity_order_summary')
    outer_name = search_name.get_attribute("innerHTML")
    price_name = search_price.get_attribute("textContent")
    price = price_name.split()
    print(outer_name, price[-1])


finally:
    driver.quit()
