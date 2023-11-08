from selenium import webdriver
import time
import random

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def open_webpage(url):
    driver_path = r"C:\DriversSel\chromedriver-win64\chromedriver.exe"
    service = Service(executable_path=driver_path)
    chrome_options = Options()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(url)
    return driver


if __name__ == "__main__":
    page_url = "https://testautomationpractice.blogspot.com/"
    driver = open_webpage(url=page_url)  # Obtain the driver instance

    ######################## links #########################

    link_card = driver.find_element(By.XPATH, "//a[normalize-space()='open cart']")
    link_card.send_keys(Keys.CONTROL + Keys.RETURN)  # opening link in a new tab
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])  # switching to a newly opened tab
    time.sleep(2)
    driver.close()  # Close a new tab
    driver.switch_to.window(driver.window_handles[0])  # switching back to the initial tab

    driver.find_element(By.XPATH, "//a[normalize-space()='orange HRM']").click()  # clicking another link
    time.sleep(2)
    driver.back()  # Go back to the initial page

    ######################## web tables #########################

    # collecting the headers
    headers = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")

    print("Web tables - headers of the table are:")
    for index, header in enumerate(headers):
        print(f"{index + 1}: {header.text} ")

    # Count number of columns:
    all_columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
    print(f"Web tables - the number of columns is: {len(all_columns)}")

    # Count number of rows
    all_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
    print(f"Web tables - the number of rows is: {len(all_rows)}")

    # Display all the books of author Amit
    print("\nWeb tables - all the books written by Mukesh are: ")
    for row in range(2, len(all_rows) + 1):
        author = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]//td[2]").text
        if author == "Amit":
            book = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]//td[1]").text
            print(f"{book}")

    # Display book name, author and price of all the books related to Java as a subject
    print("\nWeb tables - all the books related to Java subject are: ")
    for row in range(2, len(all_rows) + 1):
        subject = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[3]").text
        if subject.lower() == "java":
            book = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[1]").text
            author = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[2]").text
            price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[4]").text
            print(f"{book}, written by {author} for {price}$")

    ######################## pagination tables #########################

    # Count number of pages and number of all the rows in the table
    num_pages = len(driver.find_elements(By.XPATH, "//ul[@id='pagination']/li"))
    rows_count = 0

    for page in range(1, num_pages + 1):
        driver.find_element(By.XPATH, "//ul[@id='pagination']/li[" + str(page) + "]").click()
        rows_count += len(driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody//tr"))

    driver.find_element(By.XPATH, "//ul[@id='pagination']/li[1]").click()
    print(f"\nPagination tables - the total number of all the rows in the table are: {rows_count}")

    # Find the price of a specific product and select corresponding checkbox
    searched_name = "Product 13"
    num_pages = len(driver.find_elements(By.XPATH, "//ul[@id='pagination']/li"))

    for page in range(1, num_pages + 1):
        num_rows = len(driver.find_elements(By.XPATH, "//table[@id='productTable']//tr"))

        for row in range(1, num_rows + 1):
            try:
                name_element = driver.find_element(By.XPATH,
                                                   "//table[@id='productTable']/tbody/tr[" + str(row) + "]/td[2]")
                name = name_element.text

                if searched_name == name:
                    price_element = driver.find_element(By.XPATH,
                                                        "//table[@id='productTable']/tbody/tr[" + str(row) + "]/td[3]")
                    price = price_element.text
                    print(f"Pagination tables - the price of {searched_name} is {price}")
                    driver.find_element(By.XPATH,
                                        "//table[@id='productTable']/tbody/tr[" + str(row) + "]/td[4]//input").click()
                    break  # exit the loop once the product is found
            except NoSuchElementException:
                pass  # continue to the next row if the element is not found

        if page < num_pages:
            driver.find_element(By.XPATH, "//ul[@id='pagination']/li[" + str(page + 1) + "]/a").click()

    ######################## tabs #########################

    # Open multiple search tabs
    searched_phrase = "selenium"

    driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys(searched_phrase)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    result_list = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']/div/a")
    len(result_list)

    for link in range(1, len(result_list) + 1):
        driver.find_element(By.XPATH,
                            "//div[@id='Wikipedia1_wikipedia-search-results']/div[" + str(link) + "]/a").click()
        time.sleep(1)

    driver.switch_to.window(driver.window_handles[0])
