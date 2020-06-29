from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

# All tabs that I want to automatically repopen in case chrome is unable to restore my sessions in the case of an unexpected browser shutdown

MESSENGER_URL = "https://www.messenger.com"
GOOGLE_CALENDAR_URL = "https://calendar.google.com/calendar/r/week"
GOOGLE_CHATS_URL = "https://chat.google.com/"
YOUTUBE_URL = "https://www.youtube.com/"


driver = webdriver.Chrome("./chromedriver")
# driver.maximize_window()

driver.get(MESSENGER_URL)
driver.find_element_by_id('email').send_keys(os.environ["MESSENGER_USERNAME"])
driver.find_element_by_id('pass').send_keys(os.environ["MESSENGER_PASSWORD"])
# driver.find_element_by_id('loginbutton').click()



google_calendar_tab =  '''window.open("{}","_blank");'''.format(GOOGLE_CALENDAR_URL)
driver.execute_script(google_calendar_tab)
driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_id('identifierId').send_keys(os.environ['WORK_GMAIL_USERNAME'])
driver.find_element_by_id('identifierNext').click()
driver.implicitly_wait(2)
driver.find_element_by_name('password').send_keys(os.environ['WORK_GMAIL_PASSWORD'])
# driver.find_element_by_id('passwordNext').click()



google_chats_tab = '''window.open("{}","_blank");'''.format(GOOGLE_CHATS_URL)
driver.execute_script(google_chats_tab)
driver.switch_to_window(driver.window_handles[2])
driver.find_element_by_id('identifierId').send_keys(os.environ['WORK_GMAIL_USERNAME'])
driver.find_element_by_id('identifierNext').click()
driver.implicitly_wait(2)
driver.find_element_by_name('password').send_keys(os.environ['WORK_GMAIL_PASSWORD'])
# driver.find_element_by_id('passwordNext').click()


# youtube_tab = '''window.open("{}","_blank");'''.format(YOUTUBE_URL)
# driver.execute_script(youtube_tab)
# driver.switch_to_window(driver.window_handles[3])
# driver.execute_script("document.getElementsByTagName('paper-button').item(1).click()")
# driver.find_element_by_id('identifierId').send_keys(os.environ['PERSONAL_GMAIL_USERNAME'])
# driver.find_element_by_id('identifierNext').click()
# driver.implicitly_wait(2)
# driver.find_element_by_name('password').send_keys(os.environ['PERSONAL_GMAIL_PASSWORD'])
# driver.find_element_by_id('passwordNext').click()