#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver

class TestConfig():
    driver = 'driver'
    check_loop_count = 3
    is_passed = False
    is_finished = False
    is_initialized = False
    res = []
    port = None
    sdkver = None
    dname = None
    udid = None
    auto = None
    ratio = None
    os = None
    user_name = None
    password = None

TEST_CONFIG = TestConfig()

def initialize_bp(target, argv):
    TEST_CONFIG.port = "4723"
    TEST_CONFIG.sdkver = "13"
    TEST_CONFIG.dname = "Galaxy S22+"
    TEST_CONFIG.udid = "RFCT215PARN"
    TEST_CONFIG.auto = "UiAutomator2"
    TEST_CONFIG.ratio = "2340 x 1080"
    TEST_CONFIG.os = "Android"
    TEST_CONFIG.user_name = "junhyun.kyung"
    TEST_CONFIG.password = "junhyun.kyung"
    app = '/Users/122d6424/Git/Kurly/APKs/kurly.apk'

    TEST_CONFIG.driver = webdriver.Remote(
        command_executor=f'http://127.0.0.1:{TEST_CONFIG.port}/wd/hub',
        desired_capabilities={
            'app': app,
            "platformName": "Android",
            "appium:automationName": TEST_CONFIG.auto,
            "platformVersion": TEST_CONFIG.sdkver,
            "deviceName": TEST_CONFIG.dname,
            "appium:udid": TEST_CONFIG.udid,
            "newCommandTimeout": 10000,
            "appium:noReset": "true"
    }
    )
