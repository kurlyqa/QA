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
from time import sleep

class OrderHistory(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_02_주문내역(self):
        try:
            # 1. <컬리몰 -> 주문 생성 확인>

            # 컬리몰 스테이지 url주소
            # kurlymall_url = 'https://www.stg.kurly.com/main'
            kurlymall_url = 'https://www-qa5.stg.kurly.com/main'

            # OMS url 주소
            oms_url = 'https://soms.stg.kurlycorp.kr/login'

            # 컬리몰 스테이지 url 이동
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
                self.interact(by_type="XPATH", name="//*[contains(@class, 'css-1dahn5m e2sqze60')]", error_msg="자유 출입 가능 버튼 미노출")

                # 저장 버튼 클릭
                self.interact(by_type="XPATH", name="//*[contains(@class, 'css-nytqmg e4nu7ef1')]", error_msg="저장 버튼 미노출")
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

            # OMS > 주문 내역 > 전체 주문 메뉴 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-icon notranslate fas fa-bars theme--light')]", error_msg="OMS > 메뉴 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title nav__tab-content-main') and contains(text(), '주문 내역')]", error_msg="OMS > 주문 내역 버튼 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__title nav__tab-content-sub ml-4') and contains(text(), '전체 주문')]", error_msg="OMS > 주문 내역 > 전체 주문 버튼 미노출")

            # 주문번호 검색필드에 복사한 주문번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[6]", send_keys_msg=order_number, click=False, wait_sec=10, error_msg="OMS > 주문 내역 > 전체 주문 > 주문번호 입력란 미노출")

            # [조회] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mr-3 v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--default secondary')]//*[contains(text(), '조회')]", wait_sec=10, error_msg="OMS > 주문 내역 > 전체 주문 > 조회 버튼 미노출")

            # 리스트 확인
            #  주문번호, 배송예정일, 배송유형 : 샛별 , 택배사 : FRESH, 센터: CC04  권역 /배송회차 : X/해당시간 배송회차
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-data-table__wrapper')]//td)[2]", click=False, error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 주문번호 미노출")

            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-data-table__wrapper')]//td)[3]", click=False, error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 배송예정일 미노출")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[8]")))
            delivery_type = element.text

            if delivery_type == "샛별":
                pass
            else:
                raise Exception("배송유형이 샛별이 아님")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[9]")))
            courier_company = element.text

            if courier_company == "FRESH":
                pass
            else:
                raise Exception("택배사가 FRESH가 아님")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[10]")))
            center = element.text

            if center == "CC04":
                pass
            else:
                raise Exception("센터가 CC04가 아님")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[13]")))
            region = element.text

            if "X /" in region:
                pass
            else:
                raise Exception("권역/배송회차가 X/이 아님")

            # 자세히 UI 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-btn v-btn--icon v-btn--round theme--light v-size--default')])[4]", error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 자세히 버튼 미노출")

            # 상세내용 팝업 확인
            # 수령자 정보, 주소, 배송 특이사항, 공동현관 특이사항 데이터 비교
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'subTitleRow')]//span[contains(@class,'text')])[4]")))
            address = element.text

            if address == "서울특별시 동대문구 서울시립대로 5 (답십리동, 신답극동아파트) (신답극동아파트)":
                pass
            else:
                raise Exception("주소가 맞지 않음")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'subTitleRow')]//span[contains(@class,'text')])[6]")))
            address = element.text

            if address == "문앞":
                pass
            else:
                raise Exception("배송 특이사항이 맞지 않음")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'subTitleRow')]//span[contains(@class,'text')])[7]")))
            address = element.text

            if address == "자유출입가능":
                pass
            else:
                raise Exception("공동현관 특이사항이 맞지 않음")

            # 주문 상품 생산 정보 데이터 비교
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'productText')])[2]")))
            product_name = element.text

            if product_name == "살코기 참치":
                pass
            else:
                raise Exception("상품 이름이 맞지 않음")

            # 배송정보 권역, 회차 확인
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'regionMessage')]")))
            region_message = element.text

            if "FRESH / X권역 /" in region_message:
                pass
            else:
                raise Exception("배송정보 권역이 맞지 않음")



            # 2. <전송 보류>

            # 자세히 버튼 닫기
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-icon notranslate fas fa-times theme--light')]", error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 자세히 > 닫기 버튼 미노출")

            # 컬리몰에서 생성된 주문 체크박스 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input--selection-controls__ripple')])[5]", error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 체크박스 미노출")

            # [전송 보류] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '전송 보류')]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송 보류 버튼 미노출")

            # 확인 창 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송 보류 > 확인 버튼 미노출")

            # 전송 보류 완료창 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송 보류 > 확인 > 확인 버튼 미노출")

            # 주문 전체 리스트에 해당 주문 노출안됨
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-alert__content') and contains(text(), '데이터가 존재하지 않습니다.')]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송 보류 > 데이터가 존재함")



            # 3. <전송 보류 상세확인>

            # 전송상태 > 전송보류 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-select__slot')]//*[contains(text(), '전송상태')]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송상태 선택란 미노출")
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-list-item__content')]//*[contains(text(), '전송보류')]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송 보류 > 전송상태 옵션중 전송보류 미노출")

            # [조회] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mr-3 v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--default secondary')]//*[contains(text(), '조회')]", wait_sec=10, error_msg="OMS > 주문 내역 > 전체 주문 > 조회 버튼 미노출")

            # 배송예정일 9999-12-31 노출
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[3]")))
            delivery_date = element.text

            if delivery_date == "9999-12-31":
                pass
            else:
                raise Exception("전송보류 상태의 주문 건의 배송예정일이 9999-12-31이 아님")

            # 전송상태 '전송보류'
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[5]//span[contains(@class, 'v-chip__content')]")))
            transmission_status = element.text

            if transmission_status == "전송보류":
                pass
            else:
                raise Exception("전송상태가 전송보류가 아님")

            # 권역/배송회차 공란 노출
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[13]")))
            region = element.text

            if region == "":
                pass
            else:
                raise Exception("권역/배송회차가 공란이 아님")

            # 상세내용 배송정보 > 권역 미매핑 노출됨
            # 자세히 UI 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-icon notranslate fas fa-external-link-alt theme--light silver--text')]", error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 자세히 버튼 미노출")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'regionMessage')]")))
            region_message = element.text

            if region_message == "권역 미매핑":
                pass
            else:
                raise Exception("배송정보에서 '권역 미매핑' 미노출됨")

            # 자세히 버튼 닫기
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-icon notranslate fas fa-times theme--light')]", error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 자세히 > 닫기 버튼 미노출")



            # 4. <보류 해제>

            # 전송 보류 주문 체크박스 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input--selection-controls__ripple')])[5]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송보류 건 조회 > 체크박스 미노출")

            # [보류 해제] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '보류 해제')]", error_msg="OMS > 주문 내역 > 전체 주문 > 보류 해제 버튼 미노출")

            # 확인 창 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="OMS > 주문 내역 > 전체 주문 > 보류 해제 > 확인 버튼 미노출")

            # 전송 보류 완료창 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송 보류 > 확인 > 확인 버튼 미노출")

            # 배송예정일 팝업 배송예정일 입력 , [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="OMS > 주문 내역 > 전체 주문 > 전송 보류 > 확인 > 확인 > 확인 버튼 미노출")



            # 5. <보류 해제 상세 확인>

            # 검색 영역 [초기화] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '초기화')]", error_msg="OMS > 주문 내역 > 전체 주문 > 초기화 버튼 미노출")

            # 보류해제한 주문 번호 입력
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-text-field__slot')]//input)[6]", send_keys_msg=order_number, click=False, wait_sec=10, error_msg="OMS > 주문 내역 > 전체 주문 > 주문번호 입력란 미노출")

            # [조회] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'mr-3 v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--default secondary')]//*[contains(text(), '조회')]", wait_sec=10, error_msg="OMS > 주문 내역 > 전체 주문 > 조회 버튼 미노출")

            # 배송 예정일 입력한 날짜 노출
            today = datetime.now()
            one_day = timedelta(days=1)
            tomorrow = today + one_day
            tomorrow = tomorrow.strftime("%Y-%m-%d")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[3]")))
            delivery_date = element.text

            if tomorrow == delivery_date:
                pass
            else:
                raise Exception("배송예정일이 내일이 아님")

            # 전송회차, 권역/배송회차 공란 노출
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[12]")))
            region = element.text

            if region == "":
                pass
            else:
                raise Exception("전송회차가 공란이 아님")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'v-data-table__wrapper')]//td)[13]")))
            region = element.text

            if region == "":
                pass
            else:
                raise Exception("권역/배송회차가 공란이 아님")

            # 상세내역 배송정보 > 권역 미매핑 노출
            # 자세히 UI 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-icon notranslate fas fa-external-link-alt theme--light silver--text')]", error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 자세히 버튼 미노출")

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'regionMessage')]")))
            region_message = element.text

            if region_message == "권역 미매핑":
                pass
            else:
                raise Exception("배송정보에서 '권역 미매핑' 미노출됨")

            # 자세히 버튼 닫기
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-icon notranslate fas fa-times theme--light')]", error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 자세히 > 닫기 버튼 미노출")



            # 6. <주문취소>

            # 컬리몰 생성된 주문 체크박스 선택
            self.interact(by_type="XPATH", name="(//*[contains(@class, 'v-input--selection-controls__ripple')])[5]", error_msg="OMS > 주문 내역 > 전체 주문 > 조회 > 체크박스 미노출")

            # [주문 취소] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '주문 취소')]", error_msg="OMS > 주문 내역 > 전체 주문 > 주문 취소 버튼 미노출")

            # 확인 창 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="OMS > 주문 내역 > 전체 주문 > 주문 취소 > 확인 버튼 미노출")

            # 주문 취소 완료창 [확인] 버튼 선택
            self.interact(by_type="XPATH", name="//*[contains(@class, 'v-btn__content') and contains(text(), '확인')]", error_msg="OMS > 주문 내역 > 전체 주문 > 주문 취소 > 확인 > 확인 버튼 미노출")

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
    suite = unittest.TestLoader().loadTestsFromTestCase(OrderHistory)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)