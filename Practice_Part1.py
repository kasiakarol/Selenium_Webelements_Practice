from selenium import webdriver
import time
import random
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

    ######################## Printing a page title #########################

    title = driver.find_element(By.XPATH, "//h1[@class='title']")
    print(f"Page title is: {title.text}\n")


    ######################## text boxes #########################

    name = "John Smith"
    email = "jsmith@test.com"
    phone = "6622545755"
    address = "Samoeng 653/53, 50250, Chiang Mai, Thailand"


    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "phone").send_keys(phone)
    driver.find_element(By.ID, "textarea").send_keys(address)

    # Radio buttons:
    driver.find_element(By.XPATH, "//input[@id='male']").click()


    ######################## checkboxes #########################

    # Collect the days within the week
    days_to_mark = ["Monday", "Thursday", "Sunday"]
    week_days_checkboxes = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox'] ")


    for day in week_days_checkboxes:
        if day.get_attribute("value").title() in days_to_mark:
            day.click()


    ######################## dropdowns #########################

    countries = driver.find_elements(By.XPATH, "//select[@id='country']/option")
    countries_list = []

    for country in countries:
        countries_list.append(country.text)

    # Choose a random country from the dropdown list
    random_country = random.randint(1, len(countries_list))
    driver.find_element(By.XPATH, f"//select[@id='country']/option[{random_country}]").click()


    ######################## dropdowns #########################

    colours_list = []
    colours = driver.find_elements(By.XPATH, "//select[@id='colors']/option")

    for colour in colours:
        colours_list.append(colour.text.lower())

    # Check if "green" is in the available options and select it if present
    if "green" in colours_list:
        for colour in colours:
            if colour.text.lower() == "green":
                colour.click()
    else:
        # Generate a random index to select a color in case "green" is not present
        random_index = random.randint(0, len(colours) - 1)
        colours[random_index].click()

    time.sleep(2)


    ######################## date picker #########################

    year_pick = "2025"
    month_pick = "January"
    day_pick = "2"

    driver.find_element(By.ID, "datepicker").click()

    # Choose a date
    while True:
        year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

        if month == month_pick and year == year_pick:
            break
        else:
            driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

    days = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']/a")

    for day in days:
        if day.text == day_pick:
            day.click()
            break

    driver.quit()
