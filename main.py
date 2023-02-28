from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=options)
# chrome_browser.maximize_window()
chrome_browser.get('https://phptravels.net/login')

assert 'Login - safa' in chrome_browser.title
assert 'Login - safa' in chrome_browser.body

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

