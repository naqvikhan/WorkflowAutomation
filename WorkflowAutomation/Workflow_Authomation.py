from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import keys

def cred (credentials):

    browser = webdriver.Chrome(executable_path='/Users/naqvi/Desktop/WorkflowAutomation/chromedriver')

    # for accessing WhenToWork

    browser.get('https://whentowork.com/logins.htm')

    browser.find_element_by_xpath('//*[@id="username"]').send_keys(cred(credentials["w2w_Username"]))

    browser.find_element_by_xpath('//*[@id="password"]').send_keys(cred(credentials["w2w_Password"]))

    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div/button').click()

    browser.find_element_by_xpath('//*[@id="emptop"]/tbody/tr/td[8]').click()

    browser.implicitly_wait(3)

    # for accessing Amazon Connect

    browser.execute_script("window.open('https://utd-oit-helpdesk.awsapps.com/connect/homeopen', 'new window')")

    browser.implicitly_wait(3)

    browser.find_element_by_xpath('//*[@id="wdc_username"]').send_keys(cred(credentials["amazonConnect_Username"]))

    browser.find_element_by_xpath('//*[@id="wdc_password"]').send_keys(cred(credentials["amazonConnect_Password"]))

    browser.find_element_by_xpath('/*[@id="wdc_login_button"]').click()

    # for opening Microsoft Teams and Microsoft Remote Desktop

import subprocess
subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Microsoft Remote Desktop.app"]
        )

subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Microsoft Teams.app"]
        )



