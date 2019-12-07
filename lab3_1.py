# -*- coding: utf-8 -*-
import unittest
import urllib.request
import webbrowser
from time import sleep
import re
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class testik(unittest.TestCase):

    def test_one(self):
        d = webdriver.Chrome('C:\\Users\\Noob\\Desktop\\chromedriver.exe')
        d.get("http://www.google.com")
        str = "Hello"
        str2 = "World"
        d.find_element_by_css_selector(".gLFyf.gsfi").send_keys(str)
        d.find_element_by_css_selector(".gLFyf.gsfi").send_keys(Keys.RETURN)
        # d.find_element_by_css_selector('input.gNO89b').click()
        sleep(5)
        d.find_element_by_css_selector(".gLFyf.gsfi").clear()
        d.find_element_by_css_selector(".gLFyf.gsfi").send_keys(str2)
        d.find_element_by_css_selector('.Tg7LZd').click()
        sleep(5)
        d.find_element_by_css_selector(".gLFyf.gsfi").clear()
        d.find_element_by_css_selector(".gLFyf.gsfi").send_keys(str + str2)
        d.find_element_by_css_selector('.Tg7LZd').click()
        sleep(5)
        elems = d.find_elements_by_partial_link_text("https")
        input_raw = ""
        for i in range(0, len(elems)):
            input_raw = input_raw + elems[i].text
            links = get_links(input_raw)
        for i in links:
            if i.find('helloworld') != -1:
                print(i + " существует")
        sleep(5)


def get_links(chat_string):
    pattern = '(?:http[s]?:\/\/).(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?'
    return re.findall(pattern, chat_string)
#
#
# if __name__ == "__main__":
#     unittest.main()
