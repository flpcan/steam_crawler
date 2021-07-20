from selenium import webdriver

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")


try:
    search = driver.find_element_by_class_name("menu-toggle")
    outer = search.get_attribute("innerHTML")
    print(outer)
finally:
    driver.quit()



# <span class="market_commodity_orders_header_promote">$1.69</span>
