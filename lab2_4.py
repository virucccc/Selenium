# -*- coding: utf-8 -*-
import unittest
import urllib.request
import webbrowser
from time import sleep

from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class testik(unittest.TestCase):
    def test_one(self):
        d = webdriver.Chrome('C:\\Users\\Noob\\Desktop\\chromedriver.exe')
        d.get("https://www.artlebedev.ru/case/")
        txt = "HELLO woRlD!@%$"
        ta1 = d.find_element_by_id("source").send_keys(txt)
        sleep(1)
        ta2 = d.find_element_by_id("target").get_attribute("value")
        sleep(1)
        if ta2.isupper:
            print(ta2 + " is ok")
        else:
            print(ta2 + " is bad")
        sleep(5)
#
#
# if __name__ == "__main__":
#     unittest.main()
