from selenium import webdriver  # To control the browser
from selenium.webdriver.common.by import By  # To locate elements on the page
import time

driver = webdriver.Chrome()  # Assuming chromedriver is in your PATH

# Starting URL
start_url = 'https://eb.du.ac.in/web/book-details/index?page=7165'
driver.get(start_url)

def extract_book_data():
    try:

        books = driver.find_elements(By.XPATH, "//tr[@data-key]")

        for book in books:
            isbn = book.find_element(By.XPATH, ".//td[2]").text
            title = book.find_element(By.XPATH, ".//td[3]").text
            author = book.find_element(By.XPATH, ".//td[4]").text
            print(f'ISBN: {isbn}, Title: {title}, Author: {author}')
        '''button = driver.find_element(By.XPATH, '//*[@id="w0"]/ul/li[12]/a')
        button.click()
        print("Button clicked successfully.")
        time.sleep(60)'''

    except Exception as e:
        print(f"Error extracting data: {e}")

extract_book_data()

# Close the browser
driver.quit()


'''/html/body/main/div/div/div/ul/li[12]/a
//*[@id="w0"]/ul/li[12]/a
//*[@id="w0"]/table/tbody/tr[19]/td[3]
<a href="/web/book-details/index?page=7167" data-page="7166">»</a>'''