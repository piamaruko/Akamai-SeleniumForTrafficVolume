#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://control.akamai.com/homeng/view/main')
sleep(3)

#browser.close()
# Luna login
pass_wd = browser.find_element_by_id('password')
pass_wd.send_keys('')
pass_wd.submit()

# Search Account
browser.get('https://control.akamai.com/search/advanced/')
account_name = browser.find_element_by_name('q')
account_name.send_keys('SUBARU CORPORATION in:Accounts by:Name')
account_name.submit()
sleep(3)
browser.find_element_by_link_text("SUBARU CORPORATION").click()
sleep(3)

# Choose User traffic 
browser.find_element_by_link_text("モニター").click()
browser.find_element_by_link_text("ユーザートラフィック").click()
sleep(5)

# Change CP code and date range
browser.find_element_by_id("report-change").click()
# for www.subaru-msm.com
select = Select(browser.find_element_by_name('cpcode'))
select.deselect_all()
select.select_by_value("547552")
browser.find_element_by_xpath('//*[@id="customSelector"]/div[2]/div[5]/label/input').click()
browser.find_element_by_xpath('//*[@id="cpcodeReportForm_start"]').click()


browser.find_element_by_class_name('calnavleft').click()
#browser.find_element_by_id('yui-gen47_t_cell0').click()
#browser.find_element_by_xpath('//*[@id="yui-gen47_t_cell0"]/a').click()
browser.find_element_by_link_text('1').click()
browser.find_element_by_name('end_date').click()
browser.find_element_by_link_text('1').click()
browser.find_element_by_name('ok').click()

# change from number of hit to volume
sleep(3)
pulldown = browser.find_element_by_xpath('//*[@id="top-traffic-graphs"]/div/div[1]/span[2]/select')
pulldown_select = Select(pulldown)
sleep(3)
pulldown_select.select_by_value('エッジ帯域幅')


# for www.subaru.co.jp
# for www.subaru.jp

browser.execute_script("window.scrollTo(0, 10)")

browser.set_window_size(720, 720)
browser.save_screenshot("/Users/hioka/work/python/screen.png")
exit()






