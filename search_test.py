from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_search():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # Login first
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Simulate "search" by checking item name
    item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert "Backpack" in item.text or item.text != ""
    print(f"✅ Found item: {item.text}")

    time.sleep(2)
    driver.quit()
