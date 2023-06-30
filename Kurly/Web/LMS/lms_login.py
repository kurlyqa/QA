import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import subprocess
# import os
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# # Slack API 토큰 설정
# client = WebClient(token=os.environ['xoxp-135797385811-4959253616502-5124347432567-b31a47aae75d6a672631fd3bba55dab7'])
#
# # 대상 사용자 ID 설정
# user_id = "U04U77FJ4ES"
#
# # 전송할 메시지 설정
# message = "테스트 결과입니다."
#
# try:
#     # DM 전송 요청
#     response = client.conversations_open(users=user_id)
#     channel_id = response["channel"]["id"]
#     client.chat_postMessage(channel=channel_id, text=message)
#     print("메시지 전송 완료")
# except SlackApiError as e:
#     print("Error sending message: {}".format(e))


class LMSLogin(unittest.TestCase):
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
    def interact(self, by_type, name, wait_sec=2, click=True, send_keys_msg=None):
        if by_type == 'XPATH':
            if send_keys_msg == None:
                if click:
                    ele = self.driver.find_element(by=By.XPATH, value=name)
                    self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
                    self.driver.execute_script("arguments[0].click();", ele)
                elif click == False:
                    ele = self.driver.find_element(by=By.XPATH, value=name)
                    self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
            else:
                self.driver.find_element(by=By.XPATH, value=name).send_keys(send_keys_msg)
            sleep(wait_sec)
        elif by_type == 'NAME':
            if send_keys_msg == None:
                if click:
                    ele = self.driver.find_element(by=By.NAME, value=name)
                    self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
                    self.driver.execute_script("arguments[0].click();", ele)
                elif click == False:
                    ele = self.driver.find_element(by=By.NAME, value=name)
                    self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
            else:
                self.driver.find_element(by=By.NAME, value=name).send_keys(send_keys_msg)
            sleep(wait_sec)

    def test_01_Login(self):
        try:
            # 이동할 url주소
            url = 'https://lms.stg.kurly.com/#/login'
            # url 이동
            self.driver.get(url)
            # 브라우저 최대화
            self.driver.maximize_window()

            ## LMS 모바일 로그인
            # 아이디 입력
            self.interact(by_type="XPATH", name="//input[@id='input-13' and @type='text' and @required='required']", click=False, send_keys_msg='junhyunkyung')
            # 비밀번호 입력
            self.interact(by_type="XPATH", name="//input[@id='input-16' and @type='password' and @required='required']", click=False, send_keys_msg='!wnsgus1')
            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content')]")

            # 출근 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'work-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default primary')]")
            # 송파CC
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파')]")
            # 송파 냉장1
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]")
            # 다음
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]")
            # 업무파트=IB
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'IB')]")
            # 팀명=ABC
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'ABC')]")
            # 근무 Shift=00:40 ~ 01:30
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '00:40 ~ 01:30')]")
            # 다음
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]")
            # 아니요
            self.interact(by_type="XPATH", name="//*[contains(@class, 'bottom-btn no-btn v-btn v-btn--contained theme--light v-size--default')]")
            # 네
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dialog-btn ml-0 v-btn v-btn--contained theme--light v-size--default primary')]")

            ## LMS 어드민 로그인
            # 새 탭 열기
            self.driver.execute_script("window.open('');")
            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])
            # LMS 어드민 URL 접속
            self.driver.get("https://admin-lms.stg.kurly.com/?#/login")
            # 아이디 입력
            self.interact(by_type="XPATH", name="//input[@id='input-16' and @type='text' and @required='required']", click=False, send_keys_msg='junhyun.kyung')
            # 비밀번호 입력
            self.interact(by_type="XPATH", name="//input[@id='input-19' and @type='password' and @required='required']", click=False, send_keys_msg='!tlgjatlf1')
            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large primary')]")
            # 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default primary--text')]")
            # 현장관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '현장관리')]")
            # CC = 송파CC
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]")
            # 센터 = 송파 냉장1 센터
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]")
            # 업무파트 = IB
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'IB')]")
            # 대분류 작업공정 = picking
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'picking')]")
            # 소분류 작업공정 = 111
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '111')]")
            # QR코드 junhyunkyung 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[6]//input", click=False, send_keys_msg='junhyunkyung')
            # 체크인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '체크인/체크아웃')]")
            # QR코드 junhyunkyung 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[6]//input", click=False, send_keys_msg='junhyunkyung')
            # 체크 아웃
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '체크인/체크아웃')]")
            # LMS 어드민 탭 닫기
            self.driver.close()
            # 포커스를 LMS 모바일로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

            # 퇴근
            self.interact(by_type="XPATH", name="//*[contains(@class, 'work-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default primary')]")
            # 네
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dialog-btn ml-0 v-btn v-btn--contained theme--light v-size--default primary')]")
            # LMS 모바일 닫기
            self.driver.close()
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
    suite = unittest.TestLoader().loadTestsFromTestCase(LMSLogin)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)