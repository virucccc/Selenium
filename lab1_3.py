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
        f = open('sites.txt', 'r')
        l = []
        print("Файл содержит: ")
        for line in f:
            l.append(line.replace("\n", ""))
            print(line.replace("\n", ""))
        l.sort(key=len)
        s = "window.open('"
        e = "');"
        n = 10
        m = 2
        tabs = [[0] * m for i in range(n)]
        g = 0
        print("Открываем по длине ссылки: ")
        for line in l:
            print(line)
            n = s + line + e
            d.execute_script(n)
            tabs[g][0] = line
            t = d.window_handles
            d.switch_to.window(t[len(t) - 1])
            tabs[g][1] = d.current_window_handle
            g = g + 1
        tabs.sort()
        print("Закрываем в алфавитном порядке")
        for x in range(0, 10):
            d.switch_to.window(tabs[x][1])
            d.close()
            sleep(1)

#
#
# if __name__ == "__main__":
#     unittest.main()
