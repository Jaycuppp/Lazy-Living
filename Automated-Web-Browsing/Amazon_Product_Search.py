import selenium, time, pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.EdgeOptions()
options.page_load_strategy = 'normal'

driver = webdriver.Edge(options=options)
driver.get('https://www.amazon.com/?tag=hymsabk-20&ref=pd_sl_290dlthsvm_e&adgrpid=1341404752168026&hvadid=83838074749799&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=80154&hvtargid=kwd-83838147155260:loc-190&hydadcr=28884_14580403')

Wait = WebDriverWait(driver, 0)
OriginalWindow = driver.current_window_handle
Actions = ActionChains(driver)


# Search_Button = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
# Search_Button = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located(By.ID, SearchBarID))

SearchBarID = 'twotabsearchtextbox'
Search_Button = driver.find_element(By.ID, SearchBarID)
Search_Button.send_keys('Computer Gaming Graphics Card')


# Search_Button_Click = driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
# Search_Button_Click = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located(By.ID, SearchButID))

SearchButID = 'nav-search-submit-button'
Search_Button_Click = driver.find_element(By.ID, SearchButID)
Search_Button_Click.click()

# time.sleep(1)

# driver.back() # Going Back to the Home Page
# time.sleep(1)

# driver.forward() # Going Forward to the Search Result Page
# time.sleep(1)

# driver.refresh() #Refreshing the Page
# time.sleep(1)

XPixels = 0
YPixels = 1000

Actions.scroll_by_amount(XPixels, YPixels).perform()

time.sleep(3600)
