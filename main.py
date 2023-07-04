from selenium import webdriver
import time
from fake_useragent import UserAgent


#url = "https://999.md/ru/"

useragent = UserAgent()



#options

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
driver = webdriver.Chrome(options=options)


try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally: 
    driver.close()
    driver.quit()