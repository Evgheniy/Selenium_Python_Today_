from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent

#useragent = UserAgent()

#options = webdriver.ChromeOptions()
#options.add_argument(f"user-agent={useragent.random}")
driver = webdriver.Chrome()


try:
    driver.get("https://ok.ru/")
    time.sleep(5)

    email_input = driver.find_element(By.ID, "field_email")
    email_input.clear()
    email_input.send_keys("")
    time.sleep(5)

    password_input = driver.find_element(By.ID, "field_password")
    password_input.clear()
    password_input.send_keys("")
    time.sleep(10)
    password_input.send_keys(Keys.ENTER)





except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()