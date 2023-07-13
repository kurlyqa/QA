import unittest
import re
from TestModule import testModule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class LMSWebLogin(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_01_LMS_Web_로그인(self):
        try:
            # 이동할 url주소
            url = 'https://admin-lms.stg.kurly.com/?#/login'

            # url 이동
            self.driver.get(url)

            # 브라우저 최대화
            self.driver.maximize_window()

            # 로그인 페이지 진입
            # 아이디(lmstest01) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='lmstest01', error_msg="아이디 입력란 미노출")

            # 비밀번호(q1w2e3r4!) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='q1w2e3r4!', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large primary')]//*[contains(text(), '로그인')]", error_msg="로그인 버튼 미노출")

            # 로그인 되었습니다 팝업 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '로그인 되었습니다.')]", click=False, error_msg="로그인 되었습니다. 텍스트 미노출")

            # 최종접속일시 노출(YYYY-MM-DD HH:MM:SS) -> 시간에 대한 비교로 테스트하면 오차가 생기기 때문에 형태값에 대한 테스트 진행
            # 최종접속일시 노출(YYYY-MM-DD HH:MM:SS)의 UI 요소를 찾아서 안에 있는 텍스트를 가져옴
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".v-card__text div:nth-child(2)")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의
            pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                # 확인
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default primary--text')]", error_msg="확인 버튼 미노출")
                # 공정별 투입인원 현황 텍스트 노출 확인
                self.interact(by_type="XPATH", name="//*[contains(text(), '공정별 투입인원 현황')]", click=False, error_msg="공정별 투입인원 현황 텍스트 미노출")
                # 우측상단 로그아웃 UI선택
                self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--flat v-btn--icon v-btn--round theme--dark v-size--default')])[2]", error_msg="로그아웃 버튼 미노출")
                # 로그인 버튼 노출 확인
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", click=False, error_msg="로그인 버튼 미노출")

                # LMS 모바일 닫기
                self.driver.close()
            else:
                raise Exception("YYYY-MM-DD HH:MM:SS 형태의 시간이 미노출")
        except:
            self.assertEqual(0, 1)
        else:
            print("Passed")

    def tearDown(self):
        self.driver.quit()

## 이 클래스에서 정의된 테스트 메소드를 찾아서 실행하고, 그 결과를 출력하는 코드
# Python에서 모듈이 직접 실행될 때 (즉, 다른 모듈에서 import 되지 않고 직접 실행될 때) 해당 코드 블록을 실행하도록 하는 일종의 조건문
if __name__ == '__main__':
    # 이 클래스에서 정의된 테스트 메소드들을 자동으로 찾아주는 메소드를 사용하여 테스트 스위트(TestSuite) 객체를 생성
    suite = unittest.TestLoader().loadTestsFromTestCase(LMSWebLogin)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)