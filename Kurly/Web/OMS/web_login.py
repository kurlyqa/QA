import unittest
import re
import schedule
from TestModule import testModule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class WebLogin(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_01_OMS_로그인(self):
        try:
            # 1. <로그인>

            # OMS url 주소
            oms_url = 'https://soms.stg.kurlycorp.kr/login'

            # url 이동
            self.driver.get(oms_url)

            # 브라우저 최대화
            self.driver.maximize_window()

            # 로그인 페이지 진입
            # 아이디(qa_om_auto@kurlycorp.com) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[1]//input", click=False, send_keys_msg='qa_om_auto@kurlycorp.com', error_msg="아이디 입력란 미노출")

            # 비밀번호(kurly12!) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[2]//input", click=False, send_keys_msg='kurly12!', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--is-elevated v-btn--has-bg theme--dark v-size--x-large')]", error_msg="로그인 버튼 미노출")



            # 2. <로그아웃>

            # 우측상단 로그아웃 UI선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-avatar')]", error_msg="로그아웃 UI 버튼 미노출")

            # 로그아웃 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '로그아웃')]", error_msg="로그아웃 버튼 미노출")

            # 초기화면(로그인페이지)으로 이동 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--is-elevated v-btn--has-bg theme--dark v-size--x-large')]", click=False, error_msg="로그인 버튼 미노출")

            # 탭 닫기
            self.driver.close()
        except:
            self.assertEqual(0, 1)
        else:
            print("Passed")

    def tearDown(self):
        # 브라우저 세션 닫기
        self.driver.quit()

## 이 클래스에서 정의된 테스트 메소드를 찾아서 실행하고, 그 결과를 출력하는 코드
# Python에서 모듈이 직접 실행될 때 (즉, 다른 모듈에서 import 되지 않고 직접 실행될 때) 해당 코드 블록을 실행하도록 하는 일종의 조건문
if __name__ == '__main__':
    # 이 클래스에서 정의된 테스트 메소드들을 자동으로 찾아주는 메소드를 사용하여 테스트 스위트(TestSuite) 객체를 생성
    suite = unittest.TestLoader().loadTestsFromTestCase(WebLogin)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)