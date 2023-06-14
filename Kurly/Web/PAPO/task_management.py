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
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TaskManagement(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_02_작업관리(self):
        try:
            # 파일 삭제 시 주소 ( 각 PC마다 변경해야 함 )
            folder_path = "/Users/122d6424/Git/Kurly/Web/LMS"

            # 1. <공정별 투입인원 현황 조회>

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

            # 관리자 로그인
            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # LMS 어드민 URL 접속
            url = 'https://admin-lms.stg.kurly.com/?#/login'
            self.driver.get(url)

            # 아이디(lmstest01) 입력
            self.interact(by_type="XPATH", name="//input[@id='input-16' and @type='text' and @required='required']", click=False, send_keys_msg='lmstest01', error_msg="관리자 로그인중 아이디 입력란 미노출")
            # 비밀번호(q1w2e3r4!) 입력
            self.interact(by_type="XPATH", name="//input[@id='input-19' and @type='password' and @required='required']", click=False, send_keys_msg='q1w2e3r4!', error_msg="관리자 로그인중 비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large primary')]", error_msg="관리자 로그인중 로그인 버튼 미노출")

            # 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default primary--text')]", error_msg="관리자 로그인중 확인 버튼 미노출")

            # 현장관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '현장관리')]", error_msg="작업자 체크인 중 현장관리 탭 없음")

            # CC = 송파CC
            # 센터 = 송파 냉장1 센터
            # 업무파트 = HUB
            # 대분류 작업공정 = MOVE
            # 소분류 작업공정 = PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="작업자 체크인 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="작업자 체크인 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="작업자 체크인 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="작업자 체크인 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="작업자 체크인 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="작업자 체크인 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="작업자 체크인 중 대분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="작업자 체크인 중 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="작업자 체크인 중 소분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="작업자 체크인 중 PLT 이동 미노출")

            # QR코드 junhyunkyung 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[6]//input", click=False, send_keys_msg='junhyunkyung', error_msg="작업자 체크인 중 QR코드 입력란 미노출")

            # 체크인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '체크인/체크아웃')]", error_msg="작업자 체크인 중 체크인 버튼 미노출")

            # 작업관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '작업관리')]", error_msg="작업자 체크인 중 작업관리 탭 미노출")

            # 공정별 투입인원 현황 텍스트 노출 확인
            self.interact(by_type="XPATH", name="//*[contains(text(), '공정별 투입인원 현황')]", error_msg="공정별 투입인원 현황 텍스트 미노출")

            # CC = 송파CC
            # 센터 = 송파 냉장1 센터
            # 업무파트 = HUB
            # 대분류 작업공정 = MOVE
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="공정별 투입인원 현황 조회중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="공정별 투입인원 현황 조회중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="공정별 투입인원 현황 조회중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="공정별 투입인원 현황 조회중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="공정별 투입인원 현황 조회중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="공정별 투입인원 현황 조회중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="공정별 투입인원 현황 조회중 대분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="공정별 투입인원 현황 조회중 MOVE 미노출")

            # 검색 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 투입인원 현황 조회중 검색 버튼 미노출")

            # CC / 센터 / 업무파트 (YYYY-MM-DD HH:MM) 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '송파 CC 송파 냉장1 HUB')]", click=False, error_msg="공정별 투입인원 현황 검색 결과 미노출")

            # YYYY-MM-DD HH:MM:SS 의 UI 요소를 찾아서 안에 있는 텍스트를 가져옴
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".purple-bold > span:nth-child(2)")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의
            pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                pass
            else:
                raise Exception("YYYY-MM-DD HH:MM 형태의 시간 미노출")

            # 대분류 / 소분류 공정/ Check In 값 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center v-data-table__divider tableHeader')]//span[contains(text(), 'MOVE')]", click=False, error_msg="공정별 투입인원 현황 검색 결과 중 대분류 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center v-data-table__divider tableHeader')]//span[contains(text(), 'PLT 이동')]", click=False, error_msg="공정별 투입인원 현황 검색 결과 중 소분류 미노출")
            try:
                self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center v-data-table__divider') and contains(text(), '2 명')])[2]", click=False, error_msg="")
            except:
                self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center v-data-table__divider') and contains(text(), '1 명')])[2]", click=False, error_msg="")



            # 2. <공정별 투입인원 현황 조회 초기화>

            # 초기화 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 투입인원 현황 검색 후 초기화 버튼 미노출")

            # CC : 선택
            # 센터 : 선택
            # 업무파트 : 선택
            # 대분류 공정 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//div[contains(text(), '선택')]", click=False, error_msg="초기화 버튼 클릭 후 CC 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//div[contains(text(), '선택')]", click=False, error_msg="초기화 버튼 클릭 후 센터 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//div[contains(text(), '선택')]", click=False, error_msg="초기화 버튼 클릭 후 업무파트 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//div[contains(text(), '전체')]", click=False, error_msg="초기화 버튼 클릭 후 대분류공정 선택란 '전체' 텍스트 미노출")

            # 조회결과 영역 초기화 상태 확인
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-center v-data-table__divider tableHeader")))
                raise Exception("초기화 상태인데 조회 결과 노출됨")
            except:
                pass



            # 3. <공정별 체크인 작업자 확인 조회-체크인 상태 확인>

            # 1번, 2번 TC에서 체크인 상태 확인함



            # 4. <공정별 체크인 작업자 확인 조회-체크아웃 상태 확인>

            # 현장관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '현장관리')]", error_msg="작업자 체크인 중 현장관리 탭 없음")

            # CC = 송파CC
            # 센터 = 송파 냉장1 센터
            # 업무파트 = HUB
            # 대분류 작업공정 = MOVE
            # 소분류 작업공정 = PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="작업자 체크인 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="작업자 체크인 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="작업자 체크인 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="작업자 체크인 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="작업자 체크인 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="작업자 체크인 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="작업자 체크인 중 대분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="작업자 체크인 중 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="작업자 체크인 중 소분류 작업공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="작업자 체크인 중 PLT 이동 미노출")

            # QR코드 junhyunkyung 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[6]//input", click=False, send_keys_msg='junhyunkyung', error_msg="작업자 체크인 중 QR코드 입력란 미노출")

            # 체크아웃
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '체크인/체크아웃')]", error_msg="작업자 체크인 중 체크아웃 버튼 미노출")

            # 아이디, 센터, 업무파트, 대분류 공정, 소분류 공정, 체크인, 체크아웃
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '아이디')]", error_msg="작업자 체크아웃 확인중 아이디 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '센터')]", error_msg="작업자 체크아웃 확인중 센터 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '업무파트')]", error_msg="작업자 체크아웃 확인중 업무파트 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '대분류 공정')]", error_msg="작업자 체크아웃 확인중 대분류 공정 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '소분류 공정')]", error_msg="작업자 체크아웃 확인중 소분류 공정 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '체크인')]", error_msg="작업자 체크아웃 확인중 체크인 탭 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '체크아웃')]", error_msg="작업자 체크아웃 확인중 체크아웃 탭 미노출")

            # 데이터 노출 확인 - 체크아웃 위치에 시간 노출 확인
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'text-center')])[14]")))
            time_text = time_element.text

            # 시간값을 추출하기 위한 정규표현식을 정의
            pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, time_text)

            # 형태가 일치하지 않을 경우 match의 값이 None
            if match:
                pass
            else:
                raise Exception("체크아웃 실패")



            # 5. <공정별 체크인 작업자 확인 조회 초기화>

            # 작업관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '작업관리')]", error_msg="공정별 체크인 작업자 확인 조회 중 작업관리 탭 미노출")

            # 공정별 체크인 작업자 확인 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '공정별 체크인 작업자 확인')]", error_msg="공정별 체크인 작업자 확인 탭 미노출")

            # CC = 송파CC
            # 센터 = 송파 냉장1
            # 계약구분 = 상용직
            # 업무파트 = HUB
            # 대분류 공정 = MOVE
            # 소분류 공정 = PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="공정별 체크인 작업자 확인 조회 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="공정별 체크인 작업자 확인 조회 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="공정별 체크인 작업자 확인 조회 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="공정별 체크인 작업자 확인 조회 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="공정별 체크인 작업자 확인 조회 중 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="공정별 체크인 작업자 확인 조회 중 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="공정별 체크인 작업자 확인 조회 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="공정별 체크인 작업자 확인 조회 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="공정별 체크인 작업자 확인 조회 중 대분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="공정별 체크인 작업자 확인 조회 중 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="공정별 체크인 작업자 확인 조회 중 소분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="공정별 체크인 작업자 확인 조회 중 PLT 이동 미노출")

            # 검색 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 체크인 작업자 확인 조회 중 검색 버튼 미노출")

            # 검색 결과 확인(다운로드 버튼 노출 확인)
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]", click=False, error_msg="공정별 체크인 작업자 확인 조회 후 다운로드 버튼 미노출")

            # 초기화 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 체크인 작업자 확인 조회 후 초기화 버튼 미노출")

            # 조회테이블 영역 항목 옵션 값 초기화
            # CC : 전체
            # 센터 : 전체
            # 업무파트 : 전체
            # 대분류 공정 : 전체
            # 소분류 공정 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//div[contains(text(), '전체')]", click=False, error_msg="공정별 체크인 작업자 확인 조회 후 초기화 버튼 클릭 후 CC 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//div[contains(text(), '전체')]", click=False, error_msg="공정별 체크인 작업자 확인 조회 후 초기화 버튼 클릭 후 센터 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//div[contains(text(), '전체')]", click=False, error_msg="공정별 체크인 작업자 확인 조회 후 초기화 버튼 클릭 후 업무파트 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//div[contains(text(), '전체')]", click=False, error_msg="공정별 체크인 작업자 확인 조회 후 초기화 버튼 클릭 후 대분류공정 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//div[contains(text(), '전체')]", click=False, error_msg="공정별 체크인 작업자 확인 조회 후 초기화 버튼 클릭 후 소분류공정 선택란 '전체' 텍스트 미노출")

            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="공정별 체크인 작업자 확인 조회 후 초기화 버튼 클릭 후 조회 결과가 없습니다 텍스트 미노출")



            # 6. <공정공정별 체크인 작업자 확인 작업상세내역 다운로드>

            # CC = 송파CC
            # 센터 = 송파 냉장1
            # 계약구분 = 상용직
            # 업무파트 = HUB
            # 대분류 공정 = MOVE
            # 소분류 공정 = PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="공정별 체크인 작업자 확인 조회 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="공정별 체크인 작업자 확인 조회 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="공정별 체크인 작업자 확인 조회 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="공정별 체크인 작업자 확인 조회 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="공정별 체크인 작업자 확인 조회 중 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="공정별 체크인 작업자 확인 조회 중 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="공정별 체크인 작업자 확인 조회 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="공정별 체크인 작업자 확인 조회 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="공정별 체크인 작업자 확인 조회 중 대분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="공정별 체크인 작업자 확인 조회 중 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="공정별 체크인 작업자 확인 조회 중 소분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="공정별 체크인 작업자 확인 조회 중 PLT 이동 미노출")

            # 검색 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 체크인 작업자 확인 조회 중 검색 버튼 미노출")

            # [다운로드] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="공정별 체크인 작업자 확인 조회 후 다운로드 버튼 미노출")

            # 개인정보 다운로드 설정 사유 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[7]//input", click=False, send_keys_msg='테스트테스트테스트테스트', error_msg="공정별 체크인 작업자 확인 조회 후 다운로드 시 다운로드 사유 입력란 미노출")

            # 파일 비밀번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[8]//input", click=False, send_keys_msg='!testtest1', error_msg="공정별 체크인 작업자 확인 조회 후 다운로드 시 파일 비밀번호 입력란 미노출")

            # [등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary__btn')]", error_msg="공정별 체크인 작업자 확인 조회 후 다운로드 시 등록 버튼 미노출")

            # 다운받은 엑셀 파일 삭제
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".xlsx"):
                    file_path = os.path.join(folder_path, file_name)
                    os.remove(file_path)



            # 7. <공정별 이탈 작업자 확인 조회>

            # 공정별 체크인 작업자 확인 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '공정별 이탈 작업자 확인')]", error_msg="공정별 이탈 작업자 확인 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 값 변경 : 상용직
            # 업무파트 변경 : HUB
            # 대분류 공정 변경 : MOVE
            # 소분류 공정값 변경 : PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="공정별 이탈 작업자 확인 조회 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="공정별 이탈 작업자 확인 조회 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="공정별 이탈 작업자 확인 조회 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="공정별 이탈 작업자 확인 조회 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="공정별 이탈 작업자 확인 조회 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="공정별 이탈 작업자 확인 조회 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="공정별 이탈 작업자 확인 조회 중 대분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="공정별 이탈 작업자 확인 조회 중 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="공정별 이탈 작업자 확인 조회 중 소분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="공정별 이탈 작업자 확인 조회 중 PLT 이동 미노출")

            # 검색 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 이탈 작업자 확인 조회 중 검색 버튼 미노출")

            # 아이디 / 이름 / 업무파트 / 대분류공정 / 소분류공정 / 상태 / 경과시간 / 작업자정보상세 항목 노출
            # 조회테이블 영역 항목 옵션 값 초기화
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'junhyunkyung')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 시 조회 결과의 아이디 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), '경준현')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 시 조회 결과의 이름 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'HUB')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 시 조회 결과의 업무파트 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'MOVE')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 시 조회 결과의 대분류공정 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'PLT 이동')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 시 조회 결과의 소분류공정 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), ' 체크아웃 ')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 시 조회 결과의 상태 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default')]//span[contains(text(), '상세')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 시 조회 결과의 작업자정보상세 텍스트 미노출")

            # 1분 경과시마다 경과시간 +1 증가
            # HH:MM:SS 의 UI 요소를 찾아서 텍스트를 비교

            # 시작시간
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".total-container")))
            before = time_element.text
            # 시간값을 추출하기 위한 정규표현식을 정의
            pattern = r'\d{2}:\d{2}:\d{2}'
            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, before)
            time_obj = datetime.strptime(match.group(), "%H:%M:%S")
            before_time_short = time_obj.strftime("%M")

            # 1분 경과
            sleep(65)

            # 새로고침
            self.driver.refresh()

            # 1분 후 시간
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".total-container")))
            after = time_element.text
            # 시간값을 추출하기 위한 정규표현식을 정의
            pattern = r'\d{2}:\d{2}:\d{2}'
            # 위에 정규식 패턴이 추출한 text에 존재하는지 확인
            match = re.search(pattern, after)
            time_obj = datetime.strptime(match.group(), "%H:%M:%S")
            after_time_short = time_obj.strftime("%M")

            if before_time_short == after_time_short:
                raise Exception("YYYY-MM-DD HH:MM 형태의 시간 미노출")
            else:
                pass



            # 8. <공정별 이탈 작업자 확인 조회 초기화>

            # 초기화 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 이탈 작업자 확인 조회 후 초기화 버튼 미노출")

            # 조회테이블 영역 항목 옵션 값 초기화
            # CC : 관리자 등록/수정 시 선택한 항목 값이 매핑되어 노출
            # 센터:  관리자 등록/수정 시 선택한 항목 값이 매핑되어 노출
            #  - 미 선택 시 : 전체 / 계약구분: 전체 / 업무파트:전체 / 대분류 공정: 전체 / 소분류 공정: 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", click=False, error_msg="공정별 이탈 작업자 확인 조회 초기화 후 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//*[contains(text(), '전체')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 중 전체 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", click=False, error_msg="공정별 이탈 작업자 확인 조회 초기화 후 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//*[contains(text(), '전체')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 중 전체 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", click=False, error_msg="공정별 이탈 작업자 확인 조회 초기화 후 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//*[contains(text(), '전체')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 중 전체 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", click=False, error_msg="공정별 이탈 작업자 확인 조회 초기화 후 대분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//*[contains(text(), '전체')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 중 전체 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", click=False, error_msg="공정별 이탈 작업자 확인 조회 초기화 후 소분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//*[contains(text(), '전체')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 초기화 후 전체 미노출")

            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", click=False, error_msg="공정별 이탈 작업자 확인 조회 후 초기화 버튼 클릭 후 조회 결과가 없습니다 텍스트 미노출")



            # 9. <작업자별 작업이력 확인 조회>

            # 관리자 로그인 상태
            # 작업자별 작업이력이 있는 상태
            # 작업자별 작업이력 확인 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '작업자별 작업이력 확인')]", error_msg="작업자별 작업이력 확인 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 값 변경 : 상용직
            # 업무파트 변경 : HUB
            # 대분류 공정 변경 : MOVE
            # 소분류 공정값 변경 : PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="작업자별 작업이력 확인 조회 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="작업자별 작업이력 확인 조회 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="작업자별 작업이력 확인 조회 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="작업자별 작업이력 확인 조회 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="작업자별 작업이력 확인 조회 중 작업자 정보 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '아이디')]", error_msg="작업자별 작업이력 확인 조회 중 아이디 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[4]//input", click=False, send_keys_msg='junhyunkyung', error_msg="작업자별 작업이력 확인 조회 중 검색어 입력란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="작업자별 작업이력 확인 조회 중 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="작업자별 작업이력 확인 조회 중 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="작업자별 작업이력 확인 조회 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="작업자별 작업이력 확인 조회 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="작업자별 작업이력 확인 조회 중 기준 대분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="작업자별 작업이력 확인 조회 중 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]", error_msg="작업자별 작업이력 확인 조회 중 기준 소분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="작업자별 작업이력 확인 조회 중 PLT 이동 미노출")

            # [검색]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 이탈 작업자 확인 조회 중 검색 버튼 미노출")

            # 작업자아이디 / 계약구분/ 최근출근일자 / 충 출근일수 / 최근 작업공정 / 공정별투입시간(분) 상세 / 작업내역 상세 / 작업자정보 상세 항목 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'junhyunkyung')]", click=False, error_msg="작업자별 작업이력 확인 조회 후 조회 결과의 아이디 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), '상용직')]", click=False, error_msg="작업자별 작업이력 확인 조회 후조회 결과의 계약구분 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'HUB')]", click=False, error_msg="작업자별 작업이력 확인 조회 후 조회 결과의 최근 작업공정의 업무파트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'MOVE')]", click=False, error_msg="작업자별 작업이력 확인 조회 후 조회 결과의 최근 작업공정의 대분류 공정 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center') and contains(text(), 'PLT 이동')]", click=False, error_msg="작업자별 작업이력 확인 조회 후 조회 결과의 최근 작업공정의 소분류 공정 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default')]//span[contains(text(), '상세')])[3]", click=False, error_msg="작업자별 작업이력 확인 조회 후 조회 결과의 작업자정보상세 텍스트 미노출")

            # Total:n으로 노출 및 작업자 공정별 근무내역 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-toolbar__title') and contains(text(), 'Total : 1')]", click=False, error_msg="작업자별 작업이력 확인 조회 후 조회 결과에서 Total : 1 텍스트 미노출")



            # 10. <작업자별  작업이력 확인 조회 초기화>

            # [초기화]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="작업자별 작업이력 확인 조회 후 초기화 버튼 미노출")

            # CC : 관리자 등록/수정 시 선택한 항목 값이 매핑되어 노출
            # 센터:  관리자 등록/수정 시 선택한 항목 값이 매핑되어 노출
            #  - 미 선택 시 계약구분 : 전체 / 업무파트 : 전체 / 대분류 공정 : 전체 / 소분류 공정 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//*[contains(text(), '전체')]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 전체 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//*[contains(text(), '전체')]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 전체 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 대분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]//*[contains(text(), '전체')]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 전체 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 소분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]//*[contains(text(), '전체')]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 전체 미노출")

            # 작업시간 : [작업시간 입력칸]분 이상 / 날짜 : 당일
            self.interact(by_type="XPATH", name="//*[contains(@class, 'col') and contains(text(), '분 이상')]", click=False, error_msg="작업자별 작업이력 확인 초기화 후 분 이상 텍스트 미노출")

            # 날짜 클릭 후 표시된 날짜 추출
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[3]//input", error_msg="작업자별 작업이력 확인 조회 후 초기화 버튼 클릭 시 조회 결과가 없습니다 텍스트 미노출")
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'v-btn v-date-picker-table__current v-btn--active v-btn--text v-btn--rounded theme--light accent')]//*[contains(@class, 'v-btn__content')]")))

            # 표시 된 날짜의 가장 오른쪽 하나의 숫자
            time_text = time_element.text
            time_text = str(time_text)[-1]

            # 오늘 날짜 가장 오른쪽 하나의 숫자
            today = datetime.today().strftime('%Y-%m-%d')
            today = str(today)[-1]

            # 비교
            if time_text == today:
                pass
            else:
                raise Exception("작업자별 작업이력 확인 조회 후 초기화 버튼 클릭 시 날짜가 당일이 아님")

            # 날짜 선택창 닫기 위해 오늘 날짜 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-date-picker-table__current v-btn--active v-btn--text v-btn--rounded theme--light accent')]//*[contains(@class, 'v-btn__content')]", error_msg="작업자별 작업이력 확인 초기화 시 오늘 날짜 선택 미노출")
            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", click=False, error_msg="작업자별 작업이력 확인 조회 후 초기화 버튼 클릭 시 조회 결과가 없습니다 텍스트 미노출")



            # 11. <작업자별 작업이력 확인 작업자상세내역 다운로드>

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 값 변경 : 상용직
            # 업무파트 변경 : HUB
            # 대분류 공정 변경 : MOVE
            # 소분류 공정값 변경 : PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="작업자별 작업이력 확인 조회 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="작업자별 작업이력 확인 조회 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="작업자별 작업이력 확인 조회 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="작업자별 작업이력 확인 조회 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="작업자별 작업이력 확인 조회 중 작업자 정보 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '아이디')]", error_msg="작업자별 작업이력 확인 조회 중 아이디 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input__slot white')])[4]//input", click=False, send_keys_msg='junhyunkyung', error_msg="작업자별 작업이력 확인 조회 중 검색어 입력란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="작업자별 작업이력 확인 조회 중 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="작업자별 작업이력 확인 조회 중 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="작업자별 작업이력 확인 조회 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="작업자별 작업이력 확인 조회 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="작업자별 작업이력 확인 조회 중 기준 대분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'MOVE')]", error_msg="작업자별 작업이력 확인 조회 중 MOVE 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]", error_msg="작업자별 작업이력 확인 조회 중 기준 소분류 공정 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'PLT 이동')]", error_msg="작업자별 작업이력 확인 조회 중 PLT 이동 미노출")

            # [검색]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="공정별 이탈 작업자 확인 조회 중 검색 버튼 미노출")

            # [다운로드] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="공정별 이탈 작업자 확인 조회 후 다운로드 버튼 미노출")

            # 다운받은 엑셀 파일 삭제
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".xlsx"):
                    file_path = os.path.join(folder_path, file_name)
                    os.remove(file_path)



            # 12. <연장근무 희망 관리 조회>

            # 공정별 체크인 작업자 확인 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '연장근무 희망 관리')]", error_msg="연장근무 희망 관리 탭 미노출")

            # CC 항목 값 변경
            # 센터 항목 값 변경
            # 계약구분 값 변경
            # 출근 업무파트 값 변경
            # 팀명 값 변경
            # 근무 Shift
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="연장근무 희망 관리 조회 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="연장근무 희망 관리 확인 조회 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="연장근무 희망 관리 확인 조회 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="연장근무 희망 관리 조회 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="연장근무 희망 관리 조회 중 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="연장근무 희망 관리 조회 중 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="연장근무 희망 관리 조회 중 출근업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="연장근무 희망 관리 조회 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="연장근무 희망 관리 조회 중 팀명 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송냉 HUB')]", error_msg="연장근무 희망 관리 조회 중 송냉 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="연장근무 희망 관리 조회 중 근무 Shift 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '00:25 ~ 05:00')]", error_msg="연장근무 희망 관리 조회 중 00:25 ~ 05:00 미노출")

            # [검색]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="연장근무 희망 관리 조회 중 검색 버튼 미노출")

            # CC / 센터 / 최종 체크인 대분류공정 / 최종 체크인 소분류공정 / 계약구분 / 업무파트 / 팀명 / 근무shift /
            # 아이디 / 이름 / 연장근무 가능시간 / 작업자 상세 항목 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, 'CC')]", click=False, error_msg="연장근무 희망 관리 검색 후 CC 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '센터')]", click=False, error_msg="연장근무 희망 관리 검색 후 센터 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '최종 체크인 대분류 공정')]", click=False, error_msg="연장근무 희망 관리 검색 후 최종 체크인 대분류 공정 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '최종 체크인 소분류 공정')]", click=False, error_msg="연장근무 희망 관리 검색 후 최종 체크인 소분류 공정 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '계약구분')]", click=False, error_msg="연장근무 희망 관리 검색 후 계약구분 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '출근업무파트')]", click=False, error_msg="연장근무 희망 관리 검색 후 출근업무파트 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '팀명')]", click=False, error_msg="연장근무 희망 관리 검색 후 팀명 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '근무 Shift')]", click=False, error_msg="연장근무 희망 관리 검색 후 근무 Shift 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '아이디')]", click=False, error_msg="연장근무 희망 관리 검색 후 아이디 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '이름')]", click=False, error_msg="연장근무 희망 관리 검색 후 이름 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '연장근무 가능 시간')]", click=False, error_msg="연장근무 희망 관리 검색 후 연장근무 가능 시간 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '작업자 상세')]", click=False, error_msg="연장근무 희망 관리 검색 후 작업자 상세 항목명 미노출")

            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[13]", click=False, error_msg="연장근무 희망 관리 검색 후 CC 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[14]", click=False, error_msg="연장근무 희망 관리 검색 후 센터 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[15]", click=False, error_msg="연장근무 희망 관리 검색 후 최종 체크인 대분류 공정 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[16]", click=False, error_msg="연장근무 희망 관리 검색 후 최종 체크인 소분류 공정 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[17]", click=False, error_msg="연장근무 희망 관리 검색 후 계약구분 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[18]", click=False, error_msg="연장근무 희망 관리 검색 후 출근업무파트 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[19]", click=False, error_msg="연장근무 희망 관리 검색 후 팀명 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[20]", click=False, error_msg="연장근무 희망 관리 검색 후 근무 Shift 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[21]", click=False, error_msg="연장근무 희망 관리 검색 후 아이디 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[22]", click=False, error_msg="연장근무 희망 관리 검색 후 이름 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[23]", click=False, error_msg="연장근무 희망 관리 검색 후 연장근무 가능 시간 결과 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'text-center')])[24]", click=False, error_msg="연장근무 희망 관리 검색 후 작업자 상세 결과 미노출")



            # 13. <연장근무 희망 관리 조회 초기화>

            # [초기화]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="연장근무 희망 관리 조회 후 초기화 버튼 미노출")

            # 조회테이블 영역 항목 옵션 값 초기화

            # CC : 선택 / 센터 : 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//*[contains(text(), '선택')]", click=False, error_msg="연장근무 희망 관리 초기화 후 CC 선택란 선택 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//*[contains(text(), '선택')]", click=False, error_msg="연장근무 희망 관리 초기화 후 센터 선택란 선택 텍스트 미노출")

            # 계약구분 : 전체(비활)
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//*[contains(text(), '전체')]", click=False, error_msg="연장근무 희망 관리 초기화 후 계약구분 선택란 전체 텍스트 미노출")
            # select 요소 선택
            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-select__selections')])[3]//input")))

            # input 태그의 비활성화 여부 확인하기
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("연장근무 희망 관리 초기화 후 계약구분 활성화 상태")

            # 출근업무파트:전체(비활)
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//*[contains(text(), '전체')]", click=False, error_msg="연장근무 희망 관리 초기화 후 출근업무파트 선택란 전체 텍스트 미노출")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-select__selections')])[4]//input")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("연장근무 희망 관리 초기화 후 업무파트 활성화 상태")

            # 팀명: 전체(비활)
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//*[contains(text(), '전체')]", click=False, error_msg="연장근무 희망 관리 초기화 후 팀명 선택란 전체 텍스트 미노출")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-select__selections')])[5]//input")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("연장근무 희망 관리 초기화 후 팀명 활성화 상태")

            # 근무Shift:전체(비활)
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]//*[contains(text(), '전체')]", click=False, error_msg="연장근무 희망 관리 초기화 후 근무Shift 선택란 전체 텍스트 미노출")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-select__selections')])[6]//input")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("연장근무 희망 관리 초기화 후 근무Shift 활성화 상태")

            # 연장근무 가능시간:전체(비활)
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]//*[contains(text(), '전체')]", click=False, error_msg="연장근무 희망 관리 초기화 후 연장근무 선택란 전체 텍스트 미노출")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-select__selections')])[7]//input")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("연장근무 희망 관리 초기화 후 연장근무 가능시간 활성화 상태")

            # 최종 체크인 대분류 공정:선택(비활)
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[8]//*[contains(text(), '선택')]", click=False, error_msg="연장근무 희망 관리 초기화 후 최종 체크인 대분류 공정 선택란 전체 텍스트 미노출")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-select__selections')])[8]//input")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("연장근무 희망 관리 초기화 후 최종 체크인 대분류 공정 활성화 상태")

            # 최종 체크인 소분류 공정:선택(비활)
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[9]//*[contains(text(), '선택')]", click=False, error_msg="연장근무 희망 관리 초기화 후 최종 체크인 소분류 공정 선택란 전체 텍스트 미노출")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-select__selections')])[9]//input")))
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("연장근무 희망 관리 초기화 후 최종 체크인 소분류 공정 활성화 상태")

            # 이름/아이디 : 인풋박스
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//*[contains(text(), '이름/아이디')]", click=False, error_msg="연장근무 희망 관리 초기화 후 이름/아이디 입력란 미노출")



            # 14. <연장근무 희망 관리 작업자상세내역 다운로드>

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 값 변경 : 상용직
            # 업무파트 변경 : HUB
            # 팀명 변경 : 송냉 HUB
            # 근무 Shift 변경 : 00:25 ~ 05:00
            # 대분류 공정 변경 : MOVE
            # 소분류 공정값 변경 : PLT 이동
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="연장근무 희망 관리 조회 중 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="연장근무 희망 관리 조회 중 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="연장근무 희망 관리 조회 중 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="연장근무 희망 관리 조회 중 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="연장근무 희망 관리 조회 중 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="연장근무 희망 관리 조회 중 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="연장근무 희망 관리 조회 중 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="연장근무 희망 관리 조회 중 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="연장근무 희망 관리 조회 중 팀명 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송냉 HUB')]", error_msg="연장근무 희망 관리 조회 중 송냉 HUB 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]", error_msg="연장근무 희망 관리 조회 중 기준 근무Shift 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '00:25 ~ 05:00')]", error_msg="연장근무 희망 관리 조회 중 00:25 ~ 05:00 미노출")

            # [검색]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="연장근무 희망 관리 탭 검색 버튼 미노출")

            # [다운로드] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="연장근무 희망 관리 조회 후 다운로드 버튼 미노출")

            # 개인정보 다운로드 설정 사유 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[2]", click=False, send_keys_msg='테스트테스트테스트테스트', error_msg="연장근무 희망 관리 조회 후 다운로드 시 다운로드 사유 입력란 미노출")

            # 파일 비밀번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[3]", click=False, send_keys_msg='!testtest1', error_msg="연장근무 희망 관리 조회 후 다운로드 시 파일 비밀번호 입력란 미노출")

            # [등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary__btn')]", error_msg="연장근무 희망 관리 조회 후 다운로드 시 등록 버튼 미노출")

            # 다운받은 엑셀 파일 삭제
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".xlsx"):
                    file_path = os.path.join(folder_path, file_name)
                    os.remove(file_path)



            # 15. <센터별 출근 작업자 확인 조회>

            # 센터별 출근 작업자 확인 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '센터별 출근 작업자 확인')]", error_msg="센터별 출근 작업자 확인 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파 냉장1
            # 계약구분 값 변경 : 상용직
            # 출근업무파트 변경 : HUB
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="센터별 출근 작업자 확인 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="센터별 출근 작업자 확인 탭 CC 항목 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="센터별 출근 작업자 확인 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="센터별 출근 작업자 확인 탭 센터 항목 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="센터별 출근 작업자 확인 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="센터별 출근 작업자 확인 탭 계약구분 항목 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="센터별 출근 작업자 확인 탭 출근업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="센터별 출근 작업자 확인 탭 출근업무파트 항목 HUB 미노출")

            # [검색]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="센터별 출근 작업자 확인 탭 검색 버튼 미노출")

            # CC / 센터 / 계약 구분 / 출근업무파트 / 팀명 / 근무Shift / 체크인상태 / 아이디 / 이름 / 출근일시 / 작업자정보상세
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, 'CC')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 CC 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '센터')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 센터 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '계약 구분')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 계약 구분 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '출근업무파트')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 출근업무파트 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '팀명')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 팀명 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '근무Shift')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 근무Shift 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '체크인상태')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 체크인상태 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '아이디')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 아이디 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '이름')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 이름 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '출근일시')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 출근일시 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '작업자정보상세')]", click=False, error_msg="센터별 출근 작업자 확인 탭 검색 후 작업자정보상세 항목명 미노출")



            # 16. <센터별 출근 작업자 확인 조회 초기화>

            # [초기화]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="센터별 출근 작업자 확인 탭 검색 후 초기화 버튼 미노출")

            # CC : 선택 / 센터 : 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//*[contains(text(), '선택')]", click=False, error_msg="센터별 출근 작업자 확인 탭 초기화 후 CC 선택란 선택 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//*[contains(text(), '선택')]", click=False, error_msg="센터별 출근 작업자 확인 탭 초기화 후 센터 선택란 선택 텍스트 미노출")

            # 계약구분 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//*[contains(text(), '전체')]", click=False, error_msg="센터별 출근 작업자 확인 탭 초기화 후 계약구분 선택란 전체 텍스트 미노출")

            # 출근업무파트 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//*[contains(text(), '전체')]", click=False, error_msg="센터별 출근 작업자 확인 탭 초기화 후 출근업무파트 선택란 전체 텍스트 미노출")

            # 팀명 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//*[contains(text(), '전체')]", click=False, error_msg="센터별 출근 작업자 확인 탭 초기화 후 팀명 선택란 전체 텍스트 미노출")

            # 근무Shift : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]//*[contains(text(), '전체')]", click=False, error_msg="센터별 출근 작업자 확인 탭 초기화 후 근무Shift 선택란 전체 텍스트 미노출")

            # 체크인상태 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[7]//*[contains(text(), '전체')]", click=False, error_msg="센터별 출근 작업자 확인 탭 초기화 후 체크인상태 선택란 전체 텍스트 미노출")

            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="센터별 출근 작업자 확인 탭 초기화 버튼 클릭 후 조회 결과가 없습니다 텍스트 미노출")



            # 17. <센터별 출근 작업자 작업상세내역 다운로드>

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 값 변경 : 상용직
            # 업무파트 변경 : HUB
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="센터별 출근 작업자 확인 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="센터별 출근 작업자 확인 탭 CC 항목 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="센터별 출근 작업자 확인 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="센터별 출근 작업자 확인 탭 센터 항목 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="센터별 출근 작업자 확인 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="센터별 출근 작업자 확인 탭 계약구분 항목 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="센터별 출근 작업자 확인 탭 출근업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="센터별 출근 작업자 확인 탭 출근업무파트 항목 HUB 미노출")

            # [검색]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="센터별 출근 작업자 확인 탭 검색 버튼 미노출")

            # [다운로드] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="센터별 출근 작업자 확인 탭 검색 후 다운로드 버튼 미노출")

            # 개인정보 다운로드 설정 사유 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[1]//input", click=False, send_keys_msg='테스트테스트테스트테스트', error_msg="센터별 출근 작업자 확인 탭 검색 후 다운로드 시 다운로드 사유 입력란 미노출")

            # 파일 비밀번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[2]//input", click=False, send_keys_msg='!testtest1', error_msg="센터별 출근 작업자 확인 탭 검색 후 다운로드 시 파일 비밀번호 입력란 미노출")

            # [등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary__btn')]", error_msg="센터별 출근 작업자 확인 탭 검색 후 다운로드 시 등록 버튼 미노출")



            # 18. <센터별 퇴근 작업자 확인 조회>

            # 센터별 퇴근 작업자 확인 클릭
            self.interact(by_type="XPATH", name="//*[contains(text(), '센터별 퇴근 작업자 확인')]", error_msg="센터별 퇴근 작업자 확인 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 값 변경 : 상용직
            # 출근업무파트 변경 : HUB
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="센터별 퇴근 작업자 확인 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="센터별 퇴근 작업자 확인 탭 CC 항목 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="센터별 퇴근 작업자 확인 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="센터별 퇴근 작업자 확인 탭 센터 항목 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="센터별 퇴근 작업자 확인 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="센터별 퇴근 작업자 확인 탭 계약구분 항목 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="센터별 퇴근 작업자 확인 탭 출근업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="센터별 퇴근 작업자 확인 탭 출근업무파트 항목 HUB 미노출")

            # [검색]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="센터별 퇴근 작업자 확인 탭 검색 버튼 미노출")

            # CC / 센터 / 계약구분 / 출근업무파트 / 팀명 / 근무 Shift / 아이디 / 이름 / 출근일시 / 퇴근일시 / 자동퇴근처리 / 작업자정보상세 항목 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, 'CC')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 CC 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '센터')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 센터 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '계약구분')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 계약구분 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '출근업무파트')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 출근업무파트 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '팀명')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 팀명 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '근무 Shift')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 근무 Shift 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '아이디')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 아이디 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '이름')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 이름 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '출근일시')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 출근일시 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '퇴근일시')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 퇴근일시 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '자동퇴근처리')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 자동퇴근처리 항목명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table-header')]//*[contains(@aria-label, '작업자정보상세')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 검색 후 작업자정보상세 항목명 미노출")



            # 19. <센터별 퇴근 작업자 확인 조회 초기화>

            # [초기화]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="센터별 퇴근 작업자 확인 탭 검색 후 초기화 버튼 미노출")

            # CC : 선택 / 센터 : 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//*[contains(text(), '선택')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 초기화 후 CC 선택란 선택 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//*[contains(text(), '선택')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 초기화 후 센터 선택란 선택 텍스트 미노출")

            # 계약구분 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//*[contains(text(), '전체')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 초기화 후 계약구분 선택란 전체 텍스트 미노출")

            # 출근업무파트 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//*[contains(text(), '전체')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 초기화 후 출근업무파트 선택란 전체 텍스트 미노출")

            # 팀명 : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//*[contains(text(), '전체')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 초기화 후 팀명 선택란 전체 텍스트 미노출")

            # 근무Shift : 전체
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[6]//*[contains(text(), '전체')]", click=False, error_msg="센터별 퇴근 작업자 확인 탭 초기화 후 근무Shift 선택란 전체 텍스트 미노출")

            # 퇴근Y : off
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'v-input--selection-controls__input')]//input")))

            is_disabled = element.get_attribute("aria-disabled")

            if is_disabled == "false":
                pass
            else:
                raise Exception("센터별 퇴근 작업자 확인 탭 초기화 후 퇴근Y 활성화 상태로 표시됨")

            # 날짜 : 오늘날짜
            # 날짜 클릭 후 표시된 날짜 추출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", error_msg="센터별 퇴근 작업자 탭에서 초기화 버튼 클릭 시 날짜 탭 버튼 미노출")
            time_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'v-btn v-date-picker-table__current v-btn--active v-btn--text v-btn--rounded theme--light accent')]//*[contains(@class, 'v-btn__content')]")))

            # 표시 된 날짜의 가장 오른쪽 하나의 숫자
            time_text = time_element.text
            time_text = str(time_text)[-1]

            # 오늘 날짜 가장 오른쪽 하나의 숫자
            today = datetime.today().strftime('%Y-%m-%d')
            today = str(today)[-1]

            # 비교
            if time_text == today:
                pass
            else:
                raise Exception("센터별 퇴근 작업자 탭에서 초기화 버튼 클릭 시 날짜가 오늘이 아님")

            # 날짜 선택창 닫기 위해 오늘 날짜 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-date-picker-table__current v-btn--active v-btn--text v-btn--rounded theme--light accent')]//*[contains(@class, 'v-btn__content')]", error_msg="센터별 퇴근 작업자 확인 탭 초기화 시 오늘 날짜 선택 미노출")

            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="센터별 퇴근 작업자 확인 탭 초기화 버튼 클릭 후 조회 결과가 없습니다 텍스트 미노출")



            # 20. <센터별 퇴근 작업자 작업상세내역 다운로드>

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 값 변경 : 상용직
            # 업무파트 변경 : HUB
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="센터별 퇴근 작업자 확인 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="센터별 퇴근 작업자 확인 탭 CC 항목 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="센터별 퇴근 작업자 확인 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="센터별 퇴근 작업자 확인 탭 센터 항목 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="센터별 퇴근 작업자 확인 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="센터별 퇴근 작업자 확인 탭 계약구분 항목 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="센터별 퇴근 작업자 확인 탭 출근업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'HUB')]", error_msg="센터별 퇴근 작업자 확인 탭 출근업무파트 항목 HUB 미노출")

            # [검색]버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="센터별 퇴근 작업자 확인 탭 검색 버튼 미노출")

            # [다운로드] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="센터별 퇴근 작업자 확인 탭 검색 후 다운로드 버튼 미노출")

            # 개인정보 다운로드 설정 사유 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[3]//input", click=False, send_keys_msg='테스트테스트테스트테스트', error_msg="센터별 퇴근 작업자 확인 탭 검색 후 다운로드 시 다운로드 사유 입력란 미노출")

            # 파일 비밀번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')])[4]//input", click=False, send_keys_msg='!testtest1', error_msg="센터별 퇴근 작업자 확인 탭 검색 후 다운로드 시 파일 비밀번호 입력란 미노출")

            # [등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default primary__btn')]", error_msg="센터별 퇴근 작업자 확인 탭 검색 후 다운로드 시 등록 버튼 미노출")

            # 다운받은 엑셀 파일 삭제
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".xlsx"):
                    file_path = os.path.join(folder_path, file_name)
                    os.remove(file_path)



            # LMS 어드민 탭 닫기
            self.driver.close()
            # 포커스를 LMS 모바일로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

            # 퇴근
            self.interact(by_type="XPATH", name="//*[contains(@class, 'work-btn v-btn v-btn--contained v-btn--fab v-btn--round theme--light v-size--default primary')]", error_msg="작업관리 모든 테스트 진행 후 퇴근 버튼 미노출")
            # 네
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dialog-btn ml-0 v-btn v-btn--contained theme--light v-size--default primary')]", error_msg="작업관리 모든 테스트 진행 후 퇴근 버튼 클릭 시 네 버튼 미노출")
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TaskManagement)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)