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

class TimeTest(testModule):

    def setUp(self):
        super().setUp() # testModule 클래스의 setUp 함수 호출

    def test_01_OMS회차시간변경(self):
        try:
            # 1. <1회차 테스트>
            # 현재 시간 가져오기
            now = datetime.now()
            two_minute_later = now + timedelta(minutes=2)

            # H:M:S 형태로 변경
            two_minute_later = two_minute_later.strftime("%H:%M:%S")

            # 2분 후를 마감 시간으로 지정
            # send_keys_msg = two_minute_later
            # 주문 내리기
            # 회차가 1회차인지 확인하기
            # while 1 반복하면서 현재 시간이 2분후 시간보다 큰지 확인하기
            while 1:
                current_time = datetime.now()
                current_time = current_time.strftime("%H:%M:%S")
                if current_time > two_minute_later:
                    print(1346)
                    break

            # 크면 2회차 마감시간을 2분 후로 지정
            # 현재 시간 가져오기
            now = datetime.now()
            two_minute_later = now + timedelta(minutes=2)

            # H:M:S 형태로 변경
            two_minute_later = two_minute_later.strftime("%H:%M:%S")

            # 주문 내리기


            # 회차가 2회차인지 확인하기
            # while 1 반복하면서 현재 시간이 2분후 시간보다 큰지 확인하기
            # 크면 3회차 마감시간을 2분 후로 지정
            # 주문 내리기
            # 회차가 3회차인지 확인하기
            # while 1 반복하면서 현재 시간이 2분후 시간보다 큰지 확인하기
            # 크면 주문 내리기
            # 회차가 다음날 1회차인지 확인하기




            # # 현재 시간 기록
            # current_time = datetime.now()
            #
            # # 1분 후의 시간 계산
            # one_minute_later = current_time + timedelta(minutes=1)
            #
            # # 2시간 후의 시간 계산
            # two_hours_later = current_time + timedelta(hours=2)
            #
            # # 시간 비교 및 출력
            # if one_minute_later > two_hours_later:
            #     print("1분 후의 시간이 더 큽니다.")
            # elif two_hours_later > one_minute_later:
            #     print("2시간 후의 시간이 더 큽니다.")
            # else:
            #     print("1분 후와 2시간 후의 시간이 같습니다.")





            pass
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TimeTest)
    # TextTestRunner 클래스의 객체를 생성하여 생성된 테스트 스위트 객체를 실행. verbosity 인자는 테스트 결과를 출력할 상세도를 설정하는 인자. 2이면 테스트 케이스 수, 테스트 시간, 테스트 결과를 출력. .run(suite)는 생성된 TestSuite객체를 실행하는 메소드.
    unittest.TextTestRunner(verbosity=2).run(suite)