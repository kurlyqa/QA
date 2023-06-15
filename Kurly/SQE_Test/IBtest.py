from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import datetime, time
from selenium.webdriver.common.by import By
from time import sleep
import HtmlTestRunner
import unittest

## 파트너 포탈 변수 선언
papo_web_id = 'qa_md1@kurlycorp.com'  # 파트너 포탈 계정
papo_web_pw = 'kurly12!'  # 파트너 포탈 패스워드
vd_id = 'VD2008.01'  # 공급사 계정
vd_pw = 'kurly12!@#'  # 공급사 패스워드
rms_web_id = 'qa_auto_test'  # RMS 계정
rms_web_pw = 'kurlyqa1234'  # RMS 패스워드
sku_code = 'MK0000048666'  # 테스트 SKU CODE

test_start_time0 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print()
print('--* SQA - RMS 기본기능 | 자동화 테스트 시작시간 :', test_start_time0)

class PaPoTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://partner.stg.kurly.com/#/stafflogin')
        # 아이디 입력란을 찾은 후, 아이디를 입력함
        self.driver.find_element(By.ID, 'inputEmail').send_keys(papo_web_id)
        # 비밀번호 입력란을 찾은 후, 비밀번호를 입력함
        self.driver.find_element(By.ID, 'inputPassword').send_keys(papo_web_pw)
        # 로그인 버튼을 찾은 후, 클릭
        self.driver.find_element(By.XPATH, '//*[@id="app"]/form/div/div[4]/button[1]').click()

    def interact(self, by_type, name, wait_sec=0, click=True, send_keys_msg=None):
        if by_type == 'XPATH':
            if send_keys_msg == None:
                if click:
                    ele = self.driver.find_element(by=By.XPATH, value=name)
                    self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
                    self.driver.execute_script("arguments[0].click();", ele)
                elif click == False:
                    ele = self.driver.find_element(by=By.XPATH, value=name)
                    self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
            else:
                self.driver.find_element(by=By.XPATH, value=name).send_keys(send_keys_msg)
            sleep(wait_sec)

    def test_01(self):
        driver = self.driver
        papo_title = driver.title
        value = 'Kurly Partner Portal'
        self.assertEqual(papo_title, value, 'SQA Test failed.')

    def test_02(self):
        driver = self.driver
        # GNB > 발주관리 메뉴 이동
        driver.find_element(By.PARTIAL_LINK_TEXT, '발주관리').click()
        time.sleep(1)
        # SKU 마스터코드 검색
        self.interact(by_type="XPATH", name="(//*[contains(@class, 'btn dropdown-toggle btn-primary dropdown-toggle-no-caret')])[1]")
        self.interact(by_type="XPATH", name="//span[contains(text(), '마스터코드')]")
        self.interact(by_type="XPATH", name="//input[@type='text' and @class='form-control']", click=False, send_keys_msg=sku_code)
        time.sleep(1)

        # 검색버튼 클릭
        self.interact(by_type="XPATH", name="//button[@type='submit' and @class='btn btn-primary']")
        SKU_CODE = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[3]').text
        time.sleep(1)
        SKU_NAME = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[4]').text
        print()
        print('--* 상품 코드 :', SKU_CODE, '상품명 :', SKU_NAME)

        # 발주생성
        self.interact(by_type="XPATH", name="(//*[contains(@class, 'list-checkbox custom-control custom-checkbox')])")
        self.interact(by_type="XPATH", name="(//*[contains(@id, 'viewPurchaseOrder')])")

        # 발주그룹명
        self.interact(by_type="XPATH", name="//input[@type='text' and @class='form-control']", click=False, send_keys_msg='물류SQE 테스트 발주')
        self.interact(by_type="XPATH", name="(//*[contains(@id, 'salesEstimatedDays_0_0')])", click=False, send_keys_msg='10')
        self.interact(by_type="XPATH", name="(//*[contains(@id, 'salesEstimatedDays_0_1')])", click=False, send_keys_msg='10')
        self.interact(by_type="XPATH", name="(//*[contains(@id, 'salesEstimatedDays_0_2')])", click=False, send_keys_msg='10')
        self.interact(by_type="XPATH", name="(//*[contains(@id, 'salesEstimatedDays_0_3')])", click=False, send_keys_msg='10')

        self.interact(by_type="XPATH", name="(//*[contains(@id, '0_0')])", click=False, send_keys_msg='10')
        self.interact(by_type="XPATH", name="(//*[contains(@id, '0_1')])", click=False, send_keys_msg='10')
        self.interact(by_type="XPATH", name="(//*[contains(@id, '0_2')])", click=False, send_keys_msg='10')
        self.interact(by_type="XPATH", name="(//*[contains(@id, '0_3')])", click=False, send_keys_msg='10')

        #Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[2]/td[30]/select')).select_by_visible_text('B동')
        #Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[3]/td[30]/select')).select_by_visible_text('1층')
        #Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[4]/td[30]/select')).select_by_visible_text('1층')
        #Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[5]/td[30]/select')).select_by_visible_text('1층')

        Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[2]/td[34]/select')).select_by_visible_text('긴급발주')
        Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[3]/td[34]/select')).select_by_visible_text('긴급발주')
        Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[4]/td[34]/select')).select_by_visible_text('긴급발주')
        Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[5]/td[34]/select')).select_by_visible_text('긴급발주')
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/mk-jj-mac-050/Git/Kurly/Partner_Portal/reports'))