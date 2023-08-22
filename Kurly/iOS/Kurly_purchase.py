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
        print(1)
        TCFG.driver.close_app()
        sleep(2)
        TCFG.driver.launch_app()
        sleep(2)

    def test_01_CreditCard_Payment(self):
        try:
            # 컬리 로고 노출 확인
            self.interact_by_id('navi_logo_white', search_sec=20, click=False)

            # 검색 클릭
            self.interact_by_id('tab_btn_search', search_sec=20)

            # 깻잎 입력
            self.interact_by_xpath('//XCUIElementTypeTextField[@value="검색어를 입력해주세요"]', search_sec=20, send_keys_msg="깻잎", click=False)

            # 검색 클릭
            self.interact_by_xpath('//XCUIElementTypeButton[@name="Search"]', wait_sec=5, search_sec=20)

            # 첫번째 상품의 장바구니 클릭
            self.interact_by_xpath('(//XCUIElementTypeButton[@name="saleBtnCart"])[1]', search_sec=20)

            # 장바구니 담기 클릭
            self.interact_by_xpath('//*[contains(@name, "장바구니 담기")]', search_sec=20)

            # 하단 팝업 닫기
            TouchAction(TCFG.driver).tap(None, 324, 54, 1).perform()
            sleep(2)

            # 장바구니 버튼 클릭
            self.interact_by_xpath('//XCUIElementTypeImage[@name="navi_btn_cart_purple"]', search_sec=20)

            # 주문하기 버튼 클릭
            self.interact_by_xpath('//*[contains(@name, "주문하기")]', search_sec=20)

            # 포인트 모두사용 클릭
            self.interact_by_id('모두사용', search_sec=20)

            ### 하단으로 이동 ###
            # 좌표값 설정
            start_x = 217
            start_y = 721
            end_x = 217
            end_y = 247

            # TouchAction 객체 생성
            action = TouchAction(TCFG.driver)

            # swipe 동작 수행
            action.press(x=start_x, y=start_y).wait(250).move_to(x=end_x, y=end_y).release().perform()
            sleep(2)
            action.press(x=start_x, y=start_y).wait(250).move_to(x=end_x, y=end_y).release().perform()
            sleep(2)

            # 결제하기 클릭
            self.interact_by_id('0원 결제하기', search_sec=20)

            # 앱 사용 어떠셨나요? 팝업
            try:
                self.interact_by_xpath('//XCUIElementTypeStaticText[@name="응답하지 않을래요"]', search_sec=20)
            except:
                pass

            # 주문 상세보기 클릭
            self.interact_by_id('주문 상세보기', search_sec=20)

            # 전체 상품 주문 취소 클릭
            self.interact_by_id('전체 상품 주문 취소', search_sec=20)

            # 확인 클릭
            self.interact_by_id('확인', search_sec=20)

            # 하단으로 이동
            action.press(x=start_x, y=start_y).wait(250).move_to(x=end_x, y=end_y).release().perform()
            sleep(2)

            # 주문 취소 동의 클릭
            self.interact_by_id('주문취소 내역에 동의', search_sec=20)

            # 주문 취소하기 클릭
            self.interact_by_id('주문 취소하기', search_sec=20)

            # 확인 클릭
            self.interact_by_id('확인', search_sec=20)

            # 홈으로 이동 클릭
            self.interact_by_id('홈으로 이동', search_sec=20)

            # 컬리 로고 노출 확인
            self.interact_by_id('navi_logo_white', search_sec=20, click=False)
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