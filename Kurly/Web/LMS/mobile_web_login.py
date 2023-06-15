import unittest
import re
import openpyxl
import xlwings as xw
import glob
import os
import pandas as pd
from TestModule import testModule
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class MobileWebLogin(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_06_mWeb_로그인(self):
        try:
            # 1. <로그인_출근>

            # 작업자 체크인상태
            # 이동할 url주소
            url = 'https://lms.stg.kurly.com/#/login'
            # url 이동
            self.driver.get(url)
            # 브라우저 최대화
            self.driver.maximize_window()

            # LMS 모바일 로그인
            # 아이디 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='junhyunkyung', error_msg="아이디 입력란 미노출")

            # 비밀번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='kurly12!@', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")

            # 출근/퇴근 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'work-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default primary')]", error_msg="출근 버튼 미노출")

            # 출근이 아닌 퇴근이 뜬다면 퇴근하고 다시 로그인 후에 출근하는 예외처리
            try:
                # 네
                self.interact(by_type="XPATH", name="//*[contains(@class, 'dialog-btn ml-0 v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="")
                # 확인
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--large')]", error_msg="")

                # 아이디 입력
                self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='junhyunkyung', error_msg="")

                # 비밀번호 입력
                self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='kurly12!@', error_msg="")

                # 로그인
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="")

                # 출근 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'work-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default primary')]", error_msg="")
            except:
                pass

            # 송파CC
            # 송파 냉장1
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파')]", error_msg="송파 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="송파 냉장1 미노출")

            # 다음
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="출근 프로세스 진행중 다음 버튼 미노출")

            # 업무파트=HUB
            # 팀명=송냉 HUB
            # 근무 Shift=00:25 ~ 05:00
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="HUB")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="팀명 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송냉 HUB')]", error_msg="송냉 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="근무 Shift 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '00:25 ~ 05:00')]", error_msg="00:25 ~ 05:00 미노출")

            # 다음
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="출근 프로세스 진행중 다음 버튼 미노출")

            # 네
            self.interact(by_type="XPATH", name="//*[contains(@class, 'bottom-btn v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="출근 프로세스 진행중 네 버튼 미노출")

            # 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-select__selections')]", error_msg="출근 프로세스 진행중 연장근무의 선택 버튼 미노출")

            # 연장근무 30분 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '30분')]", error_msg="출근 프로세스 진행중 연장근무 30분 선택 미노출")

            # 확인 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'bottom-btn v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="출근 프로세스 진행중 연장근무 선택 후 확인 버튼 미노출")

            # 네
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dialog-btn ml-0 v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="출근 프로세스 진행중 연장근무 선택 후 네 버튼 미노출")

            # 계정정보 노출 및 출근시간 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mb-1')]//*[contains(text(),'junhyunkyung')]", click=False, error_msg="출근 후 계정정보 미노출")
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'mb-1')]//strong//span")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의
            pattern = r'\d{2}:\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                pass
            else:
                raise Exception("출근 시 HH:MM:SS 형태의 시간 미노출")

            # 큐알코드 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'row justify-center')]//canvas", click=False, error_msg="출근 후 큐알코드 미노출")

            # 퇴근 버튼, 연장근무 신청변경 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'work-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default primary')]", click=False, error_msg="출근 후 퇴근 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'overtime-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default')]", click=False, error_msg="출근 후 연장근무 신청변경 버튼 미노출")



            # 2. <퇴근>

            # [퇴근] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'work-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default primary')]", error_msg="출근 후 퇴근 버튼 미노출")

            # 퇴근 처리 팝업 [네] 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dialog-btn ml-0 v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="출근 후 퇴근 버튼 클릭 시 네 팝업 미노출")

            # 퇴근 처리 되었습니다. 노출 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text d-flex justify-center')]//*[contains(text(), '퇴근 처리 되었습니다.')]", click=False, error_msg="퇴근 처리 후 퇴근 처리되었습니다. 텍스트 미노출")

            # 근무 시간 : n시간 n분
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text d-flex justify-center')]//*[contains(text(), '근무 시간')]", click=False, error_msg="퇴근 처리 후 근무 시간 미노출")

            # [확인] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--large')]", error_msg="퇴근 처리 후 확인 버튼 미노출")



            # 3. <로그인_잠김상태>

            # 아이디 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='test01', error_msg="아이디 입력란 미노출")

            # 잘못된 비밀번호 6회 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='kurly123!1', error_msg="비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='!', error_msg="비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='@3', error_msg="비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='4#', error_msg="비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='$5', error_msg="비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='sc', error_msg="비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")

            # 로그인 정보가 6회 이상 실패하여 계정 사용이 불가합니다. 관리자를 통해 계정 초기화 해주세요. 안내문구 화면 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-alert__content') and contains(text(), '로그인 정보가 5회 이상 실패하여 계정 사용이 불가')]", click=False, error_msg="로그인 정보가 5회 이상 실패하여 계정 사용이 불가합니다. 알럿 미노출")



            # 4. <작업자계정 잠김상태>

            # 관리자 로그인
            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # LMS 어드민 URL 접속
            url = 'https://admin-lms.stg.kurly.com/?#/login'
            self.driver.get(url)

            # 아이디(lmstest01) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='lmstest01', error_msg="관리자 로그인중 아이디 입력란 미노출")

            # 비밀번호(q1w2e3r4!) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='q1w2e3r4!', error_msg="관리자 로그인중 비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="관리자 로그인중 로그인 버튼 미노출")

            # 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default primary--text')]", error_msg="관리자 로그인중 확인 버튼 미노출")

            # 계정관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '계정관리')]", error_msg="관리자 로그인 후 계정관리 탭 미노출")

            # 작업자 계정 관리 진입
            self.interact(by_type="XPATH", name="//*[contains(text(), '작업자 계정 관리')]", error_msg="작업자 계정 관리 탭 미노출")

            # 계약구분 항목 값 변경 : 상용직
            # 작업자 정보 항목 값 변경 : 아이디
            # 검색어 입력 : 'test01'
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="작업자 계정 관리 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="작업자 계정 관리 탭 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="작업자 계정 관리 탭 작업자 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '아이디')]", error_msg="작업자 계정 관리 탭 아이디 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", send_keys_msg='test01', error_msg="작업자 계정 관리 탭 검색어 입력란 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="작업자 계정 관리 탭 검색 버튼 미노출")

            # [계정 비밀번호 초기화] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--small primary')]", error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 버튼 미노출")

            # 초기화 팝업 확인
            # - '초기화 대상 id' 를 초기화 하시겠습니까? [확인][취소]
            self.interact(by_type="XPATH", name="//*[contains(text(), '초기화 하시겠습니까')]", click=False, error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 버튼 미노출")

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--flat v-btn--text theme--light v-size--default')]", error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 버튼 클릭 후 확인 버튼 미노출")

            # 성공 팝업 확인
            # - 'id'가 초기화 되었습니다 [확인]
            self.interact(by_type="XPATH", name="//*[contains(text(), '초기화 되었습니다')]", click=False, error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 버튼 미노출")

            # 성공 팝업 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--flat v-btn--text theme--light v-size--default')]", error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 후 성공 팝업의 확인 버튼 미노출")



            # 5. <작업자계장 초기화 상태>

            # LMS 어드민 탭 닫기
            self.driver.close()

            # 포커스를 LMS 모바일로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(3)

            # 아이디 입력
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'v-text-field__slot')])[1]//input")))

            # JavaScript를 통해 직접 입력 필드의 값을 변경
            # JavaScript로 값을 변경할 때, 입력 필드의 값이 변경되면서 input 이벤트가 자동으로 발생하지 않음
            # 따라서 Selenium은 값이 변경된 것을 감지하지 못하고 변경된 값을 다시 전송하게 됨
            self.driver.execute_script("arguments[0].value = '';", element)

            # 값을 변경한 후에 JavaScript로 input 이벤트를 명시적으로 디스패치하여 입력 필드의 값이 변경되었음을 알려줌
            # 이렇게 하면 Selenium이 값을 변경한 것을 인식하고, 변경된 값이 다시 전송되지 않음
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
            sleep(3)
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='test01', error_msg="아이디 입력란 미노출")

            # 초기 비밀번호 입력 : kurly123!@
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'v-text-field__slot')])[2]//input")))
            self.driver.execute_script("arguments[0].value = '';", element)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
            sleep(3)
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='kurly123!@', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")

            # 비밀번호 변경 팝업 노출
            # 신규(초기화) 비밀번호는 변경이 필요합니다.
            self.interact(by_type="XPATH", name="//*[contains(text(), '신규(초기화) 비밀번호')]", click=False, error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업 미노출")

            # 비밀번호는 영문, 숫자, 특수문자 3종류 이상을 조합
            # 최소 8자리 이상 입력 필수입니다.
            self.interact(by_type="XPATH", name="//*[contains(text(), '비밀번호는 영문,숫자,특수문자 3종류 이상을 조합')]", click=False, error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업 미노출")

            # 비밀번호(영문,숫자,특수문자 3종류이상 8자리이상), 비밀번호 확인 항목 및 비밀번호 변경버튼 노출
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[4]", click=False, send_keys_msg="kurly12!@", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[5]", click=False, send_keys_msg="kurly12!@", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 확인 입력란 미노출")

            # 비밀번호 변경 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mt-5 v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 변경 버튼 미노출")

            # 확인 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--large')]", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 완료 후 확인 버튼 미노출")



            # 6. <Swagger_JWT토큰 획득>

            # Swagger 접속
            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # SWAGGER URL 접속
            url = 'https://api-lms.stg.kurly.com/swagger-ui/index.html'
            self.driver.get(url)

            # /qa/login 로그인
            self.interact(by_type="XPATH", name="//*[contains(@id,'operations-로그인-login')]//*[contains(@class,'opblock-summary-description')]", error_msg="스웨거 UI에서 /qa/login 미노출")

            # Try it out 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'btn try-out__btn')]", error_msg="스웨거 UI에서 /qa/login의 Try it out 버튼 미노출")

            # id pwd 입력 (web 계정)
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'body-param__text')]")))
            element.clear()
            self.interact(by_type="XPATH", name="//*[contains(@class,'body-param__text')]", click=False, send_keys_msg='{"id": "lmstest01", "pwd": "q1w2e3r4!"}', error_msg="스웨거 UI에서 /qa/login의 Request body 입력란 미노출")

            # [Execute] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'btn execute opblock-control__btn')]", error_msg="스웨거 UI에서 /qa/login의 Excute 버튼 미노출")

            # Response body값 복사
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'microlight')])[3]//span")))
            element_text = element.text

            # [Authorized] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'btn authorize unlocked')]", error_msg="스웨거 UI에서 [Authorized] 버튼 미노출")

            # Value Text Box 붙여넣기
            self.interact(by_type="XPATH", name="(//*[contains(@class,'wrapper')]//input)[2]", click=False, send_keys_msg=element_text, error_msg="스웨거 UI에서 [Authorized] 버튼 클릭 후 value text box 미노출")

            # [Authorize] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'btn modal-btn auth authorize button')]", error_msg="스웨거 UI에서 value 입력 후 [Authorized] 버튼 미노출")

            # [Close] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'btn modal-btn auth btn-done button')]", error_msg="스웨거 UI에서 value 입력 후 [Authorized] 버튼 클릭 시 [Close] 버튼 미노출")

            # 로그인 탭 다시 닫기
            self.interact(by_type="XPATH", name="//*[contains(@id,'operations-로그인-login')]//*[contains(@class,'opblock-summary-description')]", error_msg="스웨거 UI에서 /qa/login 미노출")



            # 10. <로그인_비밀번호 변경 후 90일 경과 상태>

            # 작업자 변경 > 패스워드 변경 91일 경과 상태적용 선택
            self.interact(by_type="XPATH", name="//*[contains(@id,'operations-작업자_변경-changeLaborAccountPwChangeDateLast90day')]//*[contains(@class,'opblock-summary-description')]", error_msg="스웨거 UI에서 작업자 변경 > 패스워드 변경 91일 경과 상태적용 미노출")

            # [Try it out] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'btn try-out__btn')]", error_msg="스웨거 UI에서 /qa/login의 Try it out 버튼 미노출")

            # ID 입력
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'body-param__text')]")))
            element.clear()
            self.interact(by_type="XPATH", name="//*[contains(@class,'body-param__text')]", click=False, send_keys_msg='{"loginId": "junhyunkyung"}', error_msg="스웨거 UI에서 /qa/login의  미노출")

            # [Execute] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'btn execute opblock-control__btn')]", error_msg="스웨거 UI에서 /qa/login의 Excute 버튼 미노출")



            # 11. <로그인_비밀번호 변경 후 90일 경과 상태>

            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # SWAGGER URL 접속
            url = 'https://lms.stg.kurly.com/#/login'
            self.driver.get(url)

            # 아이디 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='junhyunkyung', error_msg="아이디 입력란 미노출")

            # 비밀번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='kurly12!@', error_msg="비밀번호 입력란 미노출")

            # [로그인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")

            # 비밀번호 변경 팝업 노출
            # 개인정보 보호를 위해 비밀번호를 변경해주세요
            # 90일 이상 비밀번호를 변경하지 않으셨습니다. 동일한 비밀번호를 장기간 사용할 경우 개인정보 도용 및 유출 등의 위험이 있습니다
            self.interact(by_type="XPATH", name="//*[contains(text(), ' 개인정보 보호를 위해 ')]", click=False, error_msg="작업자 비밀번호 변경 후 90일 경과 상태 후 로그인 시 [개인정보~, 90일 이상~] 텍스트 미노출")

            # 비밀번호는 영문, 숫자, 특수문자 3종류 이상을 조합
            # 최소 8자리 이상 입력 필수입니다.
            self.interact(by_type="XPATH", name="//*[contains(text(), '비밀번호는 영문,숫자,특수문자 3종류 이상을 조합')]", click=False, error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업 미노출")

            # 비밀번호(영문,숫자,특수문자 3종류이상 8자리이상), 비밀번호 확인 항목 및 비밀번호 변경버튼 노출
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[4]", click=False, send_keys_msg="kurly21!@", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[5]", click=False, send_keys_msg="kurly21!@", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 확인 입력란 미노출")

            # 비밀번호 변경 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mt-5 v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 변경 버튼 미노출")

            # 확인 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--large')]", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 완료 후 확인 버튼 미노출")

            # 관리자 로그인
            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # LMS 어드민 URL 접속
            url = 'https://admin-lms.stg.kurly.com/?#/login'
            self.driver.get(url)

            # 아이디(lmstest01) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='lmstest01', error_msg="관리자 로그인중 아이디 입력란 미노출")

            # 비밀번호(q1w2e3r4!) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='q1w2e3r4!', error_msg="관리자 로그인중 비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="관리자 로그인중 로그인 버튼 미노출")

            try:
                # 아이디 입력
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'v-text-field__slot')])[1]//input")))

                # JavaScript를 통해 직접 입력 필드의 값을 변경
                # JavaScript로 값을 변경할 때, 입력 필드의 값이 변경되면서 input 이벤트가 자동으로 발생하지 않음
                # 따라서 Selenium은 값이 변경된 것을 감지하지 못하고 변경된 값을 다시 전송하게 됨
                self.driver.execute_script("arguments[0].value = '';", element)

                # 값을 변경한 후에 JavaScript로 input 이벤트를 명시적으로 디스패치하여 입력 필드의 값이 변경되었음을 알려줌
                # 이렇게 하면 Selenium이 값을 변경한 것을 인식하고, 변경된 값이 다시 전송되지 않음
                self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
                sleep(3)
                self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='lmstest01', error_msg="")

                # 초기 비밀번호 입력 : kurly123!@
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'v-text-field__slot')])[2]//input")))
                self.driver.execute_script("arguments[0].value = '';", element)
                self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
                sleep(3)
                self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='q1w2e3r4!', error_msg="비밀번호 입력란 미노출")

                # 로그인
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="관리자 로그인중 로그인 버튼 미노출")
            except:
                pass

            # 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default primary--text')]", error_msg="관리자 로그인중 확인 버튼 미노출")

            # 계정관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '계정관리')]", error_msg="관리자 로그인 후 계정관리 탭 미노출")

            # 작업자 계정 관리 진입
            self.interact(by_type="XPATH", name="//*[contains(text(), '작업자 계정 관리')]", error_msg="작업자 계정 관리 탭 미노출")

            # 계약구분 항목 값 변경 : 상용직
            # 작업자 정보 항목 값 변경 : 아이디
            # 검색어 입력 : 'junhyunkyung'
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="작업자 계정 관리 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="작업자 계정 관리 탭 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="작업자 계정 관리 탭 작업자 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '아이디')]", error_msg="작업자 계정 관리 탭 아이디 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", send_keys_msg='junhyunkyung', error_msg="작업자 계정 관리 탭 검색어 입력란 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="작업자 계정 관리 탭 검색 버튼 미노출")

            # [계정 비밀번호 초기화] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--small primary')]", error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 버튼 미노출")

            # 초기화 팝업 확인
            # - '초기화 대상 id' 를 초기화 하시겠습니까? [확인][취소]
            self.interact(by_type="XPATH", name="//*[contains(text(), '초기화 하시겠습니까')]", click=False, error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 버튼 미노출")

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--flat v-btn--text theme--light v-size--default')]", error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 버튼 클릭 후 확인 버튼 미노출")

            # 성공 팝업 확인
            # - 'id'가 초기화 되었습니다 [확인]
            self.interact(by_type="XPATH", name="//*[contains(text(), '초기화 되었습니다')]", click=False, error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 버튼 미노출")

            # 성공 팝업 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--flat v-btn--text theme--light v-size--default')]", error_msg="작업자 계정 관리 탭에서 계정 비밀번호 초기화 후 성공 팝업의 확인 버튼 미노출")

            # LMS 어드민 탭 닫기
            self.driver.close()

            # 포커스를 LMS 모바일로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(3)

            # 아이디 입력
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'v-text-field__slot')])[1]//input")))

            # JavaScript를 통해 직접 입력 필드의 값을 변경
            # JavaScript로 값을 변경할 때, 입력 필드의 값이 변경되면서 input 이벤트가 자동으로 발생하지 않음
            # 따라서 Selenium은 값이 변경된 것을 감지하지 못하고 변경된 값을 다시 전송하게 됨
            self.driver.execute_script("arguments[0].value = '';", element)

            # 값을 변경한 후에 JavaScript로 input 이벤트를 명시적으로 디스패치하여 입력 필드의 값이 변경되었음을 알려줌
            # 이렇게 하면 Selenium이 값을 변경한 것을 인식하고, 변경된 값이 다시 전송되지 않음
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
            sleep(3)
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='junhyunkyung', error_msg="아이디 입력란 미노출")

            # 초기 비밀번호 입력 : kurly123!@
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'v-text-field__slot')])[2]//input")))
            self.driver.execute_script("arguments[0].value = '';", element)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
            sleep(3)
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='kurly123!@', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="로그인 버튼 미노출")

            # 비밀번호 변경 팝업 노출
            # 신규(초기화) 비밀번호는 변경이 필요합니다.
            self.interact(by_type="XPATH", name="//*[contains(text(), '신규(초기화) 비밀번호')]", click=False, error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업 미노출")

            # 비밀번호는 영문, 숫자, 특수문자 3종류 이상을 조합
            # 최소 8자리 이상 입력 필수입니다.
            self.interact(by_type="XPATH", name="//*[contains(text(), '비밀번호는 영문,숫자,특수문자 3종류 이상을 조합')]", click=False, error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업 미노출")

            # 비밀번호(영문,숫자,특수문자 3종류이상 8자리이상), 비밀번호 확인 항목 및 비밀번호 변경버튼 노출
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[4]", click=False, send_keys_msg="kurly12!@", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 입력란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[5]", click=False, send_keys_msg="kurly12!@", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 확인 입력란 미노출")

            # 비밀번호 변경 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mt-5 v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 팝업에서 비밀번호 변경 버튼 미노출")

            # 확인 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--large')]", error_msg="비밀번호 초기화 후 로그인 시 비밀번호 변경 완료 후 확인 버튼 미노출")

            # LMS 모바일 닫기
            self.driver.close()

            # 포커스를 LMS 모바일로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

            # 스웨거 닫기
            self.driver.close()

            # 포커스를 LMS 모바일로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

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
    suite = unittest.TestLoader().loadTestsFromTestCase(MobileWebLogin)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)