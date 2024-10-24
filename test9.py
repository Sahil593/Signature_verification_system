from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Assuming chromedriver is in your PATH

# Starting URL for book data extraction
start_url = 'https://eb.du.ac.in/web/book-details/index?page=7168'

# List to store the extracted data
book_data = []

def extract_book_data(start_url):
    global book_data
    try:
        driver.get(start_url)
        while True:  # Keep navigating until no more "next" link is found
            # Wait until the table rows are loaded (modify as needed)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr[@data-key]')))
            
            # Find all book rows
            books = driver.find_elements(By.XPATH, '//tr[@data-key]')
            
            # Extract data for each book
            for book in books:
                isbn = book.find_element(By.XPATH, ".//td[2]").text
                title = book.find_element(By.XPATH, ".//td[3]").text
                author = book.find_element(By.XPATH, ".//td[4]").text
                # Store in dictionary format
                book_data.append({
                    'ISBN': isbn,
                    'Title': title,
                    'Author': author
                })

            # Find the "next" button using the given XPath
            try:
                next_link = driver.find_element(By.XPATH, '//*[@id="w0"]/ul/li[12]/a')
                if next_link:
                    start_url = next_link.get_attribute("href")
                    print(f"Navigating to next page: {start_url}")
                    driver.get(start_url)
                else:
                    print("No more pages to navigate.")
                    break
            except Exception as e:
                print("No 'next' link found, ending the loop.")
                break

            # Add a short delay between page navigations (to prevent potential blocking)
            time.sleep(2)
    
    except Exception as e:
        print(f"Error extracting data: {e}")
    finally:
        # Close the browser
        driver.quit()

# Function to check if an element is present
def is_element_present(by, value):
    elements = driver.find_elements(by, value)
    return len(elements) > 0

# Function to get correct text for manufacturer field
def getCorrect(text):
    start_index = 50
    search_char = "'"

    # Slice the text from the starting index
    sliced_text = text[start_index:]

    # Find the character in the sliced text
    char_index_in_sliced = sliced_text.find(search_char)

    sliced_text2 = sliced_text[char_index_in_sliced+5:]

    char_index_in_sliced2 = sliced_text2.find(search_char)
    # Adjust the index to be relative to the original text
    st = start_index + char_index_in_sliced + 1
    end = start_index + char_index_in_sliced + char_index_in_sliced2 + 5

    return (text[st:end])  

# Define the function to fill the form fields based on the data key
def fill_form_with_data(book_data):
    try:
        start_url = 'https://sellercentral.amazon.in/abis/listing/create/product_identity?productType=ABIS_BOOK&recommendedBrowseNodeId=4149708031&displayPath=Books%2FHigher+Education+Textbooks%2FScience+%26+Mathematics#product_identity'
        driver.get(start_url)

        for book in book_data:
            # Locate the input fields by their 'name' or 'id' attributes (modify based on the actual form's structure)
            
            title_field = driver.find_element(By.NAME, "item_name-0-value")  # Replace with actual field's name or id
            isbn_field = driver.find_element(By.NAME, "externally_assigned_product_identifier-0-value")  # Replace with actual field's name or id
            
            # Clear existing text if any
            title_field.clear()
            isbn_field.clear()

            # Input the data from book_data
            title_field.send_keys(book['Title'])
            isbn_field.send_keys(book['ISBN'])
            
            dropdown = Select(driver.find_element(By.NAME, '//*[@id="katal-id-44"]'))  # Replace with the actual name or id of the dropdown
            dropdown.select_by_index(1)
            
            try:
                submit_button = driver.find_element(By.XPATH, '//*[@id="submit-button"]//button')
                submit_button.click()

                ok_button = driver.find_element(By.XPATH, '//*[@id="submitButtonErrorPopOverdefault"]/section[4]/kat-popover-hide/kat-button//button')
                ok_button.click()
                
            except Exception as e:
                print("Submit button or OK button not found, ending the loop.")
                break
            
            try:
                quantity_field = driver.find_element(By.XPATH, '//*[@id="katal-id-209"]')  # Replace with actual field's name or id
                price_field = driver.find_element(By.XPATH, '//*[@id="katal-id-213"]')  # Replace with actual field's name or id

                # Clear existing text if any
                quantity_field.clear()
                price_field.clear()

                # Input the data from book_data
                quantity_field.send_keys('3')
                price_field.send_keys('399')

                checkbox = driver.find_element(By.XPATH, '//*[@id="marathonUI"]/div/div[2]/kat-modal[1]/div[2]/span/kat-box[2]/kat-radiobutton/span')  # Replace with the actual attributes

                # Check if the checkbox is already selected
                if not checkbox.is_selected():
                    checkbox.click() 

                    return_to_form = driver.find_element(By.XPATH, '//*[@id="marathonUI"]/div/div[2]/kat-modal[1]/div[2]/span/kat-box[2]/div/kat-button//button')
                    return_to_form.click()

                product_details = driver.find_element(By.XPATH, '//*[@id="product_details-link"]')
                product_details.click()
                
                author_field = driver.find_element(By.XPATH, '//*[@id="katal-id-108"]')  # Replace with actual field's name or id

                # Clear existing text if any
                author_field.clear()

                # Input the data from book_data
                author_field.send_keys('Author')

                final_submit_button = driver.find_element(By.XPATH, '//*[@id="submit-button"]//button')
                final_submit_button.click()
                
                if is_element_present(By.XPATH, '//*[@id="attribute-group-manufacturer"]/section/div[1]/div/div[1]/div[1]/section[2]/div/div/div'):
                    error_text = driver.find_element(By.XPATH, '//*[@id="attribute-group-manufacturer"]/section/div[1]/div/div[1]/div[1]/section[2]/div/div/div')

                    correct_text = getCorrect(error_text)

                    manufacturer_field = driver.find_element(By.XPATH, '//*[@id="katal-id-49"]') 

                    # Clear existing text if any
                    manufacturer_field.clear()

                    # Input the data from book_data
                    manufacturer_field.send_keys(correct_text)

                final_submit_button = driver.find_element(By.XPATH, '//*[@id="submit-button"]//button')
                final_submit_button.click()

                try:
                    next_link = driver.find_element(By.XPATH, '//*[@id="katal_button_quick_copy"]//button/div[2]/slot/span')
                    if next_link:
                        start_url = next_link.get_attribute("href")
                        print(f"Navigating to next page: {start_url}")
                    else:
                        print("No more pages to navigate.")
                        break
                except Exception as e:
                    print("No 'next' link found, ending the loop.")
                    break

                # Add a short delay between page navigations (to prevent potential blocking)
                time.sleep(2)
            except Exception as e:
                print(f"Error finding total field: {e}")

            time.sleep(2)
            driver.get(start_url)
            # Add a short delay between page navigations (to prevent potential blocking)
            time.sleep(2)

    except Exception as e:
        print(f"Error filling form: {e}")

    finally:
        driver.quit()

# Run the data extraction
extract_book_data(start_url)

# Call the function to fill the form with your book data
fill_form_with_data(book_data)
