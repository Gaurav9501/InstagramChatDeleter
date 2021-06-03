from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Controller
import time;
import pyautogui
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)
usernamePath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
passwordPath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
loginPath = '//*[@id="loginForm"]/div/div[3]/button/div'

search  = driver.find_element_by_xpath(usernamePath)
search.send_keys("gauravagarwal9501@gmail.com")
time.sleep(2)
search  = driver.find_element_by_xpath(passwordPath)
search.send_keys("activa9501")
time.sleep(2)
search  = driver.find_element_by_xpath(loginPath)
search.click()

time.sleep(4)
search  = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
search.click()

time.sleep(2)
search  = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[2]')
search.click()
time.sleep(2)

while(True):
	search  = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div')
	search.click()

	time.sleep(2)
	search  = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button')
	search.click()

	time.sleep(2)
	search  = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button/div')
	search.click()

	time.sleep(2)
	search  = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[1]')
	search.click()
	time.sleep(3)
