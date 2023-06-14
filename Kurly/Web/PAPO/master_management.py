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

class MasterManagement(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_04_마스터관리(self):
        try:
            # 1. <센터별 근무시간 관리 조회>

            # LMS 어드민 URL 접속
            url = 'https://admin-lms.stg.kurly.com/?#/login'
            # url 이동
            self.driver.get(url)
            # 브라우저 최대화
            self.driver.maximize_window()

            # 아이디(lmstest01) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[1]//input", click=False, send_keys_msg='lmstest01', error_msg="관리자 로그인중 아이디 입력란 미노출")

            # 비밀번호(q1w2e3r4!) 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class,'v-text-field__slot')])[2]//input", click=False, send_keys_msg='q1w2e3r4!', error_msg="관리자 로그인중 비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--contained theme--light v-size--large')]", error_msg="관리자 로그인중 로그인 버튼 미노출")

            # 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default primary--text')]", error_msg="관리자 로그인중 확인 버튼 미노출")

            # 마스터관리 탭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '마스터관리')]", error_msg="관리자 로그인 후 마스터관리 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 계약구분 항목 값 변경 : 상용직
            # 업무파트 항목 값 변경 : IB
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="센터별 근무시간 관리 조회 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="센터별 근무시간 관리 조회 탭 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="센터별 근무시간 관리 조회 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="센터별 근무시간 관리 조회 탭 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="센터별 근무시간 관리 조회 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '상용직')]", error_msg="센터별 근무시간 관리 조회 탭 상용직 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]", error_msg="센터별 근무시간 관리 조회 탭 업무파트 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'IB')]", error_msg="센터별 근무시간 관리 조회 탭 IB 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="센터별 근무시간 관리 조회 탭 검색 버튼 미노출")

            # CC / 센터 / 계약구분 / 업무파트 / 팀명 / 근무Shift / 휴게시간 / 연장근무가능시간 / [수정] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), 'CC')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 CC 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '센터')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 센터 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '계약구분')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 계약구분 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '업무파트')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 업무파트 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '팀명')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 팀명 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '근무Shift')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 근무Shift 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '휴게시간')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 휴게시간 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '연장근무가능시간')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 연장근무가능시간 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default')]//*[contains(text(), '수정')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 검색 후 수정 버튼 미노출")



            # 2. <센터별 근무시간 관리 초기화>

            # [초기화] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="센터별 근무시간 관리 조회 탭 검색 후 초기화 버튼 미노출")

            # 항목 값 옵션 초기화 확인
            #   - CC : 선택 / 센터 : 전체 / 계약구분 : 전체 / 업무파트 : 전체 / 팀명: '팀명을 입력해주세요'
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//div[contains(text(), '선택')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 초기화 후 CC 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//div[contains(text(), '전체')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 초기화 후 센터 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//div[contains(text(), '전체')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 초기화 후 계약구분 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//div[contains(text(), '전체')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 초기화 후 업무파트 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//*[contains(@placeholder, '팀명을 입력해주세요')]", click=False, error_msg="센터별 근무시간 관리 조회 탭 초기화 후 팀명 입력란 '팀명을 입력해주세요' 텍스트 미노출")

            # 조회결과 영역 초기화 상태 확인
    #### self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="센터별 근무시간 관리 조회 탭 초기화 후 조회 결과 영역 '조회 결과가 없습니다' 텍스트 미노출")



            # 3. <작업공정 관리 조회>

            # 작업공정 관리 탭
            self.interact(by_type="XPATH", name="//*[contains(text(), '작업공정 관리')]", error_msg="작업공정 관리 탭 미노출")

            # CC 항목 값 변경 : 송파CC
            # 센터 항목 값 변경 : 송파냉장1
            # 업무파트 항목 값 변경 : IB
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]", error_msg="작업공정 관리 탭 CC 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 CC')]", error_msg="작업공정 관리 탭 송파 CC 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]", error_msg="작업공정 관리 탭 센터 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), '송파 냉장1')]", error_msg="작업공정 관리 탭 송파 냉장1 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]", error_msg="작업공정 관리 탭 계약구분 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title') and contains(text(), 'IB')]", error_msg="작업공정 관리 탭 IB 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary v-btn v-btn--contained theme--light v-size--default')]", error_msg="작업공정 관리 탭 검색 버튼 미노출")

            # CC / 센터 / 업무파트 / 대분류 공정 / 소분류 공정 / 비고 / 상태 / [수정] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), 'CC')]", click=False, error_msg="작업공정 관리 탭 검색 후 CC 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '센터')]", click=False, error_msg="작업공정 관리 탭 검색 후 센터 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '업무파트')]", click=False, error_msg="작업공정 관리 탭 검색 후 업무파트 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '대분류 공정')]", click=False, error_msg="작업공정 관리 탭 검색 후 팀명 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '소분류 공정')]", click=False, error_msg="작업공정 관리 탭 검색 후 근무Shift 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '비고')]", click=False, error_msg="작업공정 관리 탭 검색 후 휴게시간 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'text-center')]//*[contains(text(), '상태')]", click=False, error_msg="작업공정 관리 탭 검색 후 연장근무가능시간 항목 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--contained theme--light v-size--default')]//*[contains(text(), '수정')]", click=False, error_msg="작업공정 관리 탭 검색 후 수정 버튼 미노출")



            # 4. <작업공정 관리 초기화>

            # [초기화] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'gray v-btn v-btn--contained theme--light v-size--default')]", error_msg="작업공정 관리 탭 검색 후 초기화 버튼 미노출")

            # 항목 값 옵션 초기화 확인
            #   - CC : 선택 / 센터 : 전체 / 업무파트 : 전체 / 대분류 공정 : 선택 / 소분류 공정: '공정명을 입력하세요.' / 비고 : 비고
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[1]//div[contains(text(), '선택')]", click=False, error_msg="작업공정 관리 조회 탭 초기화 후 CC 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[2]//div[contains(text(), '선택')]", click=False, error_msg="작업공정 관리 조회 탭 초기화 후 센터 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[3]//div[contains(text(), '전체')]", click=False, error_msg="작업공정 관리 조회 탭 초기화 후 업무파트 선택란 '전체' 텍스트 미노출")
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-select__selections')])[4]//div[contains(text(), '선택')]", click=False, error_msg="작업공정 관리 조회 탭 초기화 후 대분류 공정 선택란 '선택' 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//*[contains(@placeholder, '공정명을 입력하세요')]", click=False, error_msg="작업공정 관리 조회 탭 초기화 후 소분류 공정 입력란 '공정명을 입력하세요' 텍스트 미노출")

            # 조회결과 영역 초기화 상태 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-data-table__empty-wrapper')]//*[contains(text(), '조회 결과가 없습니다')]", error_msg="작업공정 관리 조회 탭 초기화 후 '조회 결과가 없습니다' 텍스트 미노출")



            # 5. <작업공정 관리_대분류 공정 등록>

            # [대분류 공정 관리] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mr-9 v-btn v-btn--contained theme--dark v-size--default primary')]", error_msg="작업공정 관리 탭 [대분류 공정 등록] 버튼 미노출")

            try:
                # 기존 대분류 공정에 !!!!! 있는지 확인
                self.interact(by_type="XPATH", name="//*[contains(@class, 'flex d-flex align-content-center justify-center align-self-stretch flex-wrap sm4') and contains(text(), '!!!!!')]", click=False, error_msg="작업공정 관리 탭 [대분류 공정 등록] 버튼 클릭 시 !!!!! 미노출")

                # 추가된 대분류 공정 : !!!!! 체크박스 선택
                self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input--selection-controls__ripple')])[1]", error_msg="작업공정 관리 탭 대분류 공정 등록 후 체크박스 버튼 미노출")

                # [-대분류 공정 삭제] 버튼 선택
                self.interact(by_type="XPATH", name="//*[contains(@class, 'mr-5 v-btn v-btn--contained theme--dark v-size--default secondary')]", error_msg="작업공정 관리 탭 [-대분류 공정 등록] 버튼 미노출")

                # 삭제 알림 팝업 노출
                #   - 대분류 공정 삭제 시 대분류에 속한 소분류 공정도 모두 삭제 처리 됩니다.
                #   - 삭제 하시겠습니까? [확인][취소]
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text card-text-content') and contains(text(), '대분류 공정 삭제 시 대분류에 속한 소분류 공정도 모두 삭제 처리 됩니다.')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 등록 삭제 시 '대분류 공정 삭제 시 대분류에 속한 소분류 공정도 모두 삭제 처리 됩니다.' 텍스트 미노출")
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text card-text-content') and contains(., '삭제 하시겠습니까?')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 등록 삭제 시 '삭제 하시겠습니까?' 텍스트 미노출")

                # 삭제 알림 팝업 [확인] 버튼 선택
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')]", error_msg="작업공정 관리 탭 대분류 공정 삭제 시 삭제 성공 팝업 [확인] 버튼 미노출")

                # 성공 팝업 노출
                #   - 대분류 공정 삭제가 완료되었습니다. [확인]
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text card-text-content') and contains(text(), '대분류 공정 삭제가 완료되었습니다.')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 삭제 성공 후 '대분류 공정 삭제가 완료되었습니다.' 텍스트 미노출")

                # 공정 삭제 성공 팝업 [확인] 선택
                self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')])[2]", error_msg="작업공정 관리 탭 대분류 공정 삭제 시 공정 삭제 성공 팝업 [확인] 버튼 미노출")

                # 대분류공정 삭제 확인
                try:
                    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'flex d-flex align-content-center justify-center align-self-stretch flex-wrap sm4') and contains(text(), '!!!!!')]")))
                    raise Exception("추가한 대분류 공정 삭제되지 않음")
                except:
                    pass
            except:
                pass

            # [+대분류 공정 등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mr-5 v-btn v-btn--contained theme--dark v-size--default primary')]", error_msg="작업공정 관리 탭 [+대분류 공정 등록] 버튼 미노출")

            # 대분류 공정명 입력 : !!!!!
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[3]", click=False, send_keys_msg='!!!!!', error_msg="작업공정 관리 탭 대분류 공정 등록 시 '대분류 공정명' 입력란 미노출")

            # 공정설명 입력 : 자동화테스트
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[4]", click=False, send_keys_msg='자동화테스트', error_msg="작업공정 관리 탭 대분류 공정 등록 시 '공정설명' 입력란 미노출")

            # [등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary__btn v-btn v-btn--contained theme--light v-size--default')]", error_msg="작업공정 관리 탭 대분류 공정 등록 시 등록 버튼 미노출")

            # 성공 팝업 노출
            #   - 공정등록 공정을 등록 하시겠습니까? [확인]
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text card-text-content') and contains(text(), '공정을 등록 하시겠습니까?')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 등록 성공 시 '공정을 등록 하시겠습니까?' 텍스트 미노출")

            # 성공 팝업 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')]", error_msg="작업공정 관리 탭 대분류 공정 등록 시 성공 팝업 [확인] 버튼 미노출")

            # 정상 처리 팝업 노출
            #   - 정상적으로 처리되었습니다 [확인]
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text card-text-content') and contains(text(), '정상적으로 처리되었습니다.')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 등록 성공 후 '정상적으로 처리되었습니다.' 텍스트 미노출")

            # 정상처리 팝업 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')])[2]", error_msg="작업공정 관리 탭 대분류 공정 등록 시 정상처리 팝업 [확인] 버튼 미노출")

            # '!!!!!' 대분류 공정이 상단에 추가 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'flex d-flex align-content-center justify-center align-self-stretch flex-wrap sm4') and contains(text(), '!!!!!')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 등록 성공 후 대분류 공정이 상단에 '!!!!!' 텍스트 미노출")



            # 6. <작업공정 관리_대분류 공정 삭제>

            # 추가된 대분류 공정 : !!!!!! 체크박스 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input--selection-controls__ripple')])[1]", error_msg="작업공정 관리 탭 대분류 공정 등록 후 체크박스 버튼 미노출")

            # [-대분류 공정 삭제] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mr-5 v-btn v-btn--contained theme--dark v-size--default secondary')]", error_msg="작업공정 관리 탭 [-대분류 공정 등록] 버튼 미노출")

            # 삭제 알림 팝업 노출
            #   - 대분류 공정 삭제 시 대분류에 속한 소분류 공정도 모두 삭제 처리 됩니다.
            #   - 삭제 하시겠습니까? [확인][취소]
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text card-text-content') and contains(text(), '대분류 공정 삭제 시 대분류에 속한 소분류 공정도 모두 삭제 처리 됩니다.')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 등록 삭제 시 '대분류 공정 삭제 시 대분류에 속한 소분류 공정도 모두 삭제 처리 됩니다.' 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text card-text-content') and contains(., '삭제 하시겠습니까?')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 등록 삭제 시 '삭제 하시겠습니까?' 텍스트 미노출")

            # 삭제 알림 팝업 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')]", error_msg="작업공정 관리 탭 대분류 공정 삭제 시 삭제 성공 팝업 [확인] 버튼 미노출")

            # 성공 팝업 노출
            #   - 대분류 공정 삭제가 완료되었습니다. [확인]
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-card__text card-text-content') and contains(text(), '대분류 공정 삭제가 완료되었습니다.')]", click=False, error_msg="작업공정 관리 탭 대분류 공정 삭제 성공 후 '대분류 공정 삭제가 완료되었습니다.' 텍스트 미노출")

            # 공정 삭제 성공 팝업 [확인] 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--block v-btn--flat v-btn--text theme--light v-size--default')]//*[contains(text(), '확인')])[2]", error_msg="작업공정 관리 탭 대분류 공정 삭제 시 공정 삭제 성공 팝업 [확인] 버튼 미노출")

            # 대분류공정 삭제 확인
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'flex d-flex align-content-center justify-center align-self-stretch flex-wrap sm4') and contains(text(), '!!!!!')]")))
                raise Exception("추가한 대분류 공정 삭제되지 않음")
            except:
                pass

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
    suite = unittest.TestLoader().loadTestsFromTestCase(MasterManagement)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)