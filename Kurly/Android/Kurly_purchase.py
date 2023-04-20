# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from TestModule import testModule
from Bootstrap import initialize_bp
from Bootstrap import TEST_CONFIG as TCFG

class Kurly_purchase(testModule):

    def initialize(self):
        TCFG.is_initialized = True
        argv = sys.argv[1]
        initialize_bp(self, argv)
        reso = TCFG.driver.get_window_size()
        TCFG.res.append(reso["width"])
        TCFG.res.append(reso["height"])

    def setUp(self):
        if not TCFG.is_passed and TCFG.is_initialized:
            self.exception('home')
        if not TCFG.is_initialized:
            self.initialize()
            TCFG.is_finished = False
        TCFG.is_passed = False

    def exception(self, menu):
        TCFG.driver.close_app()
        sleep(2)
        TCFG.driver.launch_app()
        sleep(2)

    def test_01_CreditCard_Payment(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # 컬리 로고 노출 확인
                self.interact_by_id('com.dbs.kurly.m2:id/toolbar_logo', search_sec=20, click=False)
                # 검색 클릭
                self.interact_by_xpath('//android.widget.FrameLayout[@content-desc="검색"]', search_sec=20)
                # 깻잎 입력
                self.interact_by_id('com.dbs.kurly.m2:id/search_edt', search_sec=20, send_keys_msg="깻잎", click=False)
                # 검색 클릭
                self.interact_by_id('com.dbs.kurly.m2:id/iv_search_icon', search_sec=20)
                # 첫번째 상품 클릭
                self.interact_by_id('com.dbs.kurly.m2:id/thumbnail', search_sec=20)
                # 구매하기 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="구매하기"]', search_sec=20)
                # 장바구니 담기 클릭
                self.interact_by_id('com.dbs.kurly.m2:id/addToCartText', search_sec=20)
                # 하단 팝업 닫기
                TouchAction(TCFG.driver).tap(None, 997, 152, 1).perform()
                sleep(2)
                # 장바구니 버튼 클릭
                self.interact_by_id('com.dbs.kurly.m2:id/ivCartIcon', search_sec=20)
                # 주문하기 버튼 클릭
                self.interact_by_id('com.dbs.kurly.m2:id/titleView', search_sec=20)
                # 포인트 모두사용 클릭
                self.interact_by_xpath('//android.widget.Button[@text="모두사용"]', search_sec=20)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)


                self.interact_by_xpath('//*[contains(@text, "결제하기")]', search_sec=20) # 결제하기 클릭
                self.interact_by_xpath('//android.widget.Button[@text="앱 없이 결제"]', search_sec=20) # 앱 없이 결제 클릭
                self.interact_by_xpath('//android.widget.EditText', search_sec=20, send_keys_msg="010-7513-6165", click=False) # 핸드폰 번호 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="910131-1", click=False) # 주민번호 입력
                self.interact_by_xpath('//android.view.View[@text="개인정보 수집이용 동의 체크안됨"]', search_sec=20) # 개인정보 수집이용 동의 체크
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 클릭
                self.interact_by_xpath('//*[contains(@text, "결제하기")]', search_sec=20) # 결제하기 클릭
                # 비밀번호 클릭(KB페이의 경우 번호 버튼이 잡힘)
                self.interact_by_xpath('//android.widget.Button[@text="3"]', search_sec=20) # 3 클릭
                self.interact_by_xpath('//android.widget.Button[@text="1"]', search_sec=20) # 1 클릭
                self.interact_by_xpath('//android.widget.Button[@text="8"]', search_sec=20) # 8 클릭
                self.interact_by_xpath('//android.widget.Button[@text="2"]', search_sec=20) # 2 클릭
                self.interact_by_xpath('//android.widget.Button[@text="3"]', search_sec=20) # 3 클릭
                self.interact_by_xpath('//android.widget.Button[@text="1"]', search_sec=20) # 1 클릭
                self.interact_by_xpath('//*[contains(@text, "확인")]', search_sec=20) # 확인 버튼 클릭
                sleep(4)
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa.dev:id/order_success_order_detail_button', search_sec=20) # 주문상세보기 버튼 클릭
                sleep(4)
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa.dev:id/order_card_item_button', search_sec=20) # 주문 취소 버튼 클릭
                sleep(4)
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa.dev:id/claim_product_next_btn', search_sec=20) # 다음 버튼 클릭
                sleep(4)
                self.interact_by_xpath('//*[contains(@text, "주문실수")]', search_sec=20) # 주문실수 버튼 클릭
                sleep(4)
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa.dev:id/claim_reason_radio_memo', search_sec=20, send_keys_msg="주문취소 테스트입니다!!!", click=False) # 상세사유 입력
                sleep(4)
                TouchAction(TCFG.driver).tap(None, 1018, 582, 1).perform() # 키패드 닫기
                sleep(4)
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa.dev:id/claim_reason_next_btn', search_sec=20) # 다음 클릭
                sleep(4)
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa.dev:id/claim_method_next_btn', search_sec=20) # 취소요청 클릭
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa.dev:id/claim_result_title', search_sec=20, click=False) # 취소접수가 완료되었습니다. 텍스트 노출 확인
                sleep(4)
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa.dev:id/claim_detail_bottom_ok', search_sec=20) # 취소 상세보기 버튼 클릭
                sleep(4)
                self.interact_by_xpath('//android.widget.TextView[@text="취소완료"]', search_sec=20, click=False) # "취소완료" 텍스트 노출 확인
                sleep(4)

                # 릴리즈앱
                # self.interact_by_id('com.buzzni.android.subapp.shoppingmoa:id/main_search_textview', search_sec=7) # 검색 창 클릭
                # self.interact_by_id('com.buzzni.android.subapp.shoppingmoa:id/search_edittext', search_sec=7, send_keys_msg="치약", click=False) # 검색어 입력
                # self.interact_by_id('com.buzzni.android.subapp.shoppingmoa:id/search_btn', search_sec=7) # 검색 버튼 클릭
                # self.interact_by_xpath('//*[contains(@text, "이전방송")]', search_sec=7) # 이전방송 클릭

                # 생방송 상품 구매
                # self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View', search_sec=7) # 상품 선택
                # self.interact_by_id('com.buzzni.android.subapp.shoppingmoa:id/product_detail_buy_button', search_sec=7) # 구매 버튼 클릭
                # TouchAction(TCFG.driver).tap(None, 978, 2015, 1).perform()  # 닫기 버튼 클릭
                # sleep(1)
                # TouchAction(TCFG.driver).tap(None, 880, 2092, 1).perform()  # 구매하기 버튼 클릭
                # sleep(1)
                #
                #
                # self.interact_by_xpath('', search_sec=7) # 결제 하기 클릭
                # self.interact_by_xpath('', search_sec=7) # 신용카드 선택
                # self.interact_by_xpath('', search_sec=7) # KB 국민 선택
                # self.interact_by_xpath('', search_sec=7) # 결제 동의 버튼 클릭

                # 아래 일반 상품 구매
                # self.interact_by_xpath('//android.view.View/android.widget.TabWidget/android.view.View/android.view.View[2]/android.view.View/android.widget.ListView/android.view.View[1]/android.widget.Button', search_sec=7) # 첫번째 옵션 상품 클릭
                # self.interact_by_xpath('//*[contains(@text, "바로구매")]', search_sec=7) # 바로구매 클릭
                # scroll_id(self, 'com.buzzni.android.subapp.shoppingmoa:id/order_activity_order_payment_credit_card', loc=TCFG.res[1]*0.5, y1=TCFG.res[1]*0.9, y2=TCFG.res[1]*0.6)
                # self.interact_by_id('com.buzzni.android.subapp.shoppingmoa:id/order_activity_order_payment_credit_card_type', search_sec=7) # 카드 선택 클릭
                # self.interact_by_xpath('//*[contains(@text, "KB국민")]', search_sec=7) # KB국민 클릭
                # self.interact_by_id('com.buzzni.android.subapp.shoppingmoa:id/order_activity_payment_button', search_sec=7) # 결제하기 버튼 클릭
                # self.interact_by_xpath('//android.widget.Button[@text="앱 없이 결제"]', search_sec=7) # 앱 없이 결제 클릭
                # self.interact_by_xpath('//android.widget.EditText', search_sec=7, send_keys_msg="010-7513-6165", click=False) # 핸드폰 번호 입력
                # self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=7, send_keys_msg="910131-1", click=False) # 주민번호 입력
                # self.interact_by_xpath('//android.view.View[@text="개인정보 수집이용 동의 체크안됨"]', search_sec=7) # 개인정보 수집이용 동의 체크
                # self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=7) # 로그인 클릭
            except:
                # if loop_count == (TCFG.check_loop_count-1):
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("1 Passed")
                TCFG.is_passed = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Kurly_purchase)
	unittest.TextTestRunner(verbosity=2).run(suite)
