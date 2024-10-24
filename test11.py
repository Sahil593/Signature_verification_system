from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# URL to sign-in page
signIn_url = 'https://sellercentral.amazon.in/'
driver.get(signIn_url)


def is_element_present(by, value):
    elements = driver.find_elements(by, value)
    return len(elements) > 0


def signIn():
    try:
        # Locate and click the login button
        print("Trying to find login button...")
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="SC_welcome_nav_login"]/div/a/strong'))
        )
        print("Login button found, clicking...")
        login_button.click()
        
        # Wait for the email field to be present
        print("Waiting for email field...")
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        print("Email field found, entering email...")
        email_field.clear()
        email_field.send_keys('shresthbabeley575@gmail.com')
        
        # Click the continue button
        print("Trying to find continue button...")
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))
        )
        print("Continue button found, clicking...")
        continue_button.click()
        
        pswd = input("Enter your password: ")
        # Wait for the password field to be present
        print("Waiting for password field...")
        pswd_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        print("Password field found, entering password...")
        pswd_field.clear()
        time.sleep(15)
        pswd_field.send_keys(pswd)
        time.sleep(15)
        
        # Click the sign-in button
        print("Trying to find sign-in button...")
        sign_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="signInSubmit"]'))
        )
        print("Sign-in button found, clicking...")
        sign_button.click()
        
        # Manual wait for user to input OTP from terminal
        otp = input("Enter your OTP: ")

        otp_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="auth-mfa-otpcode"]'))  # Update this line based on your actual field's attribute
        )
        otp_field.clear()
        time.sleep(15)
        otp_field.send_keys(otp)
        time.sleep(15)
        # Click the submit button for OTP
        print("Trying to find OTP submit button...")
        submit_otp_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-signin-button"]'))  # Update this line based on the actual button's attribute
        )
        print("OTP submit button found, clicking...")
        submit_otp_button.click()
        
        if is_element_present(By.XPATH, '//*[@id="picker-container"]/div/div[3]/div/button'):
            select_account_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="picker-container"]/div/div[3]/div/button'))  # Update this line based on the actual button's attribute
            )
            print("Account Selecting...")
            select_account_button.click()
        
        print("Trying to find add product button...")
        add_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="favorite-pages-links-list"]/a'))
        )
        print("Add product button found, clicking...")
        add_product.click()

        print("Trying to find add product ID button...")
        product_id = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/kat-box[3]'))
        )
        print("Add product ID found, clicking...")
        product_id.click()






        '''# Step 1: Find the Shadow Host
        shadow_host = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'shadow-host-selector'))  # Replace 'shadow-host-selector' with the actual selector for the shadow host
        )

        # Step 2: Use JavaScript to get the Shadow Root (open Shadow DOM)
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

        # Step 3: Find the element inside the Shadow DOM (using the shadow root)
        product_id_field = shadow_root.find_element(By.CSS_SELECTOR, '#katal-id-1')  # Replace with the actual CSS selector

        # Step 4: Interact with the element
        product_id_field.clear()
        product_id_field.send_keys('9781315014364')'''

        
        print("Step 1: Find the Shadow Host (the <kat-textarea> element)")
        shadow_host = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'kat-textarea[data-testid="product-ids-input"]'))
        )

        print("Step 2: Use JavaScript to access the Shadow Root (inside the shadow host)")
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

        print("Step 3: Find the <textarea> inside the Shadow DOM")
        textarea_element = shadow_root.find_element(By.CSS_SELECTOR, 'textarea#katal-id-1')

        print("Step 4: Interact with the <textarea> (send product IDs)")
        textarea_element.clear()  # Clear any existing text
        textarea_element.send_keys('9781315014364')  # Send the product ID

        print("Trying to find submit button...")
        # Step 5: Check if the button is in another shadow DOM
        shadow_host = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'kat-button[data-testid="omnibox-submit-button"]'))
        )

        print('2')
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

        print('3')
        submit_button = shadow_root.find_element(By.CSS_SELECTOR, 'button')

        print('4')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(submit_button)).click()
        




        '''

        print('Step 1: Find the Shadow Host (the <kat-textarea> element inside <kat-box>)')
        kat_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'kat-box'))
        )

        print('Step 2: Access the Shadow Root of <kat-box> (if needed, skip if not a shadow host)')
        kat_box_shadow_root = driver.execute_script('return arguments[0].shadowRoot', kat_box)

        print('Step 3: Find the Shadow Host (the <kat-textarea> element inside <kat-box>)')
        kat_textarea = kat_box_shadow_root.find_element(By.CSS_SELECTOR, 'kat-textarea[data-testid="product-ids-input"]')

        print('Step 4: Access the Shadow Root of the <kat-textarea>')
        textarea_shadow_root = driver.execute_script('return arguments[0].shadowRoot', kat_textarea)

        print('Step 5: Interact with the <textarea> inside the Shadow DOM')
        textarea_element = textarea_shadow_root.find_element(By.CSS_SELECTOR, 'textarea#katal-id-1')
        textarea_element.clear()  # Clear any existing text
        textarea_element.send_keys('9781315014364')  # Send the product ID
        
        print('Step 6: Find the <kat-button> inside the same shadow DOM as the <kat-textarea>')
        kat_button = kat_box_shadow_root.find_element(By.CSS_SELECTOR, 'kat-button[data-testid="omnibox-submit-button"]')
        
        print('Step 7: Find the actual <button> element inside <kat-button> and click it')
        submit_button = kat_button.find_element(By.CSS_SELECTOR, 'button')  # Locate the actual button inside kat-button
        
        # Ensure the button is clickable before clicking
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button)).click()

        '''



        # Click the create new listing button for OTP
        print("Trying to create new listing button...")
        create_new_listing = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="create-listing-link"]'))  # Update this line based on the actual button's attribute
        )
        print("create new listing button found, clicking...")
        create_new_listing.click()

        print('done....')
        if create_new_listing:
            start_url = create_new_listing.get_attribute("href")
            print(f"Navigating to create listing page: {start_url}")
        else:
            print("Failed to navigate to create listing page.")

        driver.get(start_url)


        print("Trying find recommended checkbox...") 
        recommended_checkbox = driver.find_element(By.XPATH, '//*[@id="marathonUI"]/div/div[2]/div/div[1]/div[2]/div[2]/kat-radiobutton[2]/span')  # Replace with the actual attributes

        # Check if the checkbox is already selected
        if not recommended_checkbox.is_selected():
            recommended_checkbox.click()
            print("recommended checkbox found, clicking...")
        
        print("Trying find required checkbox...") 
        required_checkbox = driver.find_element((By.ID, 'katal-id-1'))  # Replace with the actual attributes

        # Check if the checkbox is already selected
        if not required_checkbox.is_selected():
            required_checkbox.click()
            print("required checkbox found, clicking...")

        print("Waiting for item name field...")
        item_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'katal-id-0'))
        )
        print("item name field found, entering...")
        item_name_field.clear()
        item_name_field.send_keys('A History of British Socialism')
        time.sleep(10)

        print("Trying to find confirm button...")
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="default-section"]/div[2]/div/div[3]/div/div[2]/div/div/div[2]/kat-button//button'))  # Update this line based on the actual button's attribute
        )
        print("confirm button found, clicking...")
        confirm_button.click()
        time.sleep(10)

        print("Waiting for isbn field...")
        isbn_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'katal-id-37'))
        )
        print("Isbn field found, entering...")
        isbn_field.clear()
        isbn_field.send_keys('9781315014364')
        time.sleep(10)

        print("Select ISBN from dropdown menu...")
        dropdown = Select(driver.find_element(By.ID, 'katal-id-9'))  # Replace with the actual name or id of the dropdown
        dropdown.select_by_index(1)

        print("Trying to find next button...")
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="next-button"]//button'))  # Update this line based on the actual button's attribute
        )
        print("next button found, clicking...")
        next_button.click()
        time.sleep(30)

        print("Trying to find ok button...")
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButtonErrorPopOverdefault"]/section[4]/kat-popover-hide/kat-button//button'))  # Update this line based on the actual button's attribute
        )
        print("Ok button found, clicking...")
        ok_button.click()
        time.sleep(30)

    except Exception as e:
        print(f"Error filling form: {e}")
    finally:
        time.sleep(5)  # Optional: adjust sleep time based on your needs
        driver.quit()

# Call the sign-in function
signIn()
