from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Form:

    def __init__(self, url="https://www.imdb.com/search/name/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Explicit wait
        self.wait = WebDriverWait(self.driver, 10)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait.until(ec.url_to_be(self.url))

    def quit(self):
        self.driver.quit()

    def findElementByID(self, id):
        return self.driver.find_element(by=By.ID, value=id)

    def findElementByLINK_TEXT(self, value):
        return self.driver.find_element(by=By.TAG_NAME, value=value)

    def fillForm(self):
        self.boot()
        self.wait.until(ec.presence_of_element_located((By.XPATH,
                                                        '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button/span'))).click()

        self.driver.execute_script("window.scrollBy(0, 500);")

        self.wait.until(ec.presence_of_element_located((By.NAME, 'name-text-input'))).send_keys("Vijay")

        self.wait.until(ec.presence_of_element_located((By.NAME, 'birth-date-start-input'))).click()


        self.wait.until(ec.presence_of_element_located((By.XPATH,
                                 '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button'))).click()



form = Form("https://www.imdb.com/search/name/")
form.fillForm()
form.quit()