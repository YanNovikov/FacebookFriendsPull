from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from loger import *


class ElementsPuller:

    def __init__(self, browser):
        self.log = Logger()
        self._browser = browser

    def clickable(self, wait_time, by, condition):
        try:
            wait = WebDriverWait(self._browser, wait_time)
            return wait.until(expected_conditions.element_to_be_clickable((by, condition)))
        except TimeoutException:
            self.log.ERROR("Could not load clickable element [{}]".format(condition))
            return None

    def text(self, wait_time, by, condition):
        try:
            wait = WebDriverWait(self._browser, wait_time)
            return wait.until(expected_conditions.presence_of_element_located((by, condition)))
        except TimeoutException:
            self.log.ERROR("Could not load text element [{}]".format(condition))
            return None

    def list(self, wait_time, by, condition):
        try:
            wait = WebDriverWait(self._browser, wait_time)
            return wait.until(expected_conditions.presence_of_all_elements_located((by, condition)))
        except TimeoutException:
            self.log.ERROR("Could not load list element [{}]".format(condition))
            return None