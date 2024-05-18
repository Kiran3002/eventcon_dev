# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestContactus():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_contactus(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "Contact Us").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("kiran kumar")
    self.driver.find_element(By.ID, "email").send_keys("kirankumar300213@gmail.com")
    self.driver.find_element(By.ID, "subject").click()
    self.driver.find_element(By.ID, "subject").send_keys("hello")
    self.driver.find_element(By.ID, "message").click()
    self.driver.find_element(By.ID, "message").send_keys("good morning")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
  
