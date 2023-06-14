import unittest
import re
import openpyxl
import xlwings as xw
import glob
import os
import pandas as pd
from datetime import datetime
from TestModule import testModule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class SiteManagement(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_03_현장관리(self):
        try:
            # 1. <공정별 체크인/체크아웃 - 체크인>

            # 관리자 로그인 상태
            # 작업자 출근 상태
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

            # 아니요
            self.interact(by_type="XPATH", name="//*[contains(@class, 'bottom-btn no-btn v-btn v-btn--contained theme--light v-size--default')]", error_msg="출근 프로세스 진행중 아니요 버튼 미노출")

            # 네
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dialog-btn ml-0 v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="출근 프로세스 진행중 네 버튼 미노출")

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

            # 현장관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '현장관리')]", error_msg="작업자 체크인 중 현장관리 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 업무파트 변경 : HUB
            # 대분류 공정 변경 : MOVE
            # 소분류 작업공정 : PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="공정별 체크인/체크아웃 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="공정별 체크인/체크아웃 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="공정별 체크인/체크아웃 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="공정별 체크인/체크아웃 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="공정별 체크인/체크아웃 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="공정별 체크인/체크아웃 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="공정별 체크인/체크아웃 중 대분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="공정별 체크인/체크아웃 중 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="공정별 체크인/체크아웃 중 소분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="공정별 체크인/체크아웃 중 PLT 이동 미노출")

            # QR코드 입력 (ID) : junhyunkyung
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[6]//input", click=False, send_keys_msg='junhyunkyung', error_msg="작업자 체크인 중 QR코드 입력란 미노출")

            # [체크인/체크아웃] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '체크인/체크아웃')]", error_msg="작업자 체크인 중 체크인 버튼 미노출")

            # 최상단에 체크인한 아이디, 센터, 업무파트, 대분류 공정, 소분류 공정, 체크인 일시 노출, 체크아웃 일시 미노출
            # 작업자 아이디 : junhyunkyung 센터 : 송파 냉장1 업무파트 : HUB 대분류공정 : MOVE, 소분류공정 : PLT 이동
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[8]")))
            if element.text == 'junhyunkyung':
                pass
            else:
                raise Exception("체크인 후 작업자 아이디 junhyunkyung 미노출")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[9]")))
            if element.text == '송파 냉장1':
                pass
            else:
                raise Exception("체크인 후 센터 송파 냉장1 미노출")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[10]")))
            if element.text == 'HUB':
                pass
            else:
                raise Exception("체크인 후 센터 HUB 미노출")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[11]")))
            if element.text == 'MOVE':
                pass
            else:
                raise Exception("체크인 후 대분류공정 MOVE 미노출")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[12]")))
            if element.text == 'PLT 이동':
                pass
            else:
                raise Exception("체크인 후 소분류공정 PLT 이동 미노출")

            # 체크인 일시 : YYYY-MM-DD HH:mm:ss 상단 팝업 노출 자동닫힘 확인
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[13]")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의합니다.
            pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                pass
            else:
                raise Exception("체크인 시 YYYY-MM-DD HH:MM:SS 형태의 시간 미노출")

            # 체크아웃 일시 미노출
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[14]")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의합니다.
            pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                raise Exception("체크아웃하지 않았는데 체크아웃 시간 노출")
            else:
                pass

            # 이전에 해당 센터 공정 체크인/아웃 이력 모두 노출
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[15]")))
            if element.text == 'junhyunkyung':
                pass
            else:
                raise Exception("체크인 후 이전 체크인/아웃 이력 미노출")



            # 2. <공정별 체크인/체크아웃 - 체크아웃>

            # QR코드 입력 (ID) : junhyunkyung
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[6]//input", click=False, send_keys_msg='junhyunkyung', error_msg="작업자 체크인 중 QR코드 입력란 미노출")

            # [체크인/체크아웃] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '체크인/체크아웃')]", error_msg="작업자 체크인 중 체크인 버튼 미노출")

            # 체크아웃 일시 노출
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[14]")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의합니다.
            pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                pass
            else:
                raise Exception("체크아웃 후 체크아웃 시간 미노출")

            # 이전에 해당 센터 공정 체크인/아웃 이력 모두 노출
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'text-center')])[15]")))
            if element.text == 'junhyunkyung':
                pass
            else:
                raise Exception("체크인 후 이전 체크인/아웃 이력 미노출")



            # 3. <공정별 투입인원 일괄 체크아웃>

            # QR코드 입력 (ID) : junhyunkyung
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[6]//input", click=False, send_keys_msg='junhyunkyung', error_msg="작업자 체크인 중 QR코드 입력란 미노출")

            # [체크인/체크아웃] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '체크인/체크아웃')]", error_msg="작업자 체크인 중 체크인 버튼 미노출")

            # 공정별 투입인원 일괄 체크아웃 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '공정별 투입인원 일괄 체크아웃')]", error_msg="공정별 투입인원 일괄 체크아웃 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 업무파트 변경 : HUB
            # 대분류 공정 변경 : MOVE
            # 소분류 작업공정 : PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="공정별 투입인원 일괄 체크아웃 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="공정별 투입인원 일괄 체크아웃 탭 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="공정별 투입인원 일괄 체크아웃 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="공정별 투입인원 일괄 체크아웃 탭 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="공정별 투입인원 일괄 체크아웃 탭 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="공정별 투입인원 일괄 체크아웃 탭 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="공정별 투입인원 일괄 체크아웃 탭 대분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="공정별 투입인원 일괄 체크아웃 탭 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="공정별 투입인원 일괄 체크아웃 탭 소분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="공정별 투입인원 일괄 체크아웃 탭 PLT 이동 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 투입인원 일괄 체크아웃 탭 검색 버튼 미노출")

            # 업무파트 / 대분류공정 / 소분류공정 / 아이디 / 이름 / 작업자 정보상세
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'HUB')]", click=False, error_msg="공정별 투입인원 일괄 체크아웃 시 검색 결과에서 업무파트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'MOVE')]", click=False, error_msg="공정별 투입인원 일괄 체크아웃 시 검색 결과에서 대분류공정 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'PLT 이동')]", click=False, error_msg="공정별 투입인원 일괄 체크아웃 시 검색 결과에서 소분류공정 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'junhyunkyung')]", click=False, error_msg="공정별 투입인원 일괄 체크아웃 시 검색 결과에서 아이디 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), '경준현')]", click=False, error_msg="공정별 투입인원 일괄 체크아웃 시 검색 결과에서 이름 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default')]//*[contains(text(), '상세')]", click=False, error_msg="공정별 투입인원 일괄 체크아웃 시 검색 결과에서 작업자정보상세 미노출")

            # 체크인 MM:SS 확인
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'text-center')])[13]")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의합니다.
            pattern = r'\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                pass
            else:
                raise Exception("체크아웃 후 체크아웃 시간 미노출")

            # 체크박스 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-start')]//*[contains(@class, 'v-input--selection-controls__ripple')])[2]", error_msg="공정별 투입인원 일괄 체크아웃 탭 검색 결과 없음")

            # [공정 체크아웃 처리] 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mr-5 v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="공정 체크아웃 처리 버튼 미노출")

            # 팝업 노출 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')]", error_msg="공정 체크아웃 처리 버튼 클릭후 확인 버튼 미노출")

            # 완료 팝업 노출 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'flex')]//*[contains(text(), '확인')])[2]", error_msg="공정 체크아웃 처리 버튼 클릭, 확인버튼 클릭 후 완료 팝업의 확인 버튼 미노출")

            # 체크아웃된 사용자 목록에서 삭제됨
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="공정 체크아웃 처리 후 조회 결과가 없습니다 텍스트 미노출")



            # 4. <공정별 투입인원 일괄 체크아웃 초기화>

            # 초기화 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정 체크아웃 처리 후 초기화 버튼 미노출")

            # CC : 선택
            # 센터 : 선택
            # 업무파트 : 선택
            # 대분류 공정 : 선택
            # 소분류 공정 : 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//div[contains(text(), '선택')]", click=False, error_msg="초기화 버튼 클릭 후 CC 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//div[contains(text(), '선택')]", click=False, error_msg="초기화 버튼 클릭 후 센터 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//div[contains(text(), '선택')]", click=False, error_msg="초기화 버튼 클릭 후 업무파트 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//div[contains(text(), '선택')]", click=False, error_msg="초기화 버튼 클릭 후 대분류공정 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//div[contains(text(), '선택')]", click=False, error_msg="초기화 버튼 클릭 후 소분류공정 선택란 '선택' 텍스트 미노출")

            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="공정 체크아웃 처리 후 초기화 버튼 클릭시 조회 결과가 없습니다 텍스트 미노출")



            # 5. <휴대폰 소지자 QR 출력>

            # 휴대폰 소지자 QR 출력 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '휴대폰 소지자 QR 출력')]", error_msg="휴대폰 소지자 QR 출력 탭 미노출")

            # QR코드 입력 (ID) : junhyunkyung
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", click=False, send_keys_msg='junhyunkyung', error_msg="휴대폰 소지자 QR 출력 탭에서 QR 코드 입력 란 미노출")

            # [출력] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '출력')]", click=False, error_msg="휴대폰 소지자 QR 출력 탭에서 출력 버튼 미노출")



            # 6. <휴대폰 미소지자 QR출력 로그인>

            # 휴대폰 미소지자 QR출력 탭 진입
            self.interact(by_type="XPATH", name="//*[contains(@class,'v-list-item__title subtitle-1 sub-nav-item-content') and contains(text(), '휴대폰 미소지자 QR 출력')]", error_msg="휴대폰 미소지자 QR 출력 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 항목 값 변경 : 상용직
            # 업무파트 변경 : HUB
            # 팀명 항목 값 변경 : 송냉HUB
            # 근무 Shift 항목 값 변경 : 00:25 ~ 05:00
            # 이름/아이디 : 아이디
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="휴대폰 미소지자 QR출력 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="휴대폰 미소지자 QR출력 탭 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="휴대폰 미소지자 QR출력 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="휴대폰 미소지자 QR출력 탭 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="휴대폰 미소지자 QR출력 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="휴대폰 미소지자 QR출력 탭 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="휴대폰 미소지자 QR출력 탭 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="휴대폰 미소지자 QR출력 탭 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="휴대폰 미소지자 QR출력 탭 팀명 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송냉 HUB')]", error_msg="휴대폰 미소지자 QR출력 탭 송냉 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="휴대폰 미소지자 QR출력 탭 근무 Shift 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '00:25 ~ 05:00')]", error_msg="휴대폰 미소지자 QR출력 탭 00:25 ~ 05:00 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]", error_msg="휴대폰 미소지자 QR출력 탭 이름/아이디 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '아이디')]", error_msg="휴대폰 미소지자 QR출력 탭 아이디 미노출")

            # 아이디 입력 : junhyunkyung
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[8]//input", click=False, send_keys_msg='junhyunkyung', error_msg="휴대폰 미소지자 QR출력 탭 아이디 입력 미노출")

            # 휴대폰 번호 뒷 4자리 입력 : 1122
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[9]//input", click=False, send_keys_msg='1122', error_msg="휴대폰 미소지자 QR출력 탭 휴대폰 번호 뒷 4자리 입력란 미노출")

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="휴대폰 미소지자 QR출력 탭 확인 버튼 미노출")

            # 로그인 정보 일치 팝업 [확인] 버튼 선택
            # 팝업 노출
            #  - '로그인 되었습니다.'  [확인]
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')]", error_msg="휴대폰 미소지자 QR출력 탭 '로그인 되었습니다.' 미노출")

            # 상단 조회일시 노출
            #  - 조회일시 / YYYY-MM-DD(wd) HH:MM:SS 기준
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'total-container')]")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의합니다.
            pattern = r'\d{2}:\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                pass
            else:
                raise Exception("HH:MM:SS 형태의 시간 미노출")

            # 아이디/CC 센터: '로그인 작업자 계정' 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'content_information_box')]//*[contains(text(), 'junhyunkyung')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 시 junhyunkyung 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'content_information_box')]//*[contains(text(), '송파 CC 송파 냉장1 ')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 시 송파 CC 송파 냉장1 미노출")

            # 출근처리 / 작업자 QR 코드 / 작업자 QR코드 출력 / 퇴근처리 항목 노출
            #  - 작업자 QR 코드 미노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'qrImage')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 시 작업자 QR 코드 미노출")

            # 버튼 영역 확인
            #  - [확인] / [출근] 버튼 비 활성화
            #  - [초기화] / [출력] / [퇴근] 버튼 활성화
            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'primary v-btn v-btn--contained v-btn--disabled theme--light v-size--default')])[1]")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("휴대폰 미소지자 QR출력 탭에서 검색 시 [확인] 버튼 활성화 된 상태로 노출됨")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'v-btn v-btn--contained v-btn--disabled theme--light v-size--default')])[2]")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("휴대폰 미소지자 QR출력 탭에서 검색 시 [출근] 버튼 활성화 된 상태로 노출됨")

            self.interact(by_type="XPATH", name="//*[contains(@class,'v-btn__content') and contains(text(), '초기화')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 검색 시 [초기화] 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')])[1]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 검색 시 [출력] 미노출")

            # [퇴근] 버튼 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')])[2]", error_msg="휴대폰 미소지자 QR출력 탭에서 검색 시 [퇴근] 미노출")

            # 퇴근 팝업 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')])[2]", error_msg="휴대폰 미소지자 QR출력 탭 확인 버튼 미노출")



            # 7. <휴대폰 미소지자 QR출력 출근>

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 항목 값 변경 : 상용직
            # 업무파트 변경 : HUB
            # 팀명 항목 값 변경 : 송냉HUB
            # 근무 Shift 항목 값 변경 : 00:25 ~ 05:00
            # 이름/아이디 : 아이디
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="휴대폰 미소지자 QR출력 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="휴대폰 미소지자 QR출력 탭 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="휴대폰 미소지자 QR출력 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="휴대폰 미소지자 QR출력 탭 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="휴대폰 미소지자 QR출력 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="휴대폰 미소지자 QR출력 탭 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="휴대폰 미소지자 QR출력 탭 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="휴대폰 미소지자 QR출력 탭 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="휴대폰 미소지자 QR출력 탭 팀명 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송냉 HUB')]", error_msg="휴대폰 미소지자 QR출력 탭 송냉 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="휴대폰 미소지자 QR출력 탭 근무 Shift 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '00:25 ~ 05:00')]", error_msg="휴대폰 미소지자 QR출력 탭 00:25 ~ 05:00 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]", error_msg="휴대폰 미소지자 QR출력 탭 이름/아이디 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '아이디')]", error_msg="휴대폰 미소지자 QR출력 탭 아이디 미노출")

            # 아이디 입력 : junhyunkyung
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[8]//input", click=False, send_keys_msg='junhyunkyung', error_msg="휴대폰 미소지자 QR출력 탭 아이디 입력 미노출")

            # 휴대폰 번호 뒷 4자리 입력 : 1122
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[9]//input", click=False, send_keys_msg='1122', error_msg="휴대폰 미소지자 QR출력 탭 휴대폰 번호 뒷 4자리 입력란 미노출")

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="휴대폰 미소지자 QR출력 탭 확인 버튼 미노출")

            # 로그인 정보 일치 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]", error_msg="휴대폰 미소지자 QR출력 탭 확인 버튼으로 조회 시 '로그인 정보 일치' 팝업 미노출")

            # [출근] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'v-btn__content') and contains(text(), '출근')]", wait_sec=5, error_msg="휴대폰 미소지자 QR출력 탭에서 검색 후 [퇴근] 버튼 클릭 시 [출근] 미노출")

            # 팝업 노출
            #  - '출근 처리 하시겠습니까?' [확인]
            # 출근 팝업 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')])[2]", error_msg="휴대폰 미소지자 QR출력 탭 확인 버튼 미노출")

            # 상단 조회일시 노출
            #  - 조회일시 / YYYY-MM-DD(wd) HH:MM:SS 기준
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'total-container')]")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의합니다.
            pattern = r'\d{2}:\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                pass
            else:
                raise Exception("HH:MM:SS 형태의 시간 미노출")

            # 아이디/CC 센터: '로그인 작업자 계정' / CC센터 값 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'content_information_box')]//*[contains(text(), 'junhyunkyung')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 시 junhyunkyung 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'content_information_box')]//*[contains(text(), '송파 CC 송파 냉장1 ')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 시 송파 CC 송파 냉장1 미노출")

            # 출근처리 / 작업자 QR 코드 노출 / 작업자 QR코드 출력 / 퇴근처리 항목 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), '출근처리')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 출근 처리 시 출근처리 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), ' 작업자 QR코드 ')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 출근 처리 시 작업자 QR코드 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), ' 작업자 QR코드 출력 ')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 출근 처리 시 작업자 QR코드 출력 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), ' 퇴근처리 ')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 출근 처리 시 퇴근처리 탭 미노출")

            # 버튼 영역 확인
            #  - [확인] / [출근] 버튼 비 활성화
            #  - [초기화] / [출력] / [퇴근] 버튼 활성화
            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'primary v-btn v-btn--contained v-btn--disabled theme--light v-size--default')])[1]")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("휴대폰 미소지자 QR출력 탭에서 출근 후 [확인] 버튼 활성화 상태로 노출됨")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'v-btn v-btn--contained v-btn--disabled theme--light v-size--default')])[2]")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("휴대폰 미소지자 QR출력 탭에서 출근 후 [출근] 버튼 활성화 상태로 노출됨")

            self.interact(by_type="XPATH", name="//*[contains(@class,'v-btn__content') and contains(text(), '초기화')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 출근 후 [초기화] 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')])[1]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 출근 후 [출력] 미노출")



            # 8. <휴대폰 미소지자 QR출력>

            # 출력 버튼 노출 확인
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')])[1]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 출근 후 [출력] 미노출")



            # 9. <휴대폰 미소지자 QR출력 퇴근>

            # [퇴근] 버튼 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')])[2]", error_msg="휴대폰 미소지자 QR출력 탭에서 출근 후 [퇴근] 미노출")

            # 퇴근 팝업 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')])[3]", wait_sec=10, error_msg="휴대폰 미소지자 QR출력 탭 퇴근 버튼 클릭 후 확인 버튼 미노출")

            # 검색 조회 화면으로 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]//div[contains(text(), '선택')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭 퇴근 후 이름/아이디란에 선택 미노출")



            # 10. <휴대폰 미소지자 QR출력 초기화>

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 항목 값 변경 : 상용직
            # 업무파트 변경 : HUB
            # 팀명 항목 값 변경 : 송냉HUB
            # 근무 Shift 항목 값 변경 : 00:25 ~ 05:00
            # 이름/아이디 : 아이디
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="휴대폰 미소지자 QR출력 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="휴대폰 미소지자 QR출력 탭 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="휴대폰 미소지자 QR출력 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="휴대폰 미소지자 QR출력 탭 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="휴대폰 미소지자 QR출력 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="휴대폰 미소지자 QR출력 탭 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="휴대폰 미소지자 QR출력 탭 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="휴대폰 미소지자 QR출력 탭 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="휴대폰 미소지자 QR출력 탭 팀명 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송냉 HUB')]", error_msg="휴대폰 미소지자 QR출력 탭 송냉 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="휴대폰 미소지자 QR출력 탭 근무 Shift 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '00:25 ~ 05:00')]", error_msg="휴대폰 미소지자 QR출력 탭 00:25 ~ 05:00 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]", error_msg="휴대폰 미소지자 QR출력 탭 이름/아이디 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '아이디')]", error_msg="휴대폰 미소지자 QR출력 탭 아이디 미노출")

            # 아이디 입력 : junhyunkyung
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[8]//input", click=False, send_keys_msg='junhyunkyung', error_msg="휴대폰 미소지자 QR출력 탭 아이디 입력 미노출")

            # 휴대폰 번호 뒷 4자리 입력 : 1122
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[9]//input", click=False, send_keys_msg='1122', error_msg="휴대폰 미소지자 QR출력 탭 휴대폰 번호 뒷 4자리 입력란 미노출")

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="휴대폰 미소지자 QR출력 탭 확인 버튼 미노출")

            # [초기화] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'gray v-btn v-btn--contained theme--light v-size--default')]//*[contains(text(), '초기화')]", error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 [초기화] 버튼 미노출")

            # CC : 관리자 등록/수정 시 선택한 항목 값이 매핑되어 노출
            # 센터:  관리자 등록/수정 시 선택한 항목 값이 매핑되어 노출
            #  - 미 선택 시 : 선택
            # 계약구분 : 선택
            # 업무파트 : 선택
            # 팀명 : 선택디
            # 이름/아이 : 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//div[contains(text(), '송파 CC')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 CC 선택란 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//div[contains(text(), '송파 냉장1')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 센터 선택란 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//div[contains(text(), '상용직')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 계약구분 선택란 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//div[contains(text(), 'HUB')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 업무파트 선택란 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//div[contains(text(), '송냉 HUB')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 팀명 선택란 송파 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]//div[contains(text(), '00:25 ~ 05:00')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 근무 Shift 선택란 00:25 ~ 05:00 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]//div[contains(text(), '선택')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 이름/아이디 선택란 선택 미노출")

            # 이름 또는 아이디를 입력하세요 문구 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//*[contains(text(),'이름 또는 아이디를 입력하세요')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 이름 또는 아이디를 입력하세요 미노출")

            # 휴대폰 번호 뒷 4자리를 입력하세요 문구 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//*[contains(@placeholder, '휴대폰 번호 뒷 4자리를 입력하세요')]", click=False, error_msg="휴대폰 미소지자 QR출력 탭에서 로그인 후 초기화 시 휴대폰 번호 뒷 4자리를 입력하세요 미노출")

            # 조회결과 영역 초기화 상태 확인
            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'gray v-btn v-btn--contained v-btn--disabled theme--light v-size--default')]")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("휴대폰 미소지자 QR출력 탭에서 초기화 버튼 클릭 후 [초기화] 버튼 활성화 상태로 노출됨")

            # LMS 어드민 탭 닫기
            self.driver.close()
            # 포커스를 LMS 모바일로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

            # 퇴근
            self.interact(by_type="XPATH", name="//*[contains(@class, 'work-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default primary')]", error_msg="현장관리 모든 테스트 진행 후 퇴근 버튼 미노출")
            # 네
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dialog-btn ml-0 v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="현장관리 모든 테스트 진행 후 퇴근 버튼 클릭 시 네 버튼 미노출")
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
    suite = unittest.TestLoader().loadTestsFromTestCase(SiteManagement)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)