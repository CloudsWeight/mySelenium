'''
Inspecting network responses with Selenium

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
chr_dr_path = 'path/to/chromedriver'
# Set up Chrome WebDriver with DevTools enabled

service = Service(chr_dr_path)
capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(service=service, desired_capabilities=capabilities)

get_page = input("Please enter the webpage including the http(s): ")
# Open the web page
driver.get(get_page)

# Retrieve network logs
logs = driver.get_log('performance')

# Iterate through network logs
for log in logs:
    message = log['message']
    if 'Network.response' in message:
        response = log['message']['params']['response']
        url = response['url']
        headers = response['headers']
        
        # Process and analyze the headers 
        print(f"URL: {url}")
        print(f"Response Headers: {headers}")

