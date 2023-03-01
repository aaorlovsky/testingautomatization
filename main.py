from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=options)
# chrome_browser.maximize_window()
chrome_browser.get('https://phptravels.net/login')

assert 'Login - safa' in chrome_browser.title

assert 'email' in chrome_browser.page_source
user_email = chrome_browser.find_element(By.NAME, 'email')
user_email.clear()
user_email.send_keys('test@test.com')

assert 'password' in chrome_browser.page_source
user_pass = chrome_browser.find_element(By.NAME, 'password')
user_pass.clear()
user_pass.send_keys('123')
# print(buttons.get_attribute('innerHTML'))

login_button = chrome_browser.find_element(By.XPATH, "//form/div/button")
login_button.click()

assert 'Wrong ' in chrome_browser.page_source



# chrome_browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=options)
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

