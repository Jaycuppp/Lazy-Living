# Importing the required Libraries to run the automated task
from selenium import *
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#Initial Setup
driver = webdriver.Chrome()
driver.get('https://www.amazon.com/?tag=amazusnavi-20&hvadid=381823327672&hvpos=&hvnetw=g&hvrand=15369903253882284441&hvpone=&hvptwo=&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9031162&hvtargid=kwd-10573980&ref=pd_sl_7j18redljs_e&hydadcr=28883_11845445&gclid=CjwKCAjwmJeYBhAwEiwAXlg0ATpf1Z-JL2kpyEl7yRZRhGWjvKzG3tVkde1CAQCiNZ9JaYRHyJXjjRoCf5wQAvD_BwE')


Search_Button = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
# Change the string to any product you want to automatically search
Search_Button.send_keys('Graphics Card')

# Clicking the Search Button
Search_Button_Click = driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
Search_Button_Click.click()

# Extra safety measure for how long you want the script to be running in seconds
time.sleep(3600)
