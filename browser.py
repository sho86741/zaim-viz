# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Browser(object):
    def __init__(self, webdriver):
        self.driver = webdriver

    def __getattr__(self, name):
        if hasattr(self.driver, name):
            return getattr(self.driver, name)
        raise AttributeError

    def sync_send_keys(self, locator, key):
        # wait for element
        WebDriverWait(self, 120).until(
            EC.element_to_be_clickable(locator)
        )
        # send keys
        self.find_element(locator[0], locator[1]).send_keys(key)
        # wait for update
        WebDriverWait(self, 30).until(
            EC.text_to_be_present_in_element_value(locator, key)
        )

    def wait_element(self, id):
        return WebDriverWait(self, 10).until(EC.presence_of_element_located((By.ID, id)))
