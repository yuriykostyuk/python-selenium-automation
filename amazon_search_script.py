import h1 as h1
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("/Users/yuriykostyuk/Desktop/git/jobeasy/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://www.amazon.com/gp/help/customer/display.html")

link = driver.find_element(By.ID, "helpsearch")
link.send_keys('Cancel order')
link.send_keys(Keys.RETURN)

text = driver.find_element(By.XPATH, '//*[@id="a-page"]/div[2]/div[2]/div[1]/div/div[2]/div/div/h1')

print(text.is_displayed())

driver.quit()