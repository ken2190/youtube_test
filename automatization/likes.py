# Local imports
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import WEBDRIVER_PREFERENCES
from .gologin_test import GoLogin

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import getpass

# Other imports
import os
import sys
from time import sleep


class YoutubeLiker:
    def __init__(self, account_number):
        self.url = 'https://accounts.google.com/signin/v2/identifier'
        # Options.
        # self.ua = UserAgent()
        u_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        if account_number == 0:
            self.profile = webdriver.FirefoxProfile('C:/Users/nikit/AppData/Roaming/Mozilla/Firefox/Profiles/1c5e4kyj.default-release')
        elif account_number == 1:
            self.profile = webdriver.FirefoxProfile('C:/Users/nikit/AppData/Roaming/Mozilla/Firefox/Profiles/the_second')
        elif account_number == 2:
            self.profile = webdriver.FirefoxProfile('C:/Users/nikit/AppData/Roaming/Mozilla/Firefox/Profiles/the_third')
        self.profile.set_preference('dom.webdriver.enabled', False)
        self.profile.set_preference('useAutomationExtension', False)
        self.profile.update_preferences()
        self.desired = DesiredCapabilities.FIREFOX
        self.driver = webdriver.Firefox(
            firefox_profile=self.profile,
            desired_capabilities=self.desired,
            executable_path=os.getcwd()+'/automatization/geckodriver.exe'
        )
        self.wait = WebDriverWait(self.driver, 5)

    def login(self, mail, passwd):
        # self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
        # sleep(3)
        # self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/button[1]').click()
        self.driver.get(self.url)
        a = input('>>> ')
        # try:
        #     sleep(99999)
        #     print(self.driver.current_url)
        #     mail_field = self.wait.until(ec.presence_of_element_located((By.ID, 'identifierId')))
        #     mail_field.click()
        #     mail_field.send_keys(mail)
        #     sleep(1)
        #     mail_field.send_keys(Keys.ENTER)
        #     # submit_first = self.wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
        #     # submit_first.click()
        #     if 'denied' in self.driver.current_url:
        #         divs = self.driver.find_elements_by_tag_name('div')
        #         for div in divs:
        #             print(div.text)
        #             sleep(1)

        #     sleep(3)
        #     print(self.driver.current_url)
        #     passwd_field = self.wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')))
        #     passwd_field.click()
        #     # passwd_field.send_keys(passwd)
        #     # submit_second = self.wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
        #     # submit_second.click()
        #     chains = ActionChains(self.driver)
        #     chains.send_keys(passwd + Keys.ENTER).perform()
        #     sleep(1)

        #     try:
        #         phone_code = self.wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/span/figure/samp')))
        #         print(phone_code.text)
        #         a = input('>>> ')
        #     except Exception as ex:
        #         print(ex)
        # except Exception as ex:
        #     print(ex)
        # try:
        #     not_now = self.wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/c-wiz/div/div/div/div[2]/div[4]/div[1]/button/span')))
        #     not_now.click()
        # except Exception as ex:
        #     pass
        # try:
        #     update = self.wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/span/span')))
        #     update.click()
        # except Exception as ex:
        #     pass
        # try:
        #     welcome_msg = self.wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[3]/div/div/header/h1')))
        #     # welcome_msg = self.driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[3]/div/div/header/h1')
        #     print(welcome_msg.text)
        #     print('Аккаунт залогинен')
        # except Exception as ex:
        #     pass

    def like_the_video(self, id_of_the_video, text_for_the_video):
        youtube_url = 'https://www.youtube.com/watch?v=' + id_of_the_video
        self.driver.get(youtube_url)
        sleep(5)
        try:
            like_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon')))
            like_btn.click()
        except Exception as ex:
            print(ex)
        try:
            sleep(2)
            self.driver.execute_script('window.scrollBy(0, 600)', '')
            comment_field = self.wait.until(ec.presence_of_element_located((By.ID, 'simplebox-placeholder')))
            comment_field.click()

            sleep(1)
            chains = ActionChains(self.driver)
            chains.send_keys(text_for_the_video).perform()
        except Exception as ex:
            pass

        submit_btn = self.driver.find_elements_by_id('text')
        for submit in submit_btn:
            if submit.text == 'ОСТАВИТЬ КОММЕНТАРИЙ':
                submit.click()


if __name__ == '__main__':
    pass
