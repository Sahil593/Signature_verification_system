from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Assuming chromedriver is in your PATH

# Open the webpage where you want to fill the data
url = 'https://onlinefeestechnocrats.in/LoginStudent.aspx?type=F'  # Replace with the actual form page URL
driver.get(url)

test_data = [
    {'enrollment': '0191AL211139', 'password': '05092003'},
    {'enrollment': '0191AL211137', 'password': '30012003'}
]

# Wait for the form to load (optional, if necessary)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tr[@data-key]")))

# Define the function to fill the form fields based on the data key
def fill_form_with_data(test_data):
    try:
        for test in test_data:
            # Locate the input fields by their 'name' or 'id' attributes (modify based on the actual form's structure)
            
            enrl_field = driver.find_element(By.NAME, "Login1$UserName")  # Replace with actual field's name or id
            pswd_field = driver.find_element(By.NAME, "Login1$Password")  # Replace with actual field's name or id
            
            # Clear existing text if any
            enrl_field.clear()
            pswd_field.clear()

            # Input the data from book_data
            enrl_field.send_keys(test['enrollment'])
            pswd_field.send_keys(test['password'])

            #print(f"Filled form with ISBN: {book['ISBN']}, Title: {book['Title']}, Author: {book['Author']}")
            
            # Optionally submit the form (if required, remove this if the form doesn't need to be submitted each time)
            #submit_button = driver.find_element(By.XPATH, '//*[@id="Login1_LoginButton"]')  # Modify based on form's structure
            #submit_button.click()
            try:
                submit_button = driver.find_element(By.XPATH, '//*[@id="Login1_LoginButton"]')
                submit_button.click()
                if submit_button:
                    start_url = submit_button.get_attribute("href")
                    print(f"Navigating to next page: {start_url}")
                else:
                    print("No more pages to navigate.")
                    break
            except Exception as e:
                print("No 'next' link found, ending the loop.")
                break
            
            # Wait for the page to load and the total field to appear
            try:
                total = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_cPanel_ExportGridview_ctl02_lblTotal"]'))
                ).text
                print(f'Total: {total}')
            except Exception as e:
                print(f"Error finding total field: {e}")

            time.sleep(2)
            driver.get(url)
            # Add a short delay between page navigations (to prevent potential blocking)
            time.sleep(2)
            # Wait for the next page to load before continuing to the next book
            #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tr[@data-key]")))

    except Exception as e:
        print(f"Error filling form: {e}")

# Call the function to fill the form with your book data
fill_form_with_data(test_data)

# Optionally, close the browser after completing the task
driver.quit()


#//*[@id="UpdatePanel1"]/div[2]/div[1]/section/div[1]/div[2]