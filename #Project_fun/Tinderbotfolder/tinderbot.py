from selenium import webdriver
from time import sleep

from secrets import username, password

#All the sleeps are used due to internet repsoniveness, the faster the webpage loads the less sleep you need.

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(3)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(2)
        self.driver.switch_to_window(base_window)
        sleep(2)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        sleep(2)
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        sleep(2)
        like_btn.click()

    def dislike(self):
        sleep(2)
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        sleep(2)
        dislike_btn.click()

    def auto_swipe(self):
        from random import random
        i = 0
        while i <= 80:
            print(i)
            sleep(0.5)
            try:
                rand = random()
                if rand < 0.65 :
                    self.like()
                    i += 1
                else:
                    self.dislike()
                    i += 1
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        sleep(2)
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        sleep(2)
        popup_3.click()

    def close_match(self):
        match_counter = 0
        sleep(2)
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        sleep(2)
        match_popup.click()
        match_counter += 1
        print('You got a new match!!, total this run = ' + match_counter)


bot = TinderBot()
bot.login()
sleep(3)
bot.auto_swipe()