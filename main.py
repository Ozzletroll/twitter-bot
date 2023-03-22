import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:

    def __init__(self):
        self.EMAIL = os.environ["EMAIL"]
        self.PASSWORD = "ElonMuskHasAFragileEgo"
        self.USERNAME = "eelonn_musque"

        # Selenium driver setup
        self.service = Service("C:/Program Files (x86)/Google/Chrome/chromedriver.exe")
        self.options = ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def speed_test(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        popup = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        popup.click()
        time.sleep(1)
        go = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div["
                                                "1]/a/span[4]")
        go.click()
        time.sleep(60)
        popup_2 = self.driver.find_element(By.CSS_SELECTOR, "#container > div > div.main-content > div > div > div > "
                                                            "div.pure-u-custom-speedtest > "
                                                            "div.speedtest-container.main-row > div.main-view > div > "
                                                            "div.desktop-app-prompt-modal > div > a")
        popup_2.click()
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        return download_speed.text, upload_speed.text

    def twitter_login(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        sign_in = self.driver.find_element(By.XPATH,
                                           "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div["
                                           "2]/div/div/div/div[5]/label/div/div[2]/div/input")
        sign_in.click()
        sign_in.send_keys(self.EMAIL)
        sign_in.send_keys(Keys.ENTER)
        time.sleep(3)

        # password = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div["
        #                                          "2]/div[1]/div/div/div[3]/div/label/div/div[1]")
        # password.click()
        # password.send_keys(PASSWORD)
        # password.send_keys(Keys.ENTER)

        username_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div["
                                                            "2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div["
                                                            "2]/div/input")
        username_input.click()
        username_input.send_keys(self.USERNAME)
        username_input.send_keys(Keys.ENTER)
        time.sleep(3)

        password = self.driver.find_element(By.XPATH,
                                            "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                            "2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.click()
        password.send_keys(self.PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(4)

    def tweet(self, speed_list):
        input_field = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        input_field.click()
        input_field.send_keys(f"Twitter is stupid. My download speed is: {speed_list[0]} Mbps,"
                              f" and my upload speed is {speed_list[1]} Mbps. ")
        # input_field.send_keys(Keys.ENTER)


twitter_bot = InternetSpeedTwitterBot()
speeds = twitter_bot.speed_test()
twitter_bot.twitter_login()
twitter_bot.tweet(speeds)
