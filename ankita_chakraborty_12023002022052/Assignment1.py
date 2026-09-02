from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ==========================================
# ASSIGNMENT 1: WEB ELEMENT IDENTIFICATION
# ==========================================

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

time.sleep(3)


# ==========================================
# 1. By.ID
# ==========================================

name_field = driver.find_element(By.ID, "name")

print("1. By.ID")
print("Name field found:", name_field.get_attribute("placeholder"))


# ==========================================
# 2. By.NAME
# ==========================================

print("\n2. By.NAME")

# Find all elements having a name attribute
name_elements = driver.find_elements(By.CSS_SELECTOR, "[name]")

print("Number of elements having name attribute:",
      len(name_elements))

for element in name_elements:
    print("Name attribute:",
          element.get_attribute("name"))


# Use the first element that has a name attribute
if len(name_elements) > 0:

    name_value = name_elements[0].get_attribute("name")

    name_element = driver.find_element(
        By.NAME,
        name_value
    )

    print("By.NAME - Element found:",
          name_value)

else:
    print("No element with NAME attribute found.")


# ==========================================
# 3. By.TAG_NAME
# ==========================================

heading = driver.find_element(By.TAG_NAME, "h1")

print("\n3. By.TAG_NAME")
print("Heading:", heading.text)


# ==========================================
# 4. By.LINK_TEXT
# ==========================================

home_link = driver.find_element(
    By.LINK_TEXT,
    "Home"
)

print("\n4. By.LINK_TEXT")
print("Link found:", home_link.text)


# ==========================================
# 5. By.CLASS_NAME
# ==========================================

class_element = driver.find_element(
    By.CLASS_NAME,
    "form-control"
)

print("\n5. By.CLASS_NAME")
print("Class:", class_element.get_attribute("class"))


# ==========================================
# Wait
# ==========================================

time.sleep(3)

driver.quit()
