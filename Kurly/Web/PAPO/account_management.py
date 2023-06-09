import unittest
import re
import openpyxl
import xlwings as xw
import glob
import os
import pandas as pd
from datetime import datetime
from selenium.webdriver import Keys, ActionChains
from TestModule import testModule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class AccountManagement(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_05_계정관리(self):
        try:
            # 1. <관리자 계정 관리 조회>

            # LMS 어드민 URL 접속
            url = 'https://admin-lms.stg.kurly.com/?#/login'
            # url 이동
            self.driver.get(url)
            # 브라우저 최대화
            self.driver.maximize_window()

            # 아이디(lmstest01) 입력
            self.interact(by_type="XPATH", name="//input[@id='input-16' and @type='text' and @required='required']", click=False, send_keys_msg='lmstest01', error_msg="관리자 로그인중 아이디 입력란 미노출")

            # 비밀번호(q1w2e3r4!) 입력
            self.interact(by_type="XPATH", name="//input[@id='input-19' and @type='password' and @required='required']", click=False, send_keys_msg='q1w2e3r4!', error_msg="관리자 로그인중 비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large primary')]", error_msg="관리자 로그인중 로그인 버튼 미노출")

            # 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default primary--text')]", error_msg="관리자 로그인중 확인 버튼 미노출")

            # 계정관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '계정관리')]", error_msg="관리자 로그인 후 계정관리 탭 미노출")

            # 관리자 계정 관리 탭
            self.interact(by_type="XPATH", name="//*[contains(text(), '관리자 계정 관리')]", error_msg="관리자 계정 관리 탭 미노출")

            # CC 항목 값 변경 : 송파 CC
            # 센터 항목 값 변경 : 송파 냉장1
            # 부서 항목 값 변경 : FCS
            # 권한 항목 값 변경 : 마스터
            # 계정상태 항목 값 변경 : 정상
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="관리자 계정 관리 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="관리자 계정 관리 탭 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="관리자 계정 관리 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="관리자 계정 관리 탭 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="관리자 계정 관리 탭 부서 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'FCS')]", error_msg="관리자 계정 관리 탭 FCS 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="관리자 계정 관리 탭 권한 선택란 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-list-item__title') and contains(text(), '마스터')])[2]", error_msg="관리자 계정 관리 탭 마스터 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]", error_msg="관리자 계정 관리 탭 계정상태 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '정상')]", error_msg="관리자 계정 관리 탭 정상 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="관리자 계정 관리 탭 검색 버튼 미노출")

            # 이름 / 아이디 / 부서 / 권한 / CC / 센터 / 메모 / 접근 IP / 계정상태 / 초기화(초기화 버튼 노출) / 정보수정(수정버튼 노출)
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '이름')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 이름 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '아이디')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 아이디 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '부서')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 부서 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '권한')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 권한 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), 'CC')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 CC 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '센터')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 센터 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '메모')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 메모 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '접근 IP')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 접근 IP 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '계정상태')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 계정상태 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '초기화')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 초기화 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '정보수정')]", click=False, error_msg="관리자 계정 관리 탭 검색 후 정보수정 항목 미노출")



            # 2. <관리자 계정 관리 초기화>

            # [초기화] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="관리자 계정 관리 탭 검색 후 초기화 버튼 미노출")

            # 항목 값 옵션 초기화 확인
            #   - CC : 전체 / 센터 : 전체 / 부서 : 전체 / 권한 : 전체 / 계정상태 : 전체
            # 이름 : '이름' / 아이디 : '아이디'
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//div[contains(text(), '전체')]", click=False, error_msg="관리자 계정 관리 탭 초기화 후 CC 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//div[contains(text(), '전체')]", click=False, error_msg="관리자 계정 관리 탭 초기화 후 센터 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//div[contains(text(), '전체')]", click=False, error_msg="관리자 계정 관리 탭 초기화 후 부서 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//div[contains(text(), '전체')]", click=False, error_msg="관리자 계정 관리 탭 초기화 후 권한 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[5]//div[contains(text(), '전체')]", click=False, error_msg="관리자 계정 관리 탭 초기화 후 계정상태 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//*[contains(text(), '이름')]", click=False, error_msg="관리자 계정 관리 탭 초기화 후 이름 입력란 '이름' 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//*[contains(text(), '아이디')]", click=False, error_msg="관리자 계정 관리 탭 초기화 후 아이디 입력란 '아이디' 텍스트 미노출")

            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="관리자 계정 관리 탭 초기화 후 '조회 결과가 없습니다' 텍스트 미노출")



            # 3. <작업자 계정 관리 조회>

            # 작업자 계정 관리 탭
            self.interact(by_type="XPATH", name="//*[contains(text(), '작업자 계정 관리')]", error_msg="작업자 계정 관리 탭 미노출")

            # 계약구분 항목 값 변경 : 상용직
            # 계정상태 항목 값 변경 : 정상
            # 작업자 정보 항목 값 변경 : 아이디
            # 검색어 입력 : 'test'
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="작업자 계정 관리 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="작업자 계정 관리 탭 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="작업자 계정 관리 탭 계정상태 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '정상')]", error_msg="작업자 계정 관리 탭 정상 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="작업자 계정 관리 탭 작업자 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '아이디')]", error_msg="작업자 계정 관리 탭 아이디 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", click=False, send_keys_msg='test', error_msg="작업자 계정 관리 탭 검색어 입력란 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="작업자 계정 관리 탭 검색 버튼 미노출")

            # 이름 / 아이디 / 계약구분 / 계정상태 / 초기화
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '이름')]", click=False, error_msg="작업자 계정 관리 탭 검색 후 이름 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '아이디')]", click=False, error_msg="작업자 계정 관리 탭 검색 후 아이디 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '계약구분')]", click=False, error_msg="작업자 계정 관리 탭 검색 후 계약구분 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '계정상태')]", click=False, error_msg="작업자 계정 관리 탭 검색 후 계정상태 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '초기화')]", click=False, error_msg="작업자 계정 관리 탭 검색 후 초기화 항목 미노출")




            # 4. <작업자 계정 관리 초기화>

            # [초기화] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="작업자 계정 관리 탭 검색 후 초기화 버튼 미노출")

            # 항목 값 옵션 초기화 확인
            # - 계약구분 : 전체 / 계정상태 : 전체 / 작업자 정보 : 선택 /
            # 검색어 :'작업자 정보를 선택 후 입력해 주세요'
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//div[contains(text(), '전체')]", click=False, error_msg="작업자 계정 관리 탭 초기화 후 계약구분 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//div[contains(text(), '전체')]", click=False, error_msg="작업자 계정 관리 탭 초기화 후 계정상태 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//div[contains(text(), '선택')]", click=False, error_msg="작업자 계정 관리 탭 초기화 후 작업자 정보 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//*[contains(@placeholder, '작업자 정보를 선택 후 입력해 주세요')]", click=False, error_msg="작업자 계정 관리 탭 초기화 후 검색어 입력란 '작업자 정보를 선택 후 입력해 주세요' 텍스트 미노출")

            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="작업자 계정 관리 탭 초기화 후 '조회 결과가 없습니다' 텍스트 미노출")

            # LMS 어드민 탭 닫기
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
    suite = unittest.TestLoader().loadTestsFromTestCase(AccountManagement)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)