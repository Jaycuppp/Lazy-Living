import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Initial Setup
driver = webdriver.Chrome()
driver.get('https://weather.com/weather/today/l/c3c69cfc9248e306c9c54533c6b25eca5c36122f5ebebc50c48908877ccfcb97')


# Change to any amount of seconds
time.sleep(3600)

# Further Development 
