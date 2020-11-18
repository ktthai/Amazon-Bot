from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
import os

chromedriver_loc = "chromedriver"

print("Starting up...")

chromedriver = chromedriver_loc #<------- Edit your path to where chromedriver is located
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome("/Users/kenny/Desktop/Amazon-bot/chromedriver")

driver.get("https://www.amazon.com/")
headlines = driver.find_elements_by_class_name("story-heading")
for headline in headlines:
    print(headline.text.strip())