import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Initial Setup
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(options=options)
driver.get('https://weather.com/weather/today/l/c3c69cfc9248e306c9c54533c6b25eca5c36122f5ebebc50c48908877ccfcb97')

# ZipCode = '91919'
# SearchBarID = 'LocationSearch_input'
# SearchBarXPath = '/html/body/div[1]/div[3]/div[1]/header/div/div[2]/div[1]/form/div/div[1]/fieldset/input'
# SearchButton = driver.find_element(By.XPATH, SearchBarXPath)
# SearchButton.send_keys(ZipCode)


# SearchResultXPath = '//*[@id="LocationSearch_listbox-d950cca6d9cd2c58c9d515af247df01aadbbc3ba158edcdc08d92eee71f1f27e"]'
# SearchResult = driver.find_element(By.XPATH, SearchResultXPath)
# SearchResult.click()

time.sleep(3600)
