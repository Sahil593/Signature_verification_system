from selenium import webdriver  # To control the browser
from selenium.webdriver.common.by import By  # To locate elements on the page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Assuming chromedriver is in your PATH

# Starting URL
start_url = 'https://eb.du.ac.in/web/book-details/index?page=7165'

# List to store the extracted data
book_data = []

def extract_book_data(start_url):
    try:
        while True:  # Keep navigating until no more "next" link is found
            driver.get(start_url)
            
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

# Run the data extraction
extract_book_data(start_url)

# Loop through each book in the list
for book in book_data:
    isbn = book['ISBN']
    title = book['Title']
    author = book['Author']
    
    # Print or perform operations on the book details
    print(f"ISBN : {isbn}, Title : {title}, Author : {author}")
