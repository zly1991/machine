# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Rdm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_rdm(self):
        driver = self.driver
        driver.get("https://signin.midea.com/login?service=http%3a%2f%2fitrdm.midea.com%2fmain.do")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("zhouly2")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Zhou1995.")
        driver.find_element_by_id("masForm").submit()
        driver.find_element_by_link_text(u"报表管理").click()
        driver.find_element_by_link_text(u"项目群阶段计划监控").click()
        driver.find_element_by_xpath("//div[@id='add_product_list']/div/div/div/input").click()
        driver.find_element_by_xpath(
            "//div[@id='commonProjectSelLayer']/div/div/div[2]/div/div/div[2]/table/tbody/tr/td/div/div/i").click()
        driver.find_element_by_xpath("//div[@id='layui-layer1']/div[3]/a/span").click()
        driver.find_element_by_xpath("//div[@id='add_product_list']/div/div[2]/div/input").click()
        driver.find_element_by_xpath(u"//*[contains(text(),'20190322周版本')]").click()
        driver.find_element_by_xpath(u"//*[contains(text(),'20190329周版本')]").click()
        driver.find_element_by_xpath("//div[@id='commonCheckTreeWrap']/div[2]/i").click()
        driver.find_element_by_id("btn_search").click()
        driver.find_element_by_xpath("(//a[contains(text(),'4')])[5]").click()
        driver.find_element_by_id("btn_export2").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
