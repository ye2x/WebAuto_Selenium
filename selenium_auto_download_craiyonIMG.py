from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.craiyon.com/')

time.sleep(1)
judul = driver.find_element(by=By.CSS_SELECTOR, value='#prompt')
judul.send_keys('sakura kid')
driver.find_element(by=By.CSS_SELECTOR, value='#generateButton').click()

WebDriverWait(driver, 90).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.grid.grid-cols-3.gap-1.sm\:gap-2 > div:nth-child(1)')))

image = driver.find_element(by=By.CSS_SELECTOR, value='.aspect-w-1.aspect-h-1').click()


time.sleep(2)


download = driver.find_element(by=By.CSS_SELECTOR, value='#actions_buttons > button:nth-child(2)').click()




time.sleep(10)

driver.quit()