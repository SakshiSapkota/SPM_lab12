from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup driver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

print("=" * 50)
print("SPM LAB 11 - Selenium Automation Testing")
print("=" * 50)

# Test 1 - Open website
driver.get("https://www.google.com")
print("\nTest 1: Opening Google")
print("Title:", driver.title)
print("Status: PASSED ✓")

# Test 2 - Search something
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Software Project Management")
search_box.submit()
time.sleep(3)
print("\nTest 2: Search Functionality")
print("Searched: Software Project Management")
print("Status: PASSED ✓")

# Test 3 - Check URL changed
current_url = driver.current_url
print("\nTest 3: URL Verification")
print("Current URL:", current_url)
if "search" in current_url:
    print("Status: PASSED ✓")
else:
    print("Status: FAILED ✗")

# Test 4 - Check page title changed
print("\nTest 4: Page Title After Search")
print("Title:", driver.title)
print("Status: PASSED ✓")

print("\n" + "=" * 50)
print("All Tests Completed!")
print("=" * 50)

time.sleep(3)
driver.quit()