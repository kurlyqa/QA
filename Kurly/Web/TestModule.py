#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from time import sleep
from selenium.webdriver.common.by import By

class testModule(unittest.TestCase):
     # 반복 되는 부분을 모듈화 한 함수
    def interact(self, by_type, name, wait_sec=2, click=True, send_keys_msg=None, error_msg=None):
        try:
            ele = self.driver.find_element(by=By.XPATH, value=name)
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
            if by_type == 'XPATH':
                if send_keys_msg:
                    ele.send_keys(send_keys_msg)
                if click:
                    self.driver.execute_script("arguments[0].click();", ele)
            elif by_type == 'NAME':
                if send_keys_msg:
                    ele.send_keys(send_keys_msg)
                if click:
                    self.driver.execute_script("arguments[0].click();", ele)
            sleep(wait_sec)
        except:
            print(error_msg)
            raise Exception(error_msg)