'''
Simple user login for react
'''
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from secrets import secret_user, secret_password

# easier to change path here 
PATH = 'D:\chromedriver.exe' #this is most likely not correct on your machine
driver = webdriver.Chrome(PATH)

# Set up Chrome WebDriver with DevTools enabled

#get_page = input("Please enter the webpage including the http(s): ")
get_page = 'your page'
driver.get(get_page)

# Find the login form elements
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

# the login_button will need a specific value found with inspecting the app
# this specific login uses a class name 'btn' 
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn')))

# Enter login credentials
username_field.send_keys(secret_user)
password_field.send_keys(secret_password)

# Submit the form
login_button.click()

# Wait for the page to load after login (customize the wait conditions as needed)
WebDriverWait(driver, 10).until(EC.title_contains('Dashboard'))

# Assert that the user is logged in by checking the resulting page or URL
assert 'dashboard' in driver.current_url.lower()

# Close the browser
driver.quit()
