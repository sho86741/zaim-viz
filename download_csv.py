# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
import yaml
from time import sleep
import os

cur_dir = os.path.dirname(__file__)
with open('%s/setting.yaml' % cur_dir, 'r') as yml:
    config = yaml.safe_load(yml)

user = config['config']['user']
pw = config['config']['pw']
from_year = config['config']['from_date'][0:4]
from_month = config['config']['from_date'][4:6]
from_day = config['config']['from_date'][6:8]
if config['config']['to_date'] != "":
    to_year = config['config']['to_date'][0:4]
    to_month = config['config']['to_date'][4:6]
    to_day = config['config']['to_date'][6:8]
else:
    to_year = '%04d' % datetime.now().year
    to_month = '%02d' % datetime.now().month
    to_day = '%02d' % datetime.now().day

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

b = Browser(webdriver.Chrome(options=options))

b.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
b.execute("send_command", {
    'cmd': 'Page.setDownloadBehavior',
    'params': {
        'behavior': 'allow',
        'downloadPath': cur_dir
     }
})

b.get('https://auth.zaim.net/')

b.sync_send_keys((By.ID, 'UserEmail'), user)
b.sync_send_keys((By.ID, 'UserPassword'), pw)
b.find_element_by_xpath('//*[@id="UserLoginForm"]/div[4]/input').click()

b.get('https://content.zaim.net/home/money')

b.find_element_by_xpath('//*[@id="main"]/div/div[2]/ul/li/h4').click()
Select(b.wait_element('MoneyStartDateYear')).select_by_value(from_year)
Select(b.wait_element('MoneyStartDateMonth')).select_by_value(from_month)
Select(b.wait_element('MoneyStartDateDay')).select_by_value(from_day)
Select(b.wait_element('MoneyEndDateYear')).select_by_value(to_year)
Select(b.wait_element('MoneyEndDateMonth')).select_by_value(to_month)
Select(b.wait_element('MoneyEndDateDay')).select_by_value(to_day)
Select(b.wait_element('MoneyCharset')).select_by_value('utf8')

b.find_element_by_xpath('//*[@id="MoneyHomeIndexForm"]/div[5]/input').click()

sleep(10)

b.quit()
