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
import ssl
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

s1 = TestLoader().loadTestsFromTestCase(LMSWebLogin)
s2 = TestLoader().loadTestsFromTestCase(TaskManagement)
s3 = TestLoader().loadTestsFromTestCase(SiteManagement)
s4 = TestLoader().loadTestsFromTestCase(MasterManagement)
s5 = TestLoader().loadTestsFromTestCase(AccountManagement)
s6 = TestLoader().loadTestsFromTestCase(MobileWebLogin)

suite = TestSuite([s1, s2, s3, s4, s5, s6])

daytime = datetime.datetime.now()
dt = daytime.strftime("%Y-%m-%d_%H-%M-%S")
domain = "LMS"
filename = domain + f"AutomationTestReport"
dir = os.getcwd()

# 전송할 파일 경로 설정
file_path = dir + f"/reports/" + filename + "_" + dt + ".html"

# report_title 파일열면 가장위에 있는 메인 title
runner = HTMLTestRunner(combine_reports=True, report_name=filename, report_title=domain + " Automation Test Report")

# 테스트 실행 결과 저장
result = runner.run(suite)

# 인증서 설정
ssl._create_default_https_context = ssl._create_unverified_context

# 테스트 결과 가져오기
pass_count = len(result.successes)
fail_count = len(result.failures)

# Slack 토큰 설정
slack_token = os.environ.get('SLACK_TOKEN')
client = WebClient(token=slack_token)

# 채널ID
channel = 'C05BQN1D9GT'

mrkdwn_text = f'''
    *[{domain} 자동화 테스트 결과]*\n
    '''

if fail_count > 0:
    mrkdwn_text = mrkdwn_text + f'''
    Pass 개수 : {pass_count} / `Fail 개수 : {fail_count}`\n
    '''
else:
    mrkdwn_text = mrkdwn_text + f'''
    Pass 개수 : {pass_count} / Fail 개수 : {fail_count}\n
    '''

mrkdwn_text = mrkdwn_text + f'''  
    <@U04U77FJ4ES>\n
    <@U04GD12NLA0>
    '''

# 메세지 및 파일 슬랙 전송
try:
    response_msg = client.chat_postMessage(channel=channel,
                                           text=mrkdwn_text)

    response_file = client.files_upload_v2(channel=channel,
                                          file=file_path,
                                          filename=filename+dt)

except SlackApiError as e:
    print('Error: {}'.format(e.response['error']))

####################### Markdown_text ########################
# mrkdwn_text = '''
# This is test message.
# > Block quote
#
# *Bold text*
#
# ```
# code block - line 1
# code block - line 2\ncode block - line 3
# ```
#
# `highlight`
#
# _italicize_
#
# ~Strikethrough~
#
# <https://www.google.com|This is link to google.com>
# '''



####################### Webhook ##############################
# def send_message_to_slack(text):
#     url = "WebHook Url"
#
#     payload = { "text" : text }
#
#     requests.post(url, json=payload)
#
# def send_message_to_slack(webhook_url, channel, message, file_path=None):
#     payload = {
#         'channel': channel,
#         'text': message
#     }
#
#     files = None
#     if file_path:
#         files = {'file': open(file_path, 'rb')}
#
#     response = requests.post(webhook_url, json=payload, files=files)
#     if response.status_code == 200:
#         print("메시지 전송 성공")
#     else:
#         print("메시지 전송 실패")
#
# # Webhook URL 설정
# webhook_url = 'https://hooks.slack.com/services/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'
#
# # 채널과 메시지 내용 설정
# channel = 'C05BQN1D9GT'
# message = '안녕하세요, 테스트입니다.'
#
# # 메시지와 파일 전송
# send_message_to_slack(webhook_url, channel, message, file_path)