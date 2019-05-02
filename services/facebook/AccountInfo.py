import sys

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from services.selenium.ElementsPuller import *
from services.facebook import *


class AccountInfo(ElementsPuller):
    def __init__(self, driver_location, delay):
        if driver_location == "":
            browser = webdriver.Chrome()
        else:
            browser = webdriver.Chrome(driver_location)

        super().__init__(browser)

        self.__delay = delay
        try:
            self._browser.get(facebook_link)
        except WebDriverException:
            self.log.FATAL("Link is unreachable:{}".format(facebook_link))
            raise ConnectionError("")

        self._browser.maximize_window()

    def signin(self, login, password):
        try:
            self.text(self.__delay, By.ID, email_box_id).send_keys(login)
            self.log.DEBUG("Login is set")

            self.text(self.__delay, By.ID, password_box_id).send_keys(password)
            self.log.DEBUG("Password is set")

            self.clickable(self.__delay, By.ID, login_button_id).click()
            self.log.DEBUG("Button is clicked")

            webdriver.ActionChains(self._browser).send_keys(Keys.ESCAPE).perform()
            self.log.INFO("Sign in - Success")
        except Exception as err:
            self.log.ERROR(str(err))

    def get_friends_dict(self):
        self.clickable(self.__delay, By.ID, profile_button_id).click()
        self.log.DEBUG("Click profile")

        self.clickable(self.__delay, By.CSS_SELECTOR, friends_selector).click()
        self.log.DEBUG("Click friends")

        self.log.DEBUG("Pulling friends info")
        friendsinfo = self.list(self.__delay, By.CSS_SELECTOR, every_friend_selector)

        friends = dict()

        if friendsinfo is not None:
            self.log.INFO("Information is collected - Success")
        else:
            self.finalize()

        for item in friendsinfo:
            friends[item.get_attribute('text')] = item.get_attribute('href')

        self.log.INFO("Names and links:")
        result = ""
        for key, value in friends.items():
            result += "\n\n{}\n{}".format(key, value)

        self.log.INFO(result)

    def finalize(self):
        self.log.INFO("Stopping browser")
        self._browser.quit()
