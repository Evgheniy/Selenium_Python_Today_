from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from auth_data import ok_email, ok_password
import pickle




driver = webdriver.Chrome()


try:
    '''
    driver.get("https://ok.ru/")
    time.sleep(5)

    email_input = driver.find_element(By.ID, "field_email")
    email_input.clear()
    email_input.send_keys(ok_email)
    time.sleep(5)

    password_input = driver.find_element(By.ID, "field_password")
    password_input.clear()
    password_input.send_keys(ok_password)
    time.sleep(10)
    password_input.send_keys(Keys.ENTER)

    #coockies
    pickle.dump(driver.get_cookies(), open(f"{ok_email}_cookies", "wb"))
    '''

    driver.get("https://ok.ru/")
    time.sleep(5)

    for cookie in pickle.load(open(f"{ok_email}_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()