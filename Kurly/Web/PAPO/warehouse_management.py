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
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class WarehouseManagement(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_03_입고관리(self):
        try:
            # 파일 삭제 시 주소 ( 각 PC마다 변경해야 함 )
            folder_path = "/Users/122d6424/Git/Kurly/Web/PAPO"

            # 1. <입고예정 내역 조회>

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

            # 입고관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '입고관리')]", error_msg="MD 계정 로그인 후 입고 관리 미노출")

            # 입고예정
            self.interact(by_type="XPATH", name="//*[contains(@class, 'nav-link')]//*[contains(text(), '입고예정')]", error_msg="입고 관리탭 입고 예정 미노출")

            # 검색 드롭박스 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')]", error_msg="입고 관리탭 입고 예정에서 검색 드롭박스 미노출")

            # 발주코드 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//*[contains(text(), '발주코드')]", error_msg="입고 관리탭 입고 예정에서 검색 드롭박스 미노출")

            # 발주확정 건 발주코드 검색
            with open('data.txt', 'r') as f:
                new_order_code = f.read()

            # 발주확정한 발주코드 불러온 발주 코드 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg=new_order_code, error_msg="입고 관리탭 입고 예정에서 검색어 입력란 미노출")

            # 발주코드 저장했던 txt파일 삭제
            if os.path.exists('data.txt'):
                os.remove('data.txt')

            # 입고예정일 종료일 캘린더 선택 후 +1일로 재설정
            # 현재 날짜 가져오기
            current_date = datetime.now()

            # 하루를 더한 날짜 계산
            next_date = current_date + timedelta(days=1)

            # 1일 뒤의 날짜 계산
            next_date = next_date.strftime("%Y/%m/%d")

            # 입고예정일과 발주일 확인을 위한 형태 변경
            converted_current_date = current_date.strftime("%Y-%m-%d")
            converted_next_date = next_date.strftime("%Y-%m-%d")

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
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn mr-1 btn-primary') and contains(text(), '발주서')]", click=False, error_msg="입고관리 -> 입고예정 -> 검색 -> 입고상세 후 발주서 버튼 미노출")
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
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input v-text-field v-input--is-label-active v-input--is-dirty theme--light')]//input)[1]", click=False, send_keys_msg='seahui.jang', error_msg="아이디 입력란 미노출")

            # 비밀번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input v-text-field v-input--is-label-active v-input--is-dirty theme--light')]//input)[2]", click=False, send_keys_msg='kurly12!', error_msg="비밀번호 입력란 미노출")

            # 로그인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn v-btn--block v-btn--large theme--light primary')]", error_msg="로그인 버튼 미노출")


            # RMS PDA Web 로그인
            # - https://m.rms.stg.kurly.com/#/login
            # - ID 입력 : seahui.jang
            # - 비밀번호 입력 : kurly12!

            # 우측 상단 사용자명 [장세희] 선택

            # 우측 상단 [센터 변경] 버튼 선택

            # 3CC 평택 상온 선택

            # 입고영역 - [검수] 버튼 선택




            # RMS PDA Web 상단 타이틀 노출
            #   검수 - 평택상온

            # 발주코드 스캔 입력 필드 노출

            # [확인] 버튼 비활성화 되어 노출







            # 5. <RMS - 발주코드 스캔>

            # RMS - 발주코드 스캔




            # 발주코드 스캔 - 발주코드 입력

            # [확인] 버튼 선택





            # 2023-06-26 입고 예정인 발주서 입니다. 담당자에게 확인해 주세요. 문구 노출
            # - 입고예정일 : 발주일 + 1일 노출

            # 발주코드 노출

            # 상품코드 스캔 입력 필드 및 [확인] 버튼 노출

            # 검수대기 상품 노출 (발주 3 / 입하 0 / 입하이슈 0)
            #    - 마스터코드 : SH1111111114
            #    - 상품명 : 자동화 TEST용 상품_SH






            # 6. <RMS - 검수대기 상품코드 스캔>

            # RMS - 검수대기 상품코드 스캔





            # 상품코드 스캔 - 마스터코드 입력
            #   - 마스터코드 : SH1111111114
            # [확인] 버튼 선택
            # [판매기한별 수량 추가] 버튼 선택





            # 판매기한 분류 - 평택상온 타이틀 노출

            # 유통기한(default 선택) / 제조일자 버튼 노출

            # YYMMSS 입력필드 노출

            # 센터판매마감일 : YYYY-MM-DD 일까지 판매 가능 노출

            # 입하수량 입력 필드 노출

            # [박스단위로 입력하기] 버튼 노출

            # 하단 [취소하기] [저장하기] 버튼 노출
















            # 7. <RMS - 판매기한별 수량 입력>

            # RMS - 판매기한별 수량 입력






            # 판매기한 분류 - 평택상온 페이지

            # [제조일자] 버튼 선택

            # 테스트 당일 날짜 입력

            # 입하수량 : 3 입력

            # [저장하기] 버튼 선택

            # [확인] 버튼 선택

            # [저장하기] 버튼 선택








            # 입고예정일 날짜 노출

            # 발주코드 노출

            # 상품코드 입력 필드 및 [확인] 버튼 노출

            # 확정대기 상품 노출 (발주 3 / 입하 3 / 입하이슈 0)
            #    - 마스터코드 : SH1111111114
            #    - 상품명 : 자동화 TEST용 상품_SH








            # 8. <RMS - 확정대기 상품코드 스캔 및 검수확정>

            # RMS - 확정대기 상품코드 스캔 및 검수확정



            # 상품코드 스캔 - 마스터코드 입력
            #   - 마스터코드 : SH1111111114

            # [확인] 버튼 선택

            # [검수확정하기] 버튼 선택

            # 검수담당자 - 싸인 입력(.)

            # 공급담당자 - 싸인 입력(.)

            # [확인] 버튼 선택



            # 발주코드 스캔 화면 노출

            # 입고확정 여부는 파트너 포탈에서 확인





            # 9. <입고데이터 생성(Jenkins batch)>

            # 개인 계정 OTP 입력이 필요하여, 수동으로 확인 필요



            # 10. <입고확정 내역 조회>

            # 입고확정 내역 조회






            # 담당자 로그인
            #  - ID 입력 : qa_md2@kurlycorp.com
            #  - 비밀번호입력 : 1234

            # 입고관리

            # 입고확정내역

            # 검색 드롭박스 발주코드 선택

            # 검수확정 건 발주코드 검색

            # 입고예정일 종료일 캘린더 선택 후 +1일로 재설정

            # [검색] 버튼 선택












            # 발주확정 건과 발주코드 동일하게 노출

            # 발주확정시 선택값 매핑되어 노출
            # - 발주코드 / 입고일 / 입고상태 / 공급사 / 마스터코드/대체코드/ 상품명 /  발주수량 /  이슈수량 / 입고확정수량 / 공급가구분 / 공급단가 / 과세여부 / 입고확정공급가(VAT제외) / 입고확정일 / 상세

            # 입고상태 : 입고확정으로 노출


























            # 이동할 url주소
            url = 'https://partner.stg.kurly.com/#/stafflogin'

            # url 이동
            self.driver.get(url)

            # 브라우저 최대화
            self.driver.maximize_window()

            # MD 계정 로그인
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

            # 1. <발주 상품 조회>

            # 상품 등록 상태(발주가능, 사용여부 Y)

            # 발주관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주관리')]", error_msg="MD 계정 로그인 후 발주 관리 미노출")

            # 발주등록 버튼 노출 확인
            self.interact(by_type="XPATH", name="//*[contains(@id, 'viewPurchaseOrder')]", click=False, error_msg="발주관리 탭에서 발주등록 버튼 미노출")

            # 상품 검색 : [QA] SH자동화
            self.interact(by_type="XPATH", name="//*[contains(@class,'form-control')]", click=False, send_keys_msg='[QA] SH자동화', error_msg="발주관리 탭에서 상품 검색어 입력란 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="발주관리 탭에서 검색 버튼 미노출")

            # 발주등록 리스트 '[QA] SH자동화 테스트용 상품_사용금지' 상품 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '[QA] SH자동화 테스트용 상품_사용금지')]", click=False, error_msg="발주관리 탭에서 검색 후 '[QA] SH자동화 테스트용 상품_사용금지' 텍스트 미노출")

            # 상품등록시 설정한 값 매핑되어 노출
            #  - 공급사 / 마스터코드 / 상품명 / 공급단가(이벤트) / 판매방법 / 담당MD / 발주담당
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH공급사')]", click=False, error_msg="발주관리 탭에서 검색 후 매핑된 공급사 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH1111111114')]", click=False, error_msg="발주관리 탭에서 검색 후 매핑된 마스터코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '3000')]", click=False, error_msg="발주관리 탭에서 검색 후 매핑된 공급단가 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '후판매')]", click=False, error_msg="발주관리 탭에서 검색 후 매핑된 담당MD 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '장세희')]", click=False, error_msg="발주관리 탭에서 검색 후 매핑된 발주담당 미노출")



            # 2. <상품 발주등록>

            # 해당 상품 체크박스 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'list-checkbox custom-control custom-checkbox')]", error_msg="발주관리 탭에서 상품 체크박스 미노출")

            # [발주등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@id, 'viewPurchaseOrder')]", error_msg="발주관리 탭에서 발주등록 버튼 미노출")

            # 선택한 상품 리스트 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주정보')]", click=False, error_msg="발주관리 탭에서 발주등록 후 '발주정보' 텍스트 미노출(리스트 미노출)")



            # 3. <발주등록 상세 데이터 입력>

            # 발주 CC 선택란 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-select')]", error_msg="발주관리 탭 발주등록 페이지에서 발주 CC 선택란 미노출")

            # 발주CC : 3CC 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-select')]", click=False, send_keys_msg='3CC(평택)', error_msg="발주관리 탭 발주등록 페이지에서 발주 CC 선택란 3CC(평택) 미노출")

            # 상품 list 1row 발주수량 입력 : 5
            self.interact(by_type="XPATH", name="(//*[contains(@id, '0_0')])[1]", click=False, send_keys_msg='5', error_msg="발주관리 탭 발주등록 페이지에서 발주수량 입력란 미노출")

            # [발주그룹 & 발주서 등록] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주그룹 & 발주서 등록')]", error_msg="발주관리 탭 발주등록 페이지에서 발주그룹 & 발주서 등록 버튼 미노출")

            # 확인팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주관리 탭 발주등록 페이지에서 발주그룹 & 발주서 등록 버튼 클릭 후 확인팝업 미노출")

            # 안내팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="발주관리 탭 발주등록 페이지에서 발주그룹 & 발주서 등록 버튼 클릭 후 안내팝업 미노출")

            # 발주서내역 확인시 발주등록시 선택한 항목값 매핑되어 노출
            # - 상태 / 발주코드 발주구분 / 입고예정일 / 입고지 / 공급사 / 마스터코드 / 상품명 / 수량 총수량 / 유통기한(소비기한) 제조일자 / 판매방법 출고방법 / 담당MD 담당AMD 발주자 발주일 데이터 노출 확인

            # 현재 날짜 가져오기
            current_date = datetime.now()

            # 하루를 더한 날짜 계산
            next_date = current_date + timedelta(days=1)

            # 날짜 출력
            current_date = current_date.strftime("%Y-%m-%d")
            next_date = next_date.strftime("%Y-%m-%d")

            self.interact(by_type="XPATH", name="//*[contains(text(), '발주생성')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '정규발주')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 발주코드 발주구분 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{next_date}')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 입고예정일 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '평택상온')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 입고지 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH공급사')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 공급사 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH1111111114')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 마스터코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '[QA] SH자동화 테스트용 상품_사용금지')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 상품명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '5')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 수량 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '후판매')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 판매방법 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '장세희')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 담당MD 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{current_date}')]", click=False, error_msg="발주관리 탭에서 발주그룹 & 발주서 등록 후 매핑된 발주일 미노출")

            # 상태 : 발주생성 , 발주코드 : 임의생성
            # 새로 생성된 발주코드
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'custom-table-striped')]//span")))
            new_order_code = element.text

            # 새로 생성된 발주코드
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'custom-table-striped')]//span)[3]")))
            old_order_code = element.text

            # 발주코드 확인
            # 비교
            if new_order_code == old_order_code:
                raise Exception("발주등록 후 발주코드가 이전 발주코드와 일치함")
            else:
                pass



            # 4. <공급사 발주생성 리스트 확인>

            # MD 계정 로그아웃
            # 우측 상단 로그아웃 UI선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'nav-item btn')])[2]//a", error_msg="로그아웃 버튼 미노출")

            # 초기화면(로그인페이지)으로 이동 확인
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, error_msg="초기화면(로그인페이지) 아이디 입력란 미노출")

            # 공급사 계정 로그인
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

            # 발주관리
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주관리')]", error_msg="공급사 계정 로그인 후 발주 관리 미노출")

            # 발주생성 : N뱃지 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'badge badge-danger badge-pill')]", error_msg="공급사 계정 발주 관리탭 N뱃지 미노출")

            # 신규로 생성한 발주서와 동일한 발주코드의 발주 내역 노출
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'custom-table-striped')]//td)[2]")))
            this_order_code = element.text

            # 비교
            if new_order_code == this_order_code:
                pass
            else:
                raise Exception("신규로 생성한 발주서의 발주코드 와 공급사 발주 내역의 발주코드가 상이함")



            # 5. <공급사 발주생성 건 발주 건 조회>

            # 검색 - 발주코드 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')]", error_msg="공급사 로그인 후 발주생성 시 검색 선택란 미노출")
            self.interact(by_type="XPATH", name="//span[contains(text(), '발주코드')]", error_msg="공급사 로그인 후 발주생성 시 검색 종류 선택란에서 발주코드 발견 미노출")

            # MD가 생성한 발주서 발주코드 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg=new_order_code, error_msg="공급사 발주 생성 시 검색어 입력란 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="공급사 발주관리 탭에서 검색 버튼 미노출")

            # 신규로 생성한 발주서와 동일한 발주코드 발주 내역 리스트에 노출
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'custom-table-striped')]//td)[2]")))
            search_order_code = element.text

            # 비교
            if new_order_code == search_order_code:
                pass
            else:
                raise Exception("신규로 생성한 발주서의 발주코드를 공급사 발주 내역에서 검색했을 때 결과 미노출")



            # 6. <공급사 발주 확정>

            # 발주생성 건 > [상세] 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn button-view-detail btn-primary')]", error_msg="공급사 발주관리 탭에서 검색 후 상세 버튼 미노출")

            # [발주확정] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '발주확정')]", error_msg="공급사 -> 발주관리 -> 특정 발주 상세페이지 발주확정 버튼 미노출")

            # 안내 팝업 - [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '확인')]", error_msg="공급사 -> 발주관리 -> 특정 발주 상세페이지 발주확정 클릭 후 안내팝업 미노출")

            # 발주확정 되었습니다. 토스트 팝업 노출
            self.interact(by_type="XPATH", name="//*[contains(@class, 'toast-container')]", click=False, error_msg="공급사 페이지에서 발주확정 후 발주확정 토스트 텍스트 미노출")

            # [공급사]발주서 상세 페이지 -> 발주상태 : 발주확정으로 노출
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주확정')]", click=False, error_msg="공급사 페이지에서 발주확정 후 발주상태가 발주확정으로 노출되지 않음")

            # 발주시 설정한 값 매핑되어 노출
            # - 발주코드 / 발주상태 / 공급사명 / 입고예정일 / 발주일 / 담당자정보 / 입고지 / 발주구분 / 발주담당자 / 입고시간 / 경유센터 / 비고
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{new_order_code}')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 발주코드 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '발주확정')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 발주상태 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH공급사(VD4360)')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 공급사명 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{next_date}')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 입고예정일 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{current_date}')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 발주일 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), 'SH담당자')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 담당자정보 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '평택상온')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 입고지 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '정규발주')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 발주구분 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '장세희')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 발주담당자 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '일반입고')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 입고시간 매핑된 상태값 미노출")
            self.interact(by_type="XPATH", name="//*[contains(text(), '경유안함')]", click=False, error_msg="공급사 발주 상세 내역에서 발주 확정 후 경유센터 매핑된 상태값 미노출")



            # 7. <발주서 내역 - 발주확정 건 조회>

            # 공급사 로그아웃
            # 우측 상단 로그아웃 UI선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'nav-item btn')])[2]//a", error_msg="로그아웃 버튼 미노출")

            # 초기화면(로그인페이지)으로 이동 확인
            self.interact(by_type="XPATH", name="//*[contains(@id, 'inputEmail')]", click=False, error_msg="초기화면(로그인페이지) 아이디 입력란 미노출")

            # 담당자 로그인
            # 새 탭 열기
            self.driver.execute_script("window.open('');")

            # 새로 열린 탭으로 포커스 변경
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # 담당자 URL 접속
            url = 'https://partner.stg.kurly.com/#/stafflogin'
            self.driver.get(url)

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

            # 발주서 내역 클릭
            self.interact(by_type="XPATH", name="//*[contains(@class,'nav-link')]//span[contains(text(), '발주서 내역')]", error_msg="MD 계정 로그인 후 발주 관리의 발주서 내역 버튼 미노출")

            # 검색버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')]", error_msg="발주내역서 탭에서 검색 종류 선택란 미노출")

            # 발주 코드 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'dropdown-item')]//span[contains(text(),'발주코드')]", error_msg="발주내역서 탭에서 검색종류 중에 발주코드 미노출")

            # 공급사가 확정한 발주서 발주코드 입력
            self.interact(by_type="XPATH", name="//*[contains(@class, 'form-control')]", click=False, send_keys_msg=new_order_code, error_msg="발주코드 입력란 미노출")

            # [검색] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'btn btn-primary') and contains(text(), '검색')]", error_msg="발주내역서 탭에서 검색 버튼 미노출")

            # 공급사가 발주확정한 건 발주코드 동일하게 노출
            self.interact(by_type="XPATH", name=f"//*[contains(text(), '{new_order_code}')]", click=False, error_msg="발주내역서 탭에서 검색 후 공급사가 발주확정한 발주코드 미노출")

            # 발주서내역 확인시 발주등록시 선택한 항목값 매핑되어 노출
            # - 상태 / 발주코드 발주구분 / 입고예정일 / 입고지 / 공급사 / 마스터코드 / 상품명 / 수량 총수량 / 유통기한(소비기한) 제조일자 / 판매방법 출고방법 / 담당MD 담당AMD 발주자 발주일 데이터 노출 확인
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '발주확정')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 상태 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '{new_order_code}')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 발주코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '정규발주')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 발주구분 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '{next_date}')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 입고예정일 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '평택상온')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 입고지 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), 'SH공급사')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 공급사 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), 'SH1111111114')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 마스터코드 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '[QA] SH자동화 테스트용 상품_사용금지')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 상품명 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '5')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 수량 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '후판매')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 판매방법 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '직배송')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 출고방법 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '장세희')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 발주자 미노출")
            self.interact(by_type="XPATH", name=f"//*[contains(@class, 'custom-table-striped')]//*[contains(text(), '{current_date}')]", click=False, error_msg="발주내역서 탭에서 검색 후 매핑된 발주일 미노출")

            # 담당자 로그아웃
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
        self.driver.quit()

## 이 클래스에서 정의된 테스트 메소드를 찾아서 실행하고, 그 결과를 출력하는 코드
# Python에서 모듈이 직접 실행될 때 (즉, 다른 모듈에서 import 되지 않고 직접 실행될 때) 해당 코드 블록을 실행하도록 하는 일종의 조건문
if __name__ == '__main__':
    # 이 클래스에서 정의된 테스트 메소드들을 자동으로 찾아주는 메소드를 사용하여 테스트 스위트(TestSuite) 객체를 생성
    suite = unittest.TestLoader().loadTestsFromTestCase(WarehouseManagement)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)