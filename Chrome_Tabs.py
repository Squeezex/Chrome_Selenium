from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# List of URLs to open
urls = [
       
    # py your urls here
]

# Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Path to your Chrome WebDriver
driver_path = 'D:\chromedriver\chromedriver.exe' #You can download driver here 'https://googlechromelabs.github.io/chrome-for-testing/'

# ANSI escape codes for colors
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

# Create a Service object for the driver
service = Service(driver_path)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open each URL in a new tab
try:
    # Open the first URL in the main tab
    driver.get(urls[0])
    print(f"Opened {urls[0]}")
    time.sleep(0.5)  # Adjust as needed
    
    # Loop through the rest of the URLs
    for url in urls[1:]:
        # Open a new tab
        driver.execute_script("window.open('');")
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])
        # Load the next URL
        driver.get(url)
        print(f"Opened {url}")
        time.sleep(0.5)  # Adjust as needed

    # Debug messages in colored text
    print(GREEN + "All tabs are opened. Chrome will remain open." + RESET)
    input(BLUE + "Press Enter to close Chrome and end the script." + RESET) # press 'Enter' to close chrom tabs
    print(GREEN + "Chrome closed." + RESET)
except Exception as e:
    print(RED + f"An error occurred: {e}" + RESET)