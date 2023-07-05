from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from auth_data import ok_email, ok_password
import pickle
import datetime

options = webdriver.ChromeOptions()


options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)


try:

    start_time = datetime.datetime.now()



    driver.get("https://www.avito.ru/all?q=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D1%8B")
    driver.implicitly_wait(5)
    for i in range(0, 3):
        items = driver. find_elements(By.XPATH, "//div[@data-marker='item-photo']")
        items[i].click()
        driver.implicitly_wait(5)

        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(5)

        username = driver.find_element(By.XPATH, "//div[@data-marker='seller-info/name']")
        print(f"User name: {username.text}")
        driver.implicitly_wait(5)

        driver.close()

        driver.switch_to.window(driver.window_handles[0])

    finish_time = datetime.datetime.now()
    spent_time = finish_time-start_time
    print(spent_time)





except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()