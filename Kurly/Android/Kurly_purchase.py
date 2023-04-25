# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from TestModule import testModule
from Bootstrap import initialize_bp
from Bootstrap import TEST_CONFIG as TCFG

class KurlyPurchase(testModule):

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
            ### 하단 팝업 닫기 ###
            # 좌표값 설정
            x = 997
            y = 152
            # TouchAction 객체 생성
            action = TouchAction(TCFG.driver)
            # 좌표 클릭 동작 수행
            action.tap(x=x, y=y).perform()
            sleep(2)
            ###
            # 장바구니 버튼 클릭
            self.interact_by_id('com.dbs.kurly.m2:id/ivCartIcon', search_sec=20)
            # 주문하기 버튼 클릭
            self.interact_by_id('com.dbs.kurly.m2:id/titleView', search_sec=20)
            # 포인트 모두사용 클릭
            self.interact_by_xpath('//android.widget.Button[@text="모두사용"]', search_sec=30)
            ### 하단으로 이동 ###
            # 좌표값 설정
            start_x = 12
            start_y = 1237
            end_x = 12
            end_y = 600
            # swipe 동작 수행
            action.press(x=start_x, y=start_y).wait(250).move_to(x=end_x, y=end_y).release().perform()
            sleep(2)
            action.press(x=start_x, y=start_y).wait(250).move_to(x=end_x, y=end_y).release().perform()
            sleep(2)
            ###
            # 결제하기 클릭
            self.interact_by_xpath('//*[contains(@text, "결제하기")]', search_sec=20)
            # 주문 상세보기 클릭
            self.interact_by_xpath('//*[contains(@text, "주문 상세보기")]', search_sec=20)
            # 전체 상품 주문 취소 클릭
            self.interact_by_xpath('//*[contains(@text, "전체 상품 주문 취소")]', search_sec=20)
            # 확인 클릭
            self.interact_by_xpath('//*[contains(@text, "확인")]', search_sec=20)
            # 하단으로 이동
            action.press(x=start_x, y=start_y).wait(250).move_to(x=end_x, y=end_y).release().perform()
            sleep(2)
            # 주문 취소 동의 클릭
            self.interact_by_xpath('//android.widget.CheckBox[@text="주문취소 내역에 동의 (전자상거래) (필수)"]', search_sec=20)
            # 주문 취소하기 클릭
            self.interact_by_xpath('//*[contains(@text, "주문 취소하기")]', search_sec=20)
            # 확인 클릭
            self.interact_by_xpath('//*[contains(@text, "확인")]', search_sec=20)
            # 홈으로 이동 클릭
            self.interact_by_xpath('//*[contains(@text, "홈으로 이동")]', search_sec=20)
            # 컬리 로고 노출 확인
            self.interact_by_id('com.dbs.kurly.m2:id/toolbar_logo', search_sec=20, click=False)
        except:
            print("Error!")
            TCFG.is_finished = True
            self.assertEqual(0, 1)
        else:
            print("1 Passed")
            TCFG.is_finished = True
            TCFG.is_passed = True

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(KurlyPurchase)
	unittest.TextTestRunner(verbosity=2).run(suite)
