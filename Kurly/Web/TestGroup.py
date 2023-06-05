#!/usr/bin/env python
#coding=utf8
from __future__ import print_function
from unittest import TestLoader, TestSuite
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from HtmlTestRunner import HTMLTestRunner
from lms_web_login import LMSWebLogin
from task_management import TaskManagement
from site_management import SiteManagement
from master_management import MasterManagement
from account_management import AccountManagement
from mobile_web_login import MobileWebLogin
import datetime
import os


s1 = TestLoader().loadTestsFromTestCase(LMSWebLogin)
s2 = TestLoader().loadTestsFromTestCase(TaskManagement)
s3 = TestLoader().loadTestsFromTestCase(SiteManagement)
s4 = TestLoader().loadTestsFromTestCase(MasterManagement)
s5 = TestLoader().loadTestsFromTestCase(AccountManagement)
s6 = TestLoader().loadTestsFromTestCase(MobileWebLogin)

suite = TestSuite([s1, s2, s3, s4, s5, s6])

# # Slack 토큰 설정
# slack_token = ""
#
# # Slack 클라이언트 생성
# client = WebClient(token=slack_token)

daytime = datetime.datetime.now()
dt = daytime.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"LMSAutomationFunctionalTestReport"
dir = os.getcwd()

# 전송할 파일 경로 설정
file_path = (dir + f"/reports/LMSAutomationTestReport_"+dt+".html")

# report_title 파일열면 가장위에 있는 메인 title
runner = HTMLTestRunner(combine_reports=True, report_name=filename, report_title="LMS Automation Functional Test Report")
runner.run(suite)

# # 파일 전송 함수 정의
# def send_file_to_slack(file_path):
#     try:
#         # 파일 전송
#         response = client.files_upload(
#             channels="#general",  # 전송할 채널명
#             file=file_path,  # 전송할 파일 경로
#         )
#         if response["ok"]:
#             print("파일 전송 성공")
#         else:
#             print("파일 전송 실패")
#     except SlackApiError as e:
#         print(f"파일 전송 에러: {e.response['error']}")
#
# # 파일 전송 함수 호출
# send_file_to_slack(file_path)