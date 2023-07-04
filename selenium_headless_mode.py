from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from auth_data import ok_email, ok_password
import pickle

options = webdriver.ChromeOptions()


options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)


try:
    driver.get("https://vk.com/")
    time.sleep(5)

    email_input = driver.find_element(By.ID, "index_email")
    email_input.clear()
    email_input.send_keys("")
    time.sleep(5)
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("")
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)
    time.sleep(20)

    video_button = driver.find_element(By.ID, "l_vid").click()
    time.sleep(5)

    video_play = driver.find_element(By.CLASS_NAME, "VideoCard__controls video_item_controls").click()
    time.sleep(20)









except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()