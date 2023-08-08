#!/usr/bin/env python
#coding=utf8
from __future__ import print_function
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from papo_login import PAPOLogin
from order_management import OrderManagement
from warehouse_management import WarehouseManagement
from settlement_management_reverse import SettlementManagementReverse
from settlement_management_regular import SettlementManagementRegular
import datetime
import os
import ssl
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

s1 = TestLoader().loadTestsFromTestCase(PAPOLogin)
s2 = TestLoader().loadTestsFromTestCase(OrderManagement)
s3 = TestLoader().loadTestsFromTestCase(WarehouseManagement)
s4 = TestLoader().loadTestsFromTestCase(SettlementManagementReverse)
s5 = TestLoader().loadTestsFromTestCase(SettlementManagementRegular)

suite = TestSuite([s4])
# suite = TestSuite([s1, s2])
# suite = TestSuite([s1, s2, s3])
# suite = TestSuite([s1, s2, s3, s4])
# suite = TestSuite([s1, s2, s3, s4, s5])

daytime = datetime.datetime.now()
dt = daytime.strftime("%Y-%m-%d_%H-%M-%S")
domain = "PAPO"
filename = domain + f"AutomationTestReport"
dir = os.getcwd()

# 전송할 파일 경로 설정
file_path = dir + f"/reports/{filename}_{dt}.html"

# report_title 파일열면 가장위에 있는 메인 title
runner = HTMLTestRunner(combine_reports=True, report_name=filename, report_title=domain + " Automation Test Report")

# 테스트 실행 결과 저장
result = runner.run(suite)

# # 인증서 설정
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # 테스트 결과 가져오기
# pass_count = len(result.successes)
# fail_count = len(result.failures)
#
# # Slack 토큰 설정
# slack_token = os.environ.get('SLACK_TOKEN')
# client = WebClient(token=slack_token)
#
# # 채널ID
# channel = 'C05BQN1D9GT'
#
# mrkdwn_text = f'''
#     *[{domain} 자동화 테스트 결과]*\n
#     '''
#
# if fail_count > 0:
#     mrkdwn_text = mrkdwn_text + f'''
#     Pass 개수 : {pass_count} / `Fail 개수 : {fail_count}`\n
#     '''
# else:
#     mrkdwn_text = mrkdwn_text + f'''
#     Pass 개수 : {pass_count} / Fail 개수 : {fail_count}\n
#     '''
#
# mrkdwn_text = mrkdwn_text + f'''
#     <@U04U77FJ4ES>\n
#     <@U04CASWJYCA>
#     '''

# # 메세지 및 파일 슬랙 전송
# try:
#     response_msg = client.chat_postMessage(channel=channel,
#                                            text=mrkdwn_text)
#
#     response_file = client.files_upload_v2(channel=channel,
#                                           file=file_path,
#                                           filename=filename+dt)
#
# except SlackApiError as e:
#     print('Error: {}'.format(e.response['error']))