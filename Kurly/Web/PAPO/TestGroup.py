#!/usr/bin/env python
#coding=utf8
from __future__ import print_function
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from lms_web_login import LMSWebLogin
from task_management import TaskManagement
from site_management import SiteManagement
from master_management import MasterManagement
from account_management import AccountManagement
from mobile_web_login import MobileWebLogin
import datetime
import os
import requests
import json

s1 = TestLoader().loadTestsFromTestCase()
# s2 = TestLoader().loadTestsFromTestCase()
# s3 = TestLoader().loadTestsFromTestCase()
# s4 = TestLoader().loadTestsFromTestCase()
# s5 = TestLoader().loadTestsFromTestCase()
# s6 = TestLoader().loadTestsFromTestCase()

suite = TestSuite([s1])
# suite = TestSuite([s1, s2, s3, s4, s5, s6])

daytime = datetime.datetime.now()
dt = daytime.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"PAPOAutomationTestReport"
dir = os.getcwd()

# 전송할 파일 경로 설정
file_path = (dir + f"/reports/PAPOAutomationTestReport_"+dt+".html")

# report_title 파일열면 가장위에 있는 메인 title
runner = HTMLTestRunner(combine_reports=True, report_name=filename, report_title="PAPO Automation Test Report")

# 테스트 실행 결과 저장
result = runner.run(suite)

# Slack 토큰 설정
slack_token = "xoxb-135797385811-5371175357495-AX0671dxN5cIIhl64I6CfhHg"

# 파일 전송 함수 정의
def send_file_to_slack(file_path, pass_count, fail_count):
    try:
        # 파일 열기
        with open(file_path, 'rb') as file:
            # Slack 파일 업로드 URL
            upload_url = 'https://slack.com/api/files.upload'
            # 전송할 채널명
            channel = 'D05B5272K1U'
            # 전송할 파일명
            filename = f"PAPOAutomationTestReport_{dt}.html"
            # 전송 제목
            title = "PAPO 자동화 테스트 결과 : " + dt

            # 메시지 내용
            if fail_count == 0:
                message = f"```\nPass 개수 : {pass_count} / Fail 개수 : {fail_count}\n```"
            else:
                message = f"```\nPass 개수 : {pass_count} / Fail 개수 : {fail_count}\n```"

            # POST 요청 보내기
            response = requests.post(upload_url, files={'file': file}, data={'token': slack_token, 'channels': channel, 'filename': filename, 'title': title, 'initial_comment': message})
            if response.ok:
                print("파일 전송 성공")
            else:
                print("파일 전송 실패")
    except Exception as e:
        print(f"파일 전송 에러: {str(e)}")

# 테스트 결과 가져오기
pass_count = len(result.successes)
fail_count = len(result.failures)

# 파일 전송 함수 호출
send_file_to_slack(file_path, pass_count, fail_count)

# # 파일 전송 함수 호출
# send_file_to_slack(file_path)

#### 슬랙 앱으로 메세지 보내는 코드 ####
# # 슬랙 API 요청 URL
# url = "https://slack.com/api/chat.postMessage"
#
# # 요청 헤더 설정
# headers = {
#     "Authorization": "Bearer xoxb-135797385811-5371175357495-AX0671dxN5cIIhl64I6CfhHg",
#     "Content-Type": "application/json"
# }
#
# # 메시지 데이터 생성
# message = {
#     "channel": "D05B5272K1U",
#     "text": "테스트 결과를 전송합니다."
# }
#
# # API 요청 보내기
# response = requests.post(url, headers=headers, data=json.dumps(message))
#
# # 응답 확인
# if response.status_code == 200:
#     print("메시지가 성공적으로 전송되었습니다.")
# else:
#     print("메시지 전송에 실패했습니다. 응답 코드:", response.status_code)