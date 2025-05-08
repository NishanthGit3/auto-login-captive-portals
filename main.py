import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from configparser import ConfigParser 

service = webdriver.FirefoxService()
options = webdriver.FirefoxOptions()

# headless mode
options.add_argument("-headless")

driver = webdriver.Firefox(service=service, options=options)

# read config file
configur = ConfigParser()
configur.read('config.ini')

link = str(configur.get('configuration', 'login_page_link'))
login_username = str(configur.get('configuration', 'username'))
login_passwd = str(configur.get('configuration', 'password'))

driver.get(link)

time.sleep(1)

# switching to login frame
frame = driver.find_element(By.NAME, "login_win")

driver.switch_to.frame(frame)

# enters username
driver.find_element(By.ID, "usrname").send_keys(login_username)

# enters password
driver.find_element(By.ID, "newpasswd").send_keys(login_passwd)

# enables terms and conditions if any
driver.find_element(By.ID, "terms").click()

# clicks login button
driver.find_element(By.ID, "update_btn").click()

time.sleep(1)

driver.quit()

print("Logged in successfully")