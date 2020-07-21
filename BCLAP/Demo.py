from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

chromeDriver = webdriver.Chrome('C:\Driver\chromedriver.exe')

chromeDriver.get('https://www.google.com')
searchBox=chromeDriver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys("Booking.com")
searchBtn=chromeDriver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchBtn.click()
searchBtn=chromeDriver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a')
searchBtn.click()
chromeDriver.find_element_by_xpath('//*[@id="ss"]').send_keys('London')
sleep(2)
searchBox.send_keys(Keys.ENTER)
searchBox.send_keys(Keys.TAB)
