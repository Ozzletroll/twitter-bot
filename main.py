import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = os.environ["EMAIL"]
PASSWORD = "ElonMuskHasAFragileEgo"
USERNAME = "eelonn_musque"

# Selenium driver setup
service = Service("C:/Program Files (x86)/Google/Chrome/chromedriver.exe")
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)


# Twitter sign in
def twitter_login():
    driver.get("https://twitter.com/home")
    time.sleep(3)
    sign_in = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div["
                                            "2]/div/div/div/div[5]/label/div/div[2]/div/input")
    sign_in.click()
    sign_in.send_keys(EMAIL)
    sign_in.send_keys(Keys.ENTER)
    time.sleep(3)

    # password = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div["
    #                                          "2]/div[1]/div/div/div[3]/div/label/div/div[1]")
    # password.click()
    # password.send_keys(PASSWORD)
    # password.send_keys(Keys.ENTER)

    username_input = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div["
                                                   "2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div["
                                                   "2]/div/input")
    username_input.click()
    username_input.send_keys(USERNAME)
    username_input.send_keys(Keys.ENTER)
    time.sleep(3)

    password = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                             "2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    password.click()
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)
    time.sleep(4)


def tweet():
    input_field = driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
    input_field.click()
    input_field.send_keys("Crom, I have never prayed to you before. I have no tongue for it. No one, not even you, "
                          "will remember if we were good men or bad. Why we fought, or why we died. All that matters "
                          "is that two stood against many. That's what's important! Valor pleases you, Crom... so "
                          "grant me one request. Grant me revenge! And if you do not listen, then to HELL with you!")
    # input_field.send_keys(Keys.ENTER)


twitter_login()
tweet()
