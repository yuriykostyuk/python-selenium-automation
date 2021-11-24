from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
<<<<<<< HEAD
driver = webdriver.Chrome(executable_path="/Users/yuriykostyuk/Desktop/git/jobeasy/python-selenium-automation/chromedriver")
=======
driver = webdriver.Chrome()
>>>>>>> 0180ad2ee428ba86c32cc0ca64ab53c1f991f44d
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
