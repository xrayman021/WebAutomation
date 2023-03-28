from selenium import webdriver
import time

firefox_driver_path = "/Users/boomb/Downloads/geckodriver-v0.32.2-win32"

driver = webdriver.Firefox(firefox_driver_path)

demo_website = "file://Users/boomb/Downloads/01 Source Files/01 Source Files/01 demo-website.html"

driver.get(demo_website)

driver.maximize_window()

time.sleep(5)

#driver.close()