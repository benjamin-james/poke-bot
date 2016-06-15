#!/usr/bin/env python3
import configure
import time
from selenium import webdriver

m_driver = webdriver.PhantomJS()


def screenshot(driver=m_driver):
        string = str(time.strftime('%Y-%m-%d-%H%M%S.png'))
        driver.get_screenshot_as_png(string)


def login(driver=m_driver,
          username=configure.username, passwd=configure.passwd):
        driver.get('https://www.facebook.com')

        driver.find_element_by_id('email').clear()
        email = driver.find_element_by_id('email')
        email.send_keys(username)

        driver.find_element_by_id('pass').clear()
        password = driver.find_element_by_id('pass')
        password.send_keys(passwd)
        password.send_keys(webdriver.common.keys.Keys.RETURN)


def check_pokes(driver=m_driver):
        driver.get('http://www.facebook.com/pokes')
        buttons = driver.find_elements_by_link_text('Poke Back')
        for button in buttons:
                button.click()
                screenshot(driver)

if __name__ == "__main__":
        try:
                login()
                print("Logging in")
                while True:
                        check_pokes()
                        time.sleep(configure.delay)
        except:
                print("Error, retrying login")
                m_driver = webdriver.PhantomJS()
                login()
                pass
