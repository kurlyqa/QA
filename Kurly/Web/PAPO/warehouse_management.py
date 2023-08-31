import unittest
import re
import schedule
import os
from datetime import datetime, timedelta
from TestModule import testModule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class WarehouseManagement(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_03_입고관리(self):
        try:
            # 1. <입고예정 내역 조회>

            # 파일 삭제 시 주소(환경변수 설정 필요!)
            folder_path = os.environ.get('FOLDER_PATH')

            # 담당자 로그인
            # 이동할 url주소
            url = 'https://partner.stg.kurly.com/#/stafflogin'

            # url 이동
            self.driver.get(url)

            # 브라우저 최대화
            self.driver.maximize_window()

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

            sleep(30)

            # 입고관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '입고관리')]", error_msg="MD 계정 로그인 후 입고 관리 미노출")

            try:
                # 입고예정
                self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link')]//*[contains(text(), '입고예정')]", error_msg="입고 관리탭 입고 예정 미노출")
            except:
                # 입고관리
                self.interact(by_type="XPATH", name="//*[contains(text(), '입고관리')]", error_msg="MD 계정 로그인 후 입고 관리 미노출")
                # 입고예정
                self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link')]//*[contains(text(), '입고예정')]", error_msg="입고 관리탭 입고 예정 미노출")

            # 검색 드롭박스 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')]", error_msg="입고 관리탭 입고 예정에서 검색 드롭박스 미노출")

            # 발주코드 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), '발주코드')]", error_msg="입고 관리탭 입고 예정에서 검색 드롭박스의 발주코드 옵션 미노출")

            try:
                # 발주확정 건 발주코드 검색
                with open('data.txt', 'r') as f:
                    new_order_code = f.read()
                # 발주코드 저장했던 txt파일 삭제
                if os.path.exists('data.txt'):
                    os.remove('data.txt')
            except:
                pass

            # 발주확정한 발주코드 불러온 발주 코드 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg=new_order_code, error_msg="입고 관리탭 '입고 예정'에서 저장된 발주코드 파일 없음 또는 검색어 입력란 미노출")

            # 입고예정일 종료일 캘린더 선택 후 +1일로 재설정
            # 현재 날짜 가져오기
            current_date = datetime.now()

            # 하루를 더한 날짜 계산
            next_date = current_date + timedelta(days=1)

            # 1일 뒤의 날짜 계산
            next_date = next_date.strftime("%Y/%m/%d")

            # 입고예정일과 발주일 확인을 위한 형태 변경
            converted_current_date = current_date.strftime("%Y-%m-%d")
            converted_next_date = datetime.strptime(next_date, "%Y/%m/%d").strftime("%Y-%m-%d")

            # 날짜 datepicker 기존값 클리어
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(@class, 'datepicker-input-class form-control')])[2]")))
            element.clear()

            # +1일 날짜 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'datepicker-input-class form-control')])[2]", click=False, send_keys_msg=next_date, error_msg="입고 관리탭 입고 예정에서 날짜 입력란 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="입고 관리탭 입고 예정에서 검색 버튼 미노출")

            # 발주확정 건과 발주코드 동일하게 노출
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{new_order_code}')]", click=False, error_msg="입고 관리탭 입고 예정에서 발주확정한 건과 발주코드가 다르거나 미노출")

            # 발주확정시 선택값 매핑되어 노출
            # - 공급사 / 발주코드 / 마스터코드/대체코드 / 상품명 / 발주수량(낱개) / 공급가구분 / 공급단가 / 입고예정일 : 발주일 + 1일 노출 / 상세
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH공급사')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 매핑된 공급사 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{new_order_code}')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 매핑된 발주코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH1111111114')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 매핑된 마스터코드/대체코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '[QA] SH자동화 테스트용 상품_사용금지')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 매핑된 상품명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '5')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 매핑된 발주수량 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '일반')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 매핑된 공급가구분 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '15,000원')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 매핑된 공급단가 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{converted_next_date}')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 매핑된 입고예정일 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn button-view-detail btn-primary') and contains(text(), '상세')]", click=False, error_msg="입고관리 탭에서 입고 예정에서 검색 후 상세 버튼 미노출")



            # 2. <입고예정 내역 상세 조회>

            # [상세] 버튼 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn button-view-detail btn-primary') and contains(text(), '상세')]", error_msg="입고관리 탭에서 입고 예정에서 검색 후 상세 버튼 미노출")

            # 상단영역 정보 확인시 발주확정 건과 선택값 동일하게 매핑되어 노출
            # - 발주코드 / 입고상태 : 입고예정으로 노출 / 공급사명 / 입고예정일 : 발주일 + 1일 노출 / 발주일 / 담당자정보 / 입고지 / 발주담당자 / 입고시간 / 경유센터
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{new_order_code}')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 발주코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '입고예정')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 입고상태 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH공급사')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 공급사명 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{converted_next_date}')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 입고예정일 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{converted_current_date}')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 발주일 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH담당자')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 담당자정보 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '평택상온')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 입고지 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '장세희')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 발주담당자 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '일반입고')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 입고시간 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '경유안함')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 매핑된 경유센터 미노출")

            # 거래명세서(입고용) / 발주서 / 닫기 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-1 btn-primary') and contains(text(), '거래명세서(입고용)')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 거래명세서(입고용) 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주서')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 발주서 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-1 btn-secondary')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 닫기 버튼 미노출")



            # 3. <입고예정 건 거래명세서 출력>

            # 하단 [거래명세서(입고용)] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-1 btn-primary') and contains(text(), '거래명세서(입고용)')]", error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 거래명세서(입고용) 버튼 미노출")

            # 다운받은 엑셀 파일 삭제
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".pdf"):
                    file_path = os.path.join(folder_path, file_name)
                    os.remove(file_path)



            # 4. <RMS 로그인>

            # RMS 로그인
            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # RMS PDA Web URL 접속
            url = 'https://m.rms.stg.kurly.com/#/login'
            self.driver.get(url)

            # 아이디 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[1]", click=False, send_keys_msg='seahui.jang', error_msg="아이디 입력란 미노출")

            # 비밀번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[2]", click=False, send_keys_msg='kurly12!', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--large theme--light primary')]", error_msg="로그인 버튼 미노출")

            # 우측 상단 사용자명 [장세희] 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--flat theme--dark')]", error_msg="RMS 로그인 후 우측 상단 사용자명 [장세희] 버튼 미노출")

            try:
                # 평택상온이 보일 경우 센터 변경 클릭 후 뒤로 가기
                self.interact(by_type="XPATH", name="//*[contains(text(), '평택상온')]", click=False, error_msg="")
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn theme--dark indigo')]", error_msg="")
                self.driver.back()
            except:
                # 평택상온이 안보일 경우 센터 변경 클릭 후 평택상온 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn theme--dark indigo')]", error_msg="RMS 로그인 후 우측 상단 [센터 변경] 버튼 미노출")
                self.interact(by_type="XPATH", name="//*[contains(text(), '평택상온')]", error_msg="RMS 로그인 후 센터 변경 선택 시 3CC 평택상온 버튼 미노출")

            # 입고영역 - [검수] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'home-btn v-btn v-btn--block v-btn--large theme--light')]//*[contains(text(),'검수')]", error_msg="RMS 센터 변경 후 검수 버튼 미노출")

            # RMS PDA Web 상단 타이틀 노출
            #   검수 - 평택상온
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-toolbar__content')]//span[contains(text(),'검수')]", click=False, error_msg="RMS PDA Web 상단 타이틀에서 '검수' 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-toolbar__content')]//span[contains(text(),'평택상온')]", click=False, error_msg="RMS PDA Web 상단 타이틀에서 '평택상온' 미노출")

            # 발주코드 스캔 입력 필드 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]", click=False, error_msg="RMS 검수 탭에서 발주코드 스캔 입력 필드 미노출")

            # [확인] 버튼 비활성화 되어 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary enter-button v-btn v-btn--block v-btn--bottom v-btn--disabled v-btn--flat theme--light')]", click=False, error_msg="RMS 검수 탭에서 확인 버튼 미노출")

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'primary enter-button v-btn v-btn--block v-btn--bottom v-btn--disabled v-btn--flat theme--light')]")))

            # input 태그의 비활성화 여부 확인하기
            is_disabled = select_element.get_attribute("disabled")

            if is_disabled:
                pass
            else:
                raise Exception("검수 탭에서 확인 버튼 활성화 상태로 노출")



            # 5. <RMS - 발주코드 스캔>

            # 발주코드 스캔 - 발주코드 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", click=False, send_keys_msg=new_order_code, error_msg="RMS 검수 탭에서 발주코드 스캔 입력 필드 미노출")

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="RMS 검수 탭에서 확인 버튼 미노출")

            # YYYY-MM-DD 입고 예정인 발주서 입니다. 담당자에게 확인해 주세요. 문구 노출
            # - 입고예정일 : 발주일 + 1일 노출
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{converted_next_date}')]", click=False, error_msg="RMS 검수 탭에서 발주코드 스캔 후 입고 예정일 미노출")

            # 발주코드 노출
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{new_order_code}')]", click=False, error_msg="RMS 검수 탭에서 발주코드 스캔 후 발주코드 미노출")

            # 상품코드 스캔 입력 필드 및 [확인] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]", click=False, error_msg="RMS 검수 탭에서 발주코드 스캔 후 상품코드 입력 필드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'primary enter-button v-btn v-btn--block v-btn--bottom v-btn--disabled v-btn--flat theme--light')]", click=False, error_msg="RMS 검수 탭에서 발주코드 스캔 후 확인 버튼 미노출")

            # 검수대기 상품 노출 (발주 3 / 입하 0 / 입하이슈 0)
            #    - 마스터코드 : SH1111111114
            #    - 상품명 : 자동화 TEST용 상품_SH
            self.interact(by_type="XPATH", name="//*[contains(@class, 'goods-code') and contains(text(), 'SH1111111114')]", click=False, error_msg="RMS 검수 탭에서 발주코드 스캔 후 마스터코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list__tile__sub-title goods-title') and contains(text(), '자동화 TEST용 상품_SH')]", click=False, error_msg="RMS 검수 탭에서 발주코드 스캔 후 상품명 미노출")



            # 6. <RMS - 검수대기 상품코드 스캔>

            # 상품코드 스캔 - 마스터코드 입력
            #   - 마스터코드 : SH1111111114
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", click=False, send_keys_msg="SH1111111114", error_msg="RMS 검수 탭에서 발주코드 스캔 후 상품코드 입력 필드 미노출")

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="RMS 검수 탭에서 발주코드 스캔 후 상품 코드 입력 시 확인 버튼 미노출")

            # [판매기한별 수량 추가] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '판매기한별 수량 추가')]", error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 미노출")

            # 판매기한 분류 - 평택상온 타이틀 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '판매기한 분류')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 판매기한 분류 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '평택상온')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 평택상온 텍스트 미노출")

            # 유통기한(default 선택) / 제조일자 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(text(),'유통기한')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 유통기한 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(),'제조일자')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 제조일자 버튼 미노출")

            # YYMMSS 입력필드 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > YYMMSS 입력필드 미노출")

            # 센터판매마감일 : YYYY-MM-DD 일까지 판매 가능 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'date-available-card v-card v-sheet theme--light')]//*[contains(text(), '센터판매마감일')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 센터판매마감일 텍스트 미노출")

            # 입하수량 입력 필드 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-input change-inspection-header-receiving-number-input mt-0 pa-0 v-text-field v-text-field--placeholder v-input--is-label-active v-input--is-dirty theme--light')]//input", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 입하수량 입력 필드 미노출")

            # [박스단위로 입력하기] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'box-input-button v-btn v-btn--block v-btn--flat theme--light')]//*[contains(text(), '박스단위로 입력하기')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 박스단위로 입력하기 미노출")

            # 하단 [취소하기] [저장하기] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'button-go-back v-btn v-btn--block v-btn--large theme--light error')]//*[contains(text(), '취소하기')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 취소하기 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'button-register v-btn v-btn--block v-btn--large theme--light primary')]//*[contains(text(), '저장하기')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 저장하기 버튼 미노출")



            # 7. <RMS - 판매기한별 수량 입력>

            # 판매기한 분류 - 평택상온 페이지

            # [제조일자] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(text(),'제조일자')]", error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 > 제조일자 버튼 미노출")

            # 테스트 당일 날짜 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-text-field__slot')]//input", click=False, send_keys_msg=converted_current_date, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 > YYMMSS 입력필드 미노출")

            # 입하수량 : 3 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-input change-inspection-header-receiving-number-input mt-0 pa-0 v-text-field v-text-field--placeholder v-input--is-label-active v-input--is-dirty theme--light')]//input", click=False, send_keys_msg=3, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 > YYMMSS 입력필드 미노출")

            # [저장하기] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'button-register v-btn v-btn--block v-btn--large theme--light primary')]//*[contains(text(), '저장하기')]", error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 > 저장하기 버튼 미노출")

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-card v-sheet theme--light')]//*[contains(text(), '확인')])[2]", error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 저장하기 > 확인 버튼 미노출")

            # [저장하기] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'button-register v-btn v-btn--block v-btn--large theme--light primary')]//*[contains(text(), '저장하기')]", error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 판매기한별 수량 추가 버튼 클릭 > 저장하기 > 확인 버튼 클릭 > 저장하기 버튼 미노출")

            # 입고예정일 날짜 노출
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{converted_next_date}')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 입고예정일 미노출")

            # 발주코드 노출
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{new_order_code}')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 발주코드 미노출")

            # 상품코드 입력 필드 및 [확인] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '상품코드 스캔')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 상품코드 입력 필드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 확인 버튼 미노출")

            # 확정대기 상품 노출 (발주 3 / 입하 3 / 입하이슈 0)
            #    - 마스터코드 : SH1111111114
            #    - 상품명 : 자동화 TEST용 상품_SH
            self.interact(by_type="XPATH", name="//*[contains(@class,'v-list__tile__content')]//span[contains(text(), '확정대기')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 확정대기 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class,'v-list__tile__content')]//span[contains(text(), 'SH1111111114')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 마스터코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class,'v-list__tile__sub-title goods-title') and contains(text(), '자동화 TEST용 상품_SH')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 상품명 미노출")



            # 8. <RMS - 확정대기 상품코드 스캔 및 검수확정>

            # [검수확정하기] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'v-btn__content') and contains(text(), '검수확정하기')]", error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 검수확정하기 버튼 미노출")

            # 검수담당자 - 싸인 입력(.)
            # <canvas> 요소에 싸인 추가
            canvas = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//canvas)[1]")))

            action_chains = ActionChains(self.driver)
            action_chains.move_to_element_with_offset(canvas, 10, 10).click().perform()

            # 공급담당자 - 싸인 입력(.)
            canvas = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//canvas)[2]")))

            action_chains = ActionChains(self.driver)
            action_chains.move_to_element_with_offset(canvas, 10, 10).click().perform()

            # [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class,'v-btn v-btn--large theme--light primary')]", error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 검수확정하기 > 확인 버튼 미노출")

            # 발주코드 스캔 화면 노출
            self.interact(by_type="XPATH", name="//*[contains(@class,'v-text-field__slot')]", click=False, error_msg="RMS 검수 > 발주코드 스캔 > 상품 코드 입력 후 검색 > 저장하기 > 검수확정하기 > 발주코드 스캔 화면 미노출")



            # 9. <입고데이터 생성(Jenkins batch)>

            # 개인 계정 OTP 입력이 필요하여, 수동으로 확인 필요



            # 10. <입고확정 내역 조회>

            # 9번 이후 진행 가능하여 수동으로 확인 필요

            # RMS 탭 닫기
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
        self.driver.quit()

## 이 클래스에서 정의된 테스트 메소드를 찾아서 실행하고, 그 결과를 출력하는 코드
# Python에서 모듈이 직접 실행될 때 (즉, 다른 모듈에서 import 되지 않고 직접 실행될 때) 해당 코드 블록을 실행하도록 하는 일종의 조건문
if __name__ == '__main__':
    # 이 클래스에서 정의된 테스트 메소드들을 자동으로 찾아주는 메소드를 사용하여 테스트 스위트(TestSuite) 객체를 생성
    suite = unittest.TestLoader().loadTestsFromTestCase(WarehouseManagement)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)