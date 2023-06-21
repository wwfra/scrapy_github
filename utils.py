# -*- coding: utf-8 -*-
"""
作者: Liwz
日期: 2023/06/13
"""
import json
from selenium import webdriver


def create_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=options,
                               executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator,"webdriver",{get: () => undefined})'}
    )
    return browser