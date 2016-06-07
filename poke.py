#!/usr/bin/env python3
import time
import configure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
m_driver = webdriver.PhantomJS()


def login(driver=m_driver,
          username=configure.username, passwd=configure.passwd):
        driver.get('https://www.facebook.com')

        driver.find_element_by_id('email').clear()
        email = driver.find_element_by_id('email')
        email.send_keys(username)

        driver.find_element_by_id('pass').clear()
        password = driver.find_element_by_id('pass')
        password.send_keys(passwd)
        password.send_keys(Keys.RETURN)


def check_pokes(driver=m_driver):
        driver.get('http://www.facebook.com/pokes')
        buttons = driver.find_elements_by_link_text('Poke Back')
        for button in buttons:
                button.click()
                print("Poked back")

if __name__ == "__main__":
        try:
                login()
                while True:
                        check_pokes()
                        time.sleep(configure.delay)
        except:
                print("Error")
                m_driver = webdriver.PhantomJS()
                login()
                pass
