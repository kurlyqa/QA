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
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class SettlementManagementReverse(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_04_정산관리_역발행(self):
        try:
            # 1. <공급사 반품 등록>

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

            # 발주관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주관리')]", error_msg="MD 계정 로그인 후 발주 관리 미노출")

            # 공급사 반품내역
            self.interact(by_type="XPATH", name="//*[contains(text(), '공급사 반품내역')]", error_msg="발주 관리에서 공급사 반품내역 미노출")

            # [+공급사 반품 등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(text(), '공급사 반품 등록')]", error_msg="발주 관리에서 [+공급사 반품 등록] 버튼 미노출")

            # 품질 확인 요청 코드 N(default) 값으로 선택되어 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '품질 확인 요청 코드')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 품질 확인 요청 코드 텍스트 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-control custom-control-inline custom-radio b-custom-control-sm')]//*[contains(text(), 'N')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> N 버튼 미노출")



            # 2. <반품 상품 추가>

            # [+ 상품 추가] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(text(), '상품 추가')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> [+ 상품 추가] 버튼 미노출")

            # 상품 추가 팝업 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'modal-content')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 추가 팝업 미노출")

            # 상품명검색 : [QA] SH자동화
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'form-control')])[4]", click=False, send_keys_msg="[QA] SH자동화", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품명 입력란 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 추가 팝업 미노출")

            # 상품리스트에 [QA] SH자동화 테스트용 상품_사용금지 상품 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '[QA] SH자동화 테스트용 상품_사용금지')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 상품리스트에 [QA] SH자동화 테스트용 상품_사용금지 상품 미노출")

            # 상품등록시 정보 매핑되어 노출
            # - 상품상태 / 공급사 / 마스터코드 / 상품명 / 중량 / 단위 / 과면세 / 단가 / 담당MD / 담당AMD
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주가능')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 상품상태 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH공급사 (VD4360)')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 공급사 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH1111111114')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 마스터코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '[QA] SH자동화 테스트용 상품_사용금지')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 상품명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '1 (1)')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 중량 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'EA')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 단위 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '과세')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 과면세 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '3,000')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 단가 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '장세희')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 담당MD 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '장세희')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품 검색 -> 담당AMD 미노출")



            # 3. <반품 상품 추가>

            # 리스트에서 해당 상품 체크박스 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'checkbox_margin modal-checkbox custom-control custom-checkbox')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 체크박스 미노출")

            # 우측 하단 [추가] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '추가')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 추가 버튼 미노출")

            # 추가된 상품 리스트에 노출
            # - 공급사 / 마스터코드 / 상품명 / 반품센터 / 반품요청수량 / 반품사유 / 공급가 / 과세유형 / 총 공급가(VAT 제외) / 반품재고정보
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH공급사')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 공급사 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH1111111114')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 마스터코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '[QA] SH자동화 테스트용 상품_사용금지')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '장지냉장')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품센터 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '전량')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품요청수량 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '선택')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품사유 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '일반 - 3,000원')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 공급가 미노출")
            self.interact(by_type="XPATH", name="//span[contains(text(), '과세')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 과세유형 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '미정')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 총 공급가(VAT 제외) 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control form-control-sm')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품재고정보 미노출")



            # 4. <반품 사유 선택>

            # 반품사유 드롭박스 선택
            element1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'custom-select')])[2]")))
            element1.click()

            # - 상품하자 선택
            element2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '상품하자')]")))

            # Select 클래스를 사용하여 드롭다운 목록 다루기
            select = Select(element1)
            select.select_by_visible_text('상품하자')



            # 5. <반품 승인 담당자 입력>

            # 반품 승인 담당자 선택
            # 1번째 드롭박스 : 장세희(qa-md2)선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 승인 담당자 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), '장세희(qa_md2)')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 승인 담당자1 장세희(qa_md2) 미노출")

            # 2번째 드롭박스 : 김현우(QA_MD) 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')])[2]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 승인 담당자 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), '김현우(QA_MD)')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 승인 담당자2 김현우(QA_MD) 미노출")

            # [반품 등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '반품 등록')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 등록 버튼 미노출")

            # 확인 팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 등록 -> 확인 버튼 미노출")

            # 공급사 반품내역 List로 이동되며 토스트 팝업 노출
            # - 성공적으로 저장되었습니다.
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 등록 -> '성공적으로 저장되었습니다.' 토스트 팝업  미노출")

            # 상태 : MD 승인대기로 노출됨
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'custom-table-striped')])[1]//*[contains(text(), 'MD 승인대기')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 등록 -> 상태 : MD 승인대기 미노출")

            # 반품코드 노출
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "((//*[contains(@class, 'custom-table-striped')])[1]//span)[2]")))
            return_code = element.text

            self.interact(by_type="XPATH", name="((//*[contains(@class, 'custom-table-striped')])[1]//span)[2]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 반품 등록 -> 반품 코드 미노출")

            # 반품요청일 당일 노출
            current_date = datetime.now()

            # 날짜 비교를 위한 형태 변경
            converted_current_date = current_date.strftime("%Y-%m-%d")

            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "((//*[contains(@class, 'custom-table-striped')])[1]//span)[9]")))
            return_date = element.text

            if converted_current_date == return_date:
                pass
            else:
                raise Exception("반품요청일이 오늘 날짜가 아님")



            # 6. <MD 승인 대기 상태 승인>

            # 등록한 반품 코드 존재
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "((//*[contains(@class, 'custom-table-striped')])[1]//span)[2]")))
            added_code = element.text

            if return_code == added_code:
                pass
            else:
                raise Exception("공급사 반품 등록 시 반품 코드가 다름")

            # 상품명검색 : [QA] SH자동화
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg="[QA] SH자동화", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상품명 입력란 미노출")

            # 상태 : MD 승인대기 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')])[2]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 상태 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), 'MD 승인대기')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> MD 승인대기 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 버튼 미노출")

            # 리스트의 상품 [상세] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn button-view-detail btn-primary') and contains(text(), '상세')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 버튼 미노출")

            # 하단에 [저장][승인][반품 취소][닫기] 버튼 노출
            # - 반품 승인담당자 계정에만 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '저장')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 저장 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-outline-primary') and contains(text(), '반품 취소')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 반품 취소 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-outline-primary') and contains(text(), '닫기')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 닫기 버튼 미노출")

            # 토스트 팝업 노출
            # - 성공적으로 저장되었습니다.
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '저장')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 저장 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 승인 -> 확인 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 승인 -> 버튼 미노출")

            # [승인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '승인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 승인 버튼 미노출")

            # 확인 팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 승인 -> 확인 버튼 미노출")

            # 공급사 반품 상세 상단영역 상태 - LC 승인대기 상태 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), 'LC 승인대기')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 승인 -> LC 승인대기 텍스트 미노출")



            # 7. <LC 승인 대기 상태 승인>

            # MD 계정 로그아웃
            self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link') and contains(text(), 'Logout')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 등록 -> 상품 추가 -> 검색 -> 상세 진입 -> 승인 -> 로그아웃 버튼 미노출")

            # LC 계정 로그인
            #  - ID 입력 : qa_lc2@kurlycorp.com
            #  - 비밀번호입력 : kurly12!

            # 아이디(qa_lc2@kurlycorp.com) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, send_keys_msg='qa_lc2@kurlycorp.com', error_msg="아이디 입력란 미노출")

            # 비밀번호(kurly12!) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputPassword')]", click=False, send_keys_msg='kurly12!', error_msg="비밀번호 입력란 미노출")

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

            # 발주관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주관리')]", error_msg="LC 계정 로그인 후 발주 관리 미노출")

            # 공급사 반품내역
            self.interact(by_type="XPATH", name="//*[contains(text(), '공급사 반품내역')]", error_msg="발주 관리 -> 공급사 반품내역 미노출")

            # 상품명검색 : [QA] SH자동화
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg="[QA] SH자동화", error_msg="발주 관리 -> 공급사 반품내역 -> 상품명 입력란 미노출")

            # 상태 : LC 승인대기 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')])[2]", error_msg="발주 관리 -> 공급사 반품내역 -> 상태 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), 'LC 승인대기')]", error_msg="발주 관리 -> 공급사 반품내역 -> 상태 선택란에서 LC 승인대기 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 버튼 미노출")

            # 리스트의 상품 [상세] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn button-view-detail btn-primary') and contains(text(), '상세')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 버튼 미노출")

            # [승인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '승인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 진입 -> 승인 버튼 미노출")

            # 확인 팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 진입 -> 승인 -> 확인 버튼 미노출")

            # 토스트 팝업 노출
            # - 성공적으로 저장되었습니다.
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 진입 -> 승인 -> 버튼 미노출")

            # 공급사 반품 상세 상단영역 상태 - IM 확인대기 상태 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), 'IM 확인대기')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 진입 -> 승인 -> IM 확인대기 텍스트 미노출")



            # 8. <IM 확인 대기 상태 확인>

            # LC 계정 로그아웃
            self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link') and contains(text(), 'Logout')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 진입 -> 승인 -> 로그아웃 버튼 미노출")

            # IM 계정 로그인
            #  - ID 입력 : qa_im2@kurlycorp.com
            #  - 비밀번호입력 : kurly12!

            # 아이디(qa_im2@kurlycorp.com) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, send_keys_msg='qa_im2@kurlycorp.com', error_msg="아이디 입력란 미노출")

            # 비밀번호(kurly12!) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputPassword')]", click=False, send_keys_msg='kurly12!', error_msg="비밀번호 입력란 미노출")

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

            # 발주관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주관리')]", error_msg="LC 계정 로그인 후 발주 관리 미노출")

            # 공급사 반품내역
            self.interact(by_type="XPATH", name="//*[contains(text(), '공급사 반품내역')]", error_msg="발주 관리 -> 공급사 반품내역 미노출")

            # 상품명검색 : [QA] SH자동화
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg="[QA] SH자동화", error_msg="발주 관리 -> 공급사 반품내역 -> 상품명 입력란 미노출")

            # 상태 : IM 확인대기 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')])[2]", error_msg="발주 관리 -> 공급사 반품내역 -> 상태 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), 'IM 확인대기')]", error_msg="발주 관리 -> 공급사 반품내역 -> 상태 선택란에서 IM 확인대기 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 버튼 미노출")

            # 리스트의 상품 [상세] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn button-view-detail btn-primary') and contains(text(), '상세')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 버튼 미노출")

            # 회수방문일 당일 입력 : yyyy/mm/ss 형태
            converted_current_date = current_date.strftime("%Y/%m/%d")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'datepicker-input-class form-control')]", click=False, send_keys_msg=converted_current_date, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 회수방문일 입력란 미노출")

            # 반품요청수량 : 5
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'form-control')])[2]", click=False, send_keys_msg=5, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 반품요청수량 입력란 미노출")

            # [확인 완료] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '확인 완료')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 버튼 미노출")

            # 확인 팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 확인 버튼 미노출")

            # 토스트 팝업 노출
            # - 성공적으로 저장되었습니다.
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> '성공적으로 저장되었습니다.' 토스트 팝업 미노출")

            # 공급사 반품 상세 상단영역 상태 - 공급사 확인대기 상태 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '공급사 확인대기')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 공급사 확인대기 텍스트 미노출")



            # 9. <공급사 확인 대기 상태 확인>

            # IM 계정 로그아웃
            self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link') and contains(text(), 'Logout')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 로그아웃 버튼 미노출")

            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # 공급사 URL 접속
            url = 'https://partner.stg.kurly.com/#/login'
            self.driver.get(url)

            # 공급사 계정 로그인
            #  - ID 입력 : VD4360.01
            #  - 비밀번호입력 : kurly12!@

            # 아이디(VD4360.01) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, send_keys_msg='VD4360.01', error_msg="아이디 입력란 미노출")

            # 비밀번호(kurly12!@) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputPassword')]", click=False, send_keys_msg='kurly12!@', error_msg="비밀번호 입력란 미노출")

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

            # 발주관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주관리')]", error_msg="공급사 계정 로그인 후 발주 관리 미노출")

            # 공급사 반품내역
            self.interact(by_type="XPATH", name="//*[contains(text(), '공급사 반품내역')]", error_msg="발주 관리 -> 공급사 반품내역 미노출")

            # 상품명검색 : [QA] SH자동화
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg="[QA] SH자동화", error_msg="발주 관리 -> 공급사 반품내역 -> 상품명 입력란 미노출")

            # 상태 : 공급사 확인대기 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')])[2]", error_msg="발주 관리 -> 공급사 반품내역 -> 상태 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), '공급사 확인대기')]", error_msg="발주 관리 -> 공급사 반품내역 -> 상태 선택란에서 공급사 확인대기 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 버튼 미노출")

            # 리스트의 상품 [상세] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn button-view-detail btn-primary') and contains(text(), '상세')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 버튼 미노출")

            # 회수 담당자 연락처 : 01011111111 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg="01011111111", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 -> 회수 담당자 연락처 입력란 미노출")

            # [확인 완료] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '확인 완료')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 버튼 미노출")

            # 확인 팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 확인 버튼 미노출")

            # 토스트 팝업 노출
            # - 성공적으로 저장되었습니다.
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> '성공적으로 저장되었습니다.' 토스트 팝업 미노출")

            # 공급사 반품 상세 상단영역 상태 - 회수대기 상태 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '회수대기')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 회수대기 텍스트 미노출")

            # 하단 버튼 [반품 거래명세서][저장][닫기] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '저장')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 저장 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-outline-primary') and contains(text(), '반품 거래명세서')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 반품 거래명세서 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-outline-primary') and contains(text(), '닫기')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 닫기 버튼 미노출")



            # 10. <반품 거래 명세서>

            # [반품 거래명세서] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-outline-primary') and contains(text(), '반품 거래명세서')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 반품 거래명세서 버튼 미노출")

            # 다운받은 엑셀 파일 삭제
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".xlsx"):
                    file_path = os.path.join(folder_path, file_name)
                    os.remove(file_path)



            # 11. <회수 대기 상태 반품 완료>

            # 공급사 계정 로그아웃
            self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link') and contains(text(), 'Logout')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 진입 -> 승인 -> 로그아웃 버튼 미노출")

            # 원래 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

            # IM 계정 로그인
            #  - ID 입력 : qa_im2@kurlycorp.com
            #  - 비밀번호입력 : kurly12!

            # 아이디(qa_im2@kurlycorp.com) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, send_keys_msg='qa_im2@kurlycorp.com', error_msg="아이디 입력란 미노출")

            # 비밀번호(kurly12!) 입력
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputPassword')]", click=False, send_keys_msg='kurly12!', error_msg="비밀번호 입력란 미노출")

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

            # 발주관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주관리')]", error_msg="LC 계정 로그인 후 발주 관리 미노출")

            # 공급사 반품내역
            self.interact(by_type="XPATH", name="//*[contains(text(), '공급사 반품내역')]", error_msg="발주 관리 -> 공급사 반품내역 미노출")

            # 상품명검색 : [QA] SH자동화
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg="[QA] SH자동화", error_msg="발주 관리 -> 공급사 반품내역 -> 상품명 입력란 미노출")

            # 상태 : 회수대기 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')])[2]", error_msg="발주 관리 -> 공급사 반품내역 -> 상태 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), '회수대기')]", error_msg="발주 관리 -> 공급사 반품내역 -> 상태 선택란에서 회수대기 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 버튼 미노출")

            # 리스트의 상품 [상세] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn button-view-detail btn-primary') and contains(text(), '상세')]", error_msg="발주 관리 -> 공급사 반품내역 -> 검색 -> 상세 버튼 미노출")

            # 하단 버튼 [반품 거래명세서][닫기] 버튼 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '반품 거래명세서')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 반품 거래명세서 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '닫기')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 닫기 버튼 미노출")

            # [반품 완료] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-2 btn-primary') and contains(text(), '반품 완료')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 반품 완료 버튼 미노출")

            # 확인 팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 확인 버튼 미노출")

            # 토스트 팝업 노출
            # - 성공적으로 저장되었습니다.
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> '성공적으로 저장되었습니다.' 토스트 팝업 미노출")

            # 공급사 반품 상세 상단영역 상태 - 완료 상태 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '완료')]", click=False, error_msg="발주 관리 -> 공급사 반품내역 -> 공급사 반품 상세 -> 확인 완료 -> 완료 텍스트 미노출")

            # 담당자 탭 닫기
            self.driver.close()

            # 포커스를 담당자 url(stafflogin)로 변경
            self.driver.switch_to.window(self.driver.window_handles[0])

            # 공급자 탭 닫기
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
    suite = unittest.TestLoader().loadTestsFromTestCase(SettlementManagementReverse)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)