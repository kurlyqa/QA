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
        # 옵션 생성
        chrome_options = webdriver.ChromeOptions()

        # headless 모드 설정
        chrome_options.add_argument('headless')

        # 크롬 드라이버를 생성
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # 웹페이지 전체가 로드 될때까지 기다림
        self.driver.implicitly_wait(100) # 또는 self.driver.set_page_load_timeout(30)
        # # 옵션 생성
        # chrome_options = webdriver.ChromeOptions()
        #
        # # headless 모드 설정
        # chrome_options.add_argument('headless')
        #
        # # 크롬 위치 명시
        # chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        # chrome_driver_binary = "/usr/local/bin/chromedriver"
        #
        # # 크롬 드라이버 설치
        # chrome_driver_service = Service(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path=chrome_driver_binary, options=chrome_options, service=chrome_driver_service)
        #
        # # 웹페이지 전체가 로드 될때까지 기다림
        # self.driver.implicitly_wait(100) # 또는 self.driver.set_page_load_timeout(30)

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
        except:
            print(error_msg)
            raise Exception(error_msg)
    #     except Exception as e:
    #         print(error_msg)
    #         # 스크린샷 저장
    #         self.save_screenshot_with_timestamp("errors", "screenshot.png")
    #         raise Exception(error_msg) from e
    #
    # def save_screenshot_with_timestamp(self, folder, filename):
    #     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #     folder_path = os.path.join(os.getcwd(), folder, timestamp)
    #     os.makedirs(folder_path, exist_ok=True)
    #     screenshot_path = os.path.join(folder_path, filename)
    #     self.driver.save_screenshot(screenshot_path)