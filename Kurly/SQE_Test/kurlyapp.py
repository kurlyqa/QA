from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import datetime, time, string, random
import HtmlTestRunner
import unittest

kurly_id = 'qatest01'
kurly_passwords = 'wldnsgks1@'

# appium 서버 http 주소

class Kurly_App_TestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '14'
        desired_caps['deviceName'] = 'emulator-5554'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def testcase_00000(self):
        driver = self.driver

    # 배경화면에 마켓컬리 앱 아이콘 존재 필요

        driver.find_element(By.XPATH, "//android.widget.TextView[@content-desc='컬리']").click()
        time.sleep(3)
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/mykurly').click()
        time.sleep(1)
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/titleView').click()
        time.sleep(1)
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/idEditView').send_keys(kurly_id)
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/passwordEditView').send_keys(kurly_passwords)
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/titleView').click()
        time.sleep(2)

        driver.back()

    def testcase_00052(self):
        driver = self.driver

        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/ivAddressIcon').click()
        time.sleep(1)
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/textViewAddAddress').click()
        time.sleep(4)
        driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys('한국타이어')
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        time.sleep(3)

        messages = driver.find_elements(By.CLASS_NAME, 'android.widget.Button')
        for i in messages:
            if '서울 강남구 테헤란로 133 (한국타이어빌딩)' in i.text:
                i.click()
                break

        time.sleep(1)

        # ID 자동 발급 및 입력
        _LENGTH = 3  # 5자리
        string_pool = string.digits  # 숫자

        # 랜덤한 문자열 생성
        da_id = "kurly"  # ID 앞자리 고정
        for i in range(_LENGTH):
            da_id += random.choice(string_pool)  # 랜덤한 문자열 하나 선택 (숫자만)
            break
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/restAddressView').send_keys(da_id)
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/titleView').click()
        #time.sleep(1)

        driver.save_screenshot('testcase_00052.png')

        # 토스트 팝업 체크
        A1 = driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/tvTitle').text
        value = '새 배송지가 추가되었습니다.'
        self.assertEqual(A1, value)
        print()
        print(A1)

        # 배송지 추가 체크
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/ivAddressIcon').click()
        time.sleep(1)

        # 토스트 팝업 체크
        A2 = driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/addressView').text
        value = '서울 강남구 테헤란로 133 (한국타이어빌딩) ' + da_id
        self.assertEqual(A2, value)
        print(A2)

        driver.back()

    def testcase_00063(self):
        driver = self.driver
        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/ivAddressIcon').click()
        time.sleep(1)

        toast1 = driver.find_elements(By.ID, 'com.dbs.kurly.m2.beta:id/deliveryPersonName')
        for i in toast1:
            if '봉봉팝' in i.text:
                i.click()
                break
        #time.sleep(0)

        # driver.save_screenshot('testcase_00063.png')

        A3 = driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/tvTitle').text

        #time.sleep(1)
        value = '배송지가 변경되었습니다.'
        self.assertEqual(A3, value, '값이 틀립니다.')
        print()
        print(A3)
        time.sleep(1)

    def testcase_00066(self):
        driver = self.driver

        driver.find_element(By.ID, 'com.dbs.kurly.m2.beta:id/mykurly').click()
        time.sleep(2)
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().index(21).instance("
                                                   "0))").click()



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/mk-jj-mac-050/PycharmProjects/SQE_unittest/appium_reports'))

    driver.back()