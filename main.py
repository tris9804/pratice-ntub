import time
import re

from datetime import datetime
from selenium import webdriver

def get_password(filename = 'key.txt'):
    with open(filename, 'r') as f:
        password = f.read().strip() 
    return password



# html = driver.page_source
# check_code = html.split('CheckCode=\'')[-1].split('\'')[0]

def get_check_code(html):
    check_code = re.search(r'CheckCode=\'(?P<code>\d*)\'', html).group('code')
    return check_code

driver = webdriver.Chrome()

driver.get('http://ntcbadm1.ntub.edu.tw/')

driver.find_element_by_id('UserID').send_keys('10736021')
driver.find_element_by_id('PWD').send_keys(get_password())
driver.find_element_by_id('txtCheckCode').send_keys(get_check_code(driver.page_source))
driver.find_element_by_id('loginbtn').click()


time.sleep(3)
driver.find_element_by_class_name('ThemePanelMainItem').click()

time.sleep(3)
# driver.find_element_by_xpath('//*[@id="div_content"]/table/tbody/tr[3]/td[5]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/a').click()
driver.find_element_by_link_text('個人請假缺曠記錄').click()

time.sleep(3)
now = datatime.now().strftime('%Y-%m-%d-%H-%M-%S')
driver.save_screenshot(f'{now}.png')

time.sleep(3)
driver.close()

token = ''
request.get = (f'https://api.telegram.org/bot{token}/sendMessage', params = {
    'chat_id':'',
    'text': '{} Done',
})

request.post = (
    f'https://api.telegram.org/bot{now}/sendPhoto', 
    params = {
        'chat_id':'',
    }, 
    files = {
        'photo': open(f'{now}.png', rb)
    })