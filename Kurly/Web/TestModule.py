#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class testModule(unittest.TestCase):

    def setUp(self):
        # 사람처럼 보이게 하는 옵션들
        chrome_options = webdriver.ChromeOptions()
        # 가속(GPU) 사용 안함
        chrome_options.add_argument('disable-gpu')
        # 언어 설정
        chrome_options.add_argument('lang=ko_KR')
        # 크롬 드라이버 설치
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        # 웹페이지 전체가 로드 될때까지 기다림
        self.driver.implicitly_wait(30) # 또는 self.driver.set_page_load_timeout(30)

    # 반복 되는 부분을 모듈화 한 함수
    def interact(self, by_type, name, wait_sec=2, click=True, send_keys_msg=None, error_msg=None):
        try:
            ele = self.driver.find_element(by=By.XPATH, value=name)
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")

            if send_keys_msg:
                ele.send_keys(send_keys_msg)

            if click:
                self.driver.execute_script("arguments[0].click();", ele)

            sleep(wait_sec)
        except:
            print(error_msg)
            raise Exception(error_msg)