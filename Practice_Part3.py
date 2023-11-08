from Practice_Part1 import open_webpage
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    page_url = "https://testautomationpractice.blogspot.com/"
    driver = open_webpage(url=page_url)  # Obtain the driver instance


    ######################## JS Alerts #########################

    # Alert
    driver.find_element(By.XPATH, "//button[normalize-space()='Alert']").click()
    alert_box = driver.switch_to.alert
    time.sleep(2)
    alert_box.accept()

    # Confirm box
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Box']").click()
    confirm_box = driver.switch_to.alert
    time.sleep(2)

    # To dismiss
    confirm_box.dismiss()

    # To verify dismiss message
    dismiss_text = "You pressed Cancel!"

    if driver.find_element(By.XPATH, "//p[@id='demo']").text == dismiss_text:
        print("\nJS Alerts - dismiss window message is displayed correctly. ")
    else:
        print("\nJS Alerts - dismiss window message is displayed incorrectly. ")

    # Prompt box
    driver.find_element(By.XPATH, "//button[normalize-space()='Prompt']").click()
    prompt_box = driver.switch_to.alert

    user_name = "Kasia"
    prompt_box.send_keys(user_name)

    # To accept
    prompt_box.accept()

    # To verify accept message
    accept_text = f"Hello {user_name}! How are you today?"

    if driver.find_element(By.XPATH, "//p[@id='demo']").text == accept_text:
        print("JS Alerts - accept window message is displayed correctly. ")
    else:
        print("JS Alerts - accept window message is displayed incorrectly. ")


    ######################## Double Click #########################

    first_window = driver.find_element(By.ID, "field1")
    second_window = driver.find_element(By.ID, "field2")

    text_tocopy = "This text will be copied!"

    first_window.clear()
    first_window.send_keys(text_tocopy)

    copytext_button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
    act = ActionChains(driver)
    act.double_click(copytext_button).perform()

    # To retrieve the value of the second textbox
    second_window_value = second_window.get_attribute("value")

    if second_window_value == text_tocopy:
        print("\nDouble Click - double-click action performed correctly.")
    else:
        print("\nDouble Click - double-click action performed incorrectly.")

    time.sleep(3)

    ######################## Drag and Drop #########################

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    act = ActionChains(driver)
    act.drag_and_drop(source, target).perform()

    # To verify if correctly dropped

    if target.text == "Dropped!":
        print("\nDrag and Drop - was successful!")
    else:
        print("\nDrag and Drop - was unsuccessful!")


    ######################## Sliders #########################

    slider_movement = driver.find_element(By.XPATH, "//div[@id='slider']/span")
    slider_movement_value = slider_movement.get_attribute('style').split()
    slider_location = slider_movement.location

    print(f"\nSlider - initial movement of the slider: {slider_movement_value[1]}")
    print(f"Slider - initial location of the slider: {slider_location}")

    act = ActionChains(driver)
    act.drag_and_drop_by_offset(slider_movement, 250, 0).perform()
    time.sleep(2)
    act.drag_and_drop_by_offset(slider_movement, -117, 0).perform()

    slider_movement = driver.find_element(By.XPATH, "//div[@id='slider']/span")
    slider_movement_value = slider_movement.get_attribute('style').split()
    slider_location = slider_movement.location

    print(f"Slider - final movement of the slider: {slider_movement_value[1]}")
    print(f"Slider - final location of the slider: {slider_location}")


    ######################## Frames #########################

    frame = driver.find_element(By.ID, "frame-one796456169")
    driver.switch_to.frame(frame)  # Switching to inner frame

    name = "John"
    DOB = "11/27/1955"

    driver.find_element(By.NAME, "RESULT_TextField-0").send_keys(name)
    driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-1_0']").click()
    driver.find_element(By.NAME, "RESULT_TextField-2").send_keys(DOB)

    jobs = driver.find_elements(By.XPATH, "//select[@id='RESULT_RadioButton-3']/option")
    random_index = random.randint(0, len(jobs) - 1)  # choose profession randomly
    jobs[random_index].click()

    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    time.sleep(3)

    try:
        successful_title = driver.find_element(By.XPATH, "//h1[@class='success-title']").text

        if successful_title == 'Thank you!':
            print("\nFrames - submitting was successful")

    except:
        print("Frames - submitting was unsuccessful")

    time.sleep(3)
    driver.switch_to.default_content()


    ######################## Resizable #########################

    resizable = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
    resizable_initial = resizable.location

    act = ActionChains(driver)
    print(f"Resizable - initial location of the resizable: {resizable_initial}")
    act.click_and_hold(resizable).move_by_offset(300, -50).release().perform()
    time.sleep(2)
    act.click_and_hold(resizable).move_by_offset(-190, 200).release().perform()
    resizable_final = resizable.location
    print(f"Resizable - final location of the resizable: {resizable_final}")

    time.sleep(5)

