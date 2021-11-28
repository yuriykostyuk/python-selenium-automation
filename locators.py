from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/yuriykostyuk/Desktop/git/jobeasy/python-selenium-automation/chromedriver")

# By ID
driver.find_element(By.ID, "continue")

#By XPATH
#driver.find_element(By.XPATH, "//*[@id="a-page"]/div[1]/div[1]/div/a/i")
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088' and @href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
driver.find_element(By.XPATH, "//input[@type='search']")