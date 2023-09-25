#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os
import datetime
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class testModule(unittest.TestCase):

    def setUp(self):
        # 옵션 생성
        chrome_options = webdriver.ChromeOptions()

        # headless 모드 설정
        # chrome_options.add_argument('headless')

        # 크롬 드라이버를 생성
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # 웹페이지 전체가 로드 될때까지 기다림
        self.driver.implicitly_wait(45) # 또는 self.driver.set_page_load_timeout(30)

    # 반복 되는 부분을 모듈화 한 함수
    def interact(self, by_type, name, wait_sec=1, click=True, send_keys_msg=None, error_msg=None):
        try:
            ele = self.driver.find_element(by=By.XPATH, value=name)
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")

            if send_keys_msg:
                ele.send_keys(send_keys_msg)

            if click:
                self.driver.execute_script("arguments[0].click();", ele)

            sleep(wait_sec)
        except Exception as e:
            print(error_msg)
            raise Exception(error_msg) from e