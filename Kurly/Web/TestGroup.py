#!/usr/bin/env python
#coding=utf8
from __future__ import print_function
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from lms_web_login import LMSWebLogin
from task_management import TaskManagement
from site_management import SiteManagement
# from 1 import 4
# from 1 import 5
# from 1 import 6
import datetime
import os

s1 = TestLoader().loadTestsFromTestCase(LMSWebLogin)
s2 = TestLoader().loadTestsFromTestCase(TaskManagement)
s3 = TestLoader().loadTestsFromTestCase(SiteManagement)
# s4 = TestLoader().loadTestsFromTestCase(4)
# s5 = TestLoader().loadTestsFromTestCase(5)
# s6 = TestLoader().loadTestsFromTestCase(6)

# suite = TestSuite([s1, s2, s3, s4, s5, s6])
suite = TestSuite([s1, s2, s3])

daytime = datetime.datetime.now()
dt = daytime.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"LMSAutomationFunctionalTestReport"
dir = os.getcwd()
finalfile = (dir + f"/reports/LMSAutomationTestReport_"+dt+".html")
# report_title 파일열면 가장위에 있는 메인 title
runner = HTMLTestRunner(combine_reports=True, report_name=filename, report_title="LMS Automation Functional Test Report")
runner.run(suite)