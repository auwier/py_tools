from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def check_and_play_sound():
     expected_text = "<expected_text>"
     xpath_expression = "<your_xpath>"

     element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH, xpath_expression))
     )

     print(element.text.strip())

     if element and element.text.strip() != expected_text:
         driver.execute_script("window.open('https://www.youtube.com/', '_blank');") # your sound for play
         clearInterval()

def clearInterval():
     global interval_id
     if interval_id:
         interval_id.cancel()

# Specify the path to your browser driver
driver_path = '<path_to_webdriver/chromedriver>' # replace with the path to your driver
driver = webdriver.Chrome(executable_path=driver_path)

# Replace the URL with the one you need
url = '<your_URL>'
driver.get(url)

# Interval in seconds
interval_seconds = 5

# Set the interval
interval_id = None
try:
     while True:
         check_and_play_sound()
         time.sleep(interval_seconds)
except KeyboardInterrupt:
     pass
finally:
     driver.quit()
