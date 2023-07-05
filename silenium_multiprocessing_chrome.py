from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from multiprocessing import Pool
from auth_data import ok_email, ok_password
import pickle
import datetime

options = webdriver.ChromeOptions()


options.add_argument("--disable-blink-features=AutomationControlled")

url_list = ["https://stackoverflow.com/", "https://www.instagram.com/", "https://vk.com/"]

def get_data(url):
    try:
        driver = webdriver.Chrome(options=options)

        driver.get(url=url)
        time.sleep(5)
        driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=3)
    p.map(get_data, url_list)



