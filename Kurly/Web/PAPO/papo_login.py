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

class PAPOLogin(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_01_PAPO_로그인(self):
        try:
            # 이동할 url주소
            url = 'https://partner.stg.kurly.com/#/stafflogin'

            # url 이동
            self.driver.get(url)

            # 브라우저 최대화
            self.driver.maximize_window()

            # 1. <담당자 로그인>

            # 로그인 페이지 진입
            # 아이디(qa_md2@kurlycorp.com) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, send_keys_msg='qa_md2@kurlycorp.com', error_msg="아이디 입력란 미노출")

            # 비밀번호(1234) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputPassword')]", click=False, send_keys_msg='1234', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-lg btn-block btn-primary')]", error_msg="로그인 버튼 미노출")

            # 다른 브라우저에 로그인 되어 있는 계정입니다. 라고 노출 될 경우 확인 버튼 클릭
            try:
                # 로그아웃 텍스트 확인
                self.interact(by_type="XPATH", name="//*[contains(text(), '로그아웃')]", click=False, error_msg="")

                # 확인 버튼 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="")
            except:
                pass

            # '로그인 되었습니다.' 토스트 팝업 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", click=False, error_msg="로그인 되었습니다. 텍스트 미노출")



            # 2. <담당자 로그아웃>

            # 우측 상단 로그아웃 UI선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'nav-item btn')])[2]//a", error_msg="로그아웃 버튼 미노출")

            # 초기화면(로그인페이지)으로 이동 확인
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, error_msg="초기화면(로그인페이지) 아이디 입력란 미노출")



            # 3. <공급사 로그인>

            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # 공급사 URL 접속
            url = 'https://partner.stg.kurly.com/#/login'
            self.driver.get(url)

            # 아이디(VD4360.01) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, send_keys_msg='VD4360.01', error_msg="아이디 입력란 미노출")

            # 비밀번호(kurly12!@) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputPassword')]", click=False, send_keys_msg='kurly12!@', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-lg btn-block btn-primary')]", error_msg="로그인 버튼 미노출")

            # 다른 브라우저에 로그인 되어 있는 계정입니다. 라고 노출 될 경우 확인 버튼 클릭
            try:
                self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="")
            except:
                pass

            # 90일 지나 비밀번호 변경 요청
            try:
                # 확인 버튼 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-outline-primary') and contains(text(), '확인')]", error_msg="")

                # 현재 비밀번호 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '현재 비밀번호')]", click=False, send_keys_msg='kurly12!@', error_msg="")

                # 변경 비밀번호 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '변경 비밀번호')]", click=False, send_keys_msg='kurly12!@2', error_msg="")

                # 변경 비밀번호 확인 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '변경 비밀번호확인')]", click=False, send_keys_msg='kurly12!@2', error_msg="")

                # 체크박스 클릭
                self.interact(by_type="XPATH", name="//input[contains(@type, 'checkbox')]", error_msg="")

                # 비밀번호 변경 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-lg mr-1 btn-primary')]", error_msg="")

                # 이름 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link dropdown-toggle')]", error_msg="")

                # 개인정보관리 클릭
                self.interact(by_type="XPATH", name="//*[contains(text(), '개인정보관리')]", error_msg="")

                # 현재 비밀번호 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '현재 비밀번호')]", click=False, send_keys_msg='kurly12!@2', error_msg="")

                # 변경 비밀번호 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '변경 비밀번호')]", click=False, send_keys_msg='kurly12!@3', error_msg="")

                # 변경 비밀번호 확인 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '변경 비밀번호확인')]", click=False, send_keys_msg='kurly12!@3', error_msg="")

                # 체크박스 클릭
                self.interact(by_type="XPATH", name="//input[contains(@type, 'checkbox')]", error_msg="")

                # 비밀번호 변경 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-lg mr-1 btn-primary')]", error_msg="")

                # 이름 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link dropdown-toggle')]", error_msg="")

                # 개인정보관리 클릭
                self.interact(by_type="XPATH", name="//*[contains(text(), '개인정보관리')]", error_msg="")

                # 현재 비밀번호 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '현재 비밀번호')]", click=False, send_keys_msg='kurly12!@3', error_msg="")

                # 변경 비밀번호 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '변경 비밀번호')]", click=False, send_keys_msg='kurly12!@', error_msg="")

                # 변경 비밀번호 확인 클릭
                self.interact(by_type="XPATH", name="//*[contains(@placeholder, '변경 비밀번호확인')]", click=False, send_keys_msg='kurly12!@', error_msg="")

                # 체크박스 클릭
                self.interact(by_type="XPATH", name="//input[contains(@type, 'checkbox')]", error_msg="")

                # 비밀번호 변경 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-lg mr-1 btn-primary')]", error_msg="")
            except:
                pass

            # '로그인 되었습니다.' 토스트 팝업 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", error_msg="확인 버튼 미노출")



            # 4. <공급사 로그아웃>

            # 우측 상단 로그아웃 UI선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'nav-item btn')])[2]//a", error_msg="로그아웃 버튼 미노출")

            # 초기화면(로그인페이지)으로 이동 확인
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, error_msg="초기화면(로그인페이지) 아이디 입력란 미노출")

            # 공급사 탭 닫기
            self.driver.close()

            # 포커스를 담당자 url(stafflogin)로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

            # 담당자 탭 닫기
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
    suite = unittest.TestLoader().loadTestsFromTestCase(PAPOLogin)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)