import unittest
import re
import schedule
import os
from datetime import datetime, timedelta
from selenium.webdriver import ActionChains
from TestModule import testModule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

class OrderTransferManagement(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_03_주문전송관리(self):
        try:
            # 1. <주문 전송 스케줄 등록>

            # 컬리몰 스테이지 url주소
            # kurlymall_url = 'https://www.stg.kurly.com/main'
            kurlymall_url = 'https://www-qa5.stg.kurly.com/main'

            # OMS url 주소
            oms_url = 'https://soms.stg.kurlycorp.kr/login'

            # url 이동
            self.driver.get(kurlymall_url)

            # 브라우저 최대화
            self.driver.maximize_window()

            # 로그인 페이지 진입
            self.interact(by_type="XPATH", name="//*[contains(text(), '로그인')]", error_msg="로그인 버튼 미노출")

            # 아이디(asd8680) 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'css-176lya2 e1uzxhvi3')]//input", click=False, send_keys_msg='asd8680', error_msg="아이디 입력란 미노출")

            # 비밀번호(!tlgjatlf2) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'css-176lya2 e1uzxhvi3')]//input)[2]", click=False, send_keys_msg='!tlgjatlf2', error_msg="비밀번호 입력란 미노출")

            # 로그인 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'css-qaxuc4 e4nu7ef3')]", wait_sec=10, error_msg="로그인 버튼 미노출")

            # X권역 주소 사용 : 서울 동대문구 서울시립대로 5 (신답극동아파트)
            # 컬리몰 임의이 상품 주문
            # 마우스 오버할 요소 찾기
            element_to_hover_over = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '카테고리')]")))

            # ActionChains 객체를 생성
            actions = ActionChains(self.driver)

            # 마우스 오버 동작 수행
            actions.move_to_element(element_to_hover_over).perform()

            # 물류_테스트 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '물류_테스트')]", error_msg="물류_테스트 버튼 미노출")

            # 검색어 입력란
            self.interact(by_type="XPATH", name="//*[contains(@class, 'css-w444a2 e1493ofl1')]//input", click=False, send_keys_msg='살코기 참치', error_msg="검색어 입력란 미노출")

            # 검색 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'css-ywxmlw e1493ofl0')]", error_msg="검색 버튼 미노출")

            # 첫번째 상품 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'css-0 e1c07x4811')]", error_msg="상품 미노출")

            # 장바구니 담기
            self.interact(by_type="XPATH", name="//*[contains(text(), '장바구니 담기')]", wait_sec=10, error_msg="장바구니 버튼 미노출")

            # 장바구니 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'css-g25h97 e14oy6dx1')]", error_msg="장바구니 이동 버튼 미노출")

            # 주문하기 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '주문하기')]", error_msg="주문하기 버튼 미노출")

            # 적립금 모두 사용 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'css-197i5eo e4nu7ef3')]", error_msg="적립금 모두사용 버튼 미노출")

            try:
                # 입력 버튼 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'css-q8bpgr e4nu7ef3')]", error_msg="")

                # 새로 열린 탭으로 포커스 변경
                self.driver.switch_to.window(self.driver.window_handles[-1])

                # 자유 출입 가능 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'css-1dahn5m e2sqze60')]", error_msg="")

                # 저장 버튼 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'css-nytqmg e4nu7ef1')]", error_msg="")
            except:
                pass

            # 0원 결제하기 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'css-nytqmg e4nu7ef1') and contains(text(), '0원 결제하기')]", error_msg="0원 결제하기 버튼 미노출")

            try:
                # 내일 1시에 받을수있어요 팝업
                self.interact(by_type="XPATH", name="//*[contains(text(), '결제하기')]", error_msg="")
            except:
                pass

            # 컬리몰 주문번호 복사
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'css-ciygyc epyeklp0')]")))
            order_number = element.text

            # OMS 로그인
            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # OMS URL 접속
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

            # 주문전송 관리 > 주문 전송 스케줄 메뉴 진입
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title nav__tab-content-main') and contains(text(), '주문 전송 관리')]", error_msg="OMS > 주문 전송 관리 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title nav__tab-content-sub ml-4') and contains(text(), '주문 전송 스케줄')]", error_msg="OMS > 주문 전송 관리 > 주문 전송 스케줄 버튼 미노출")

            # [등록/수정] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '등록/수정')]", error_msg="OMS > 주문전송 관리 > 주문 전송 스케줄 > [등록/수정] 버튼 미노출")

            # 추가 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '추가')]", error_msg="OMS > 주문전송 관리 > 주문 전송 스케줄 > [등록/수정] > 추가 버튼 미노출")

            # 결제일시 입력
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-text-field__slot')]//input)[3]")))
            element.click()
            self.driver.execute_script("arguments[0].value = '';", element)
            element.send_keys(current_time)

            # 전송 시작일시 입력
            # 현재 시간에 2분을 더함
            mins_after = now + timedelta(minutes=2)
            mins_after = mins_after.strftime("%H:%M:%S")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-text-field__slot')]//input)[5]")))
            element.click()
            self.driver.execute_script("arguments[0].value = '';", element)
            element.send_keys(mins_after)

            # [저장] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '저장')]", error_msg="OMS > 주문전송 관리 > 주문 전송 스케줄 > [등록/수정] > 추가 > 저장 버튼 미노출")



            # 2. <주문 스케줄 전송 확인>

            # 전송 시작시간까지 대기
            sleep(120)

            # X 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-icon notranslate mdi mdi-close theme--dark')]", error_msg="OMS > 주문전송 관리 > 주문 전송 스케줄 > [등록/수정] > 추가 > X 버튼 미노출")

            # 등록한 결제 일시 스케줄 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '조회')]", error_msg="OMS > 주문전송 관리 > 주문 전송 스케줄 > 조회 버튼 미노출")

            # 전송상태 '전송완료' 노출 확인
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-chip__content')])[3]")))
            transmission_status = element.text

            if transmission_status == "전송완료":
                pass
            else:
                raise Exception("전송완료 되지 않음")

            # 탭 닫기
            self.driver.close()

            # 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

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
    suite = unittest.TestLoader().loadTestsFromTestCase(OrderTransferManagement)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)