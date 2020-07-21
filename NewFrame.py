
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
chromeDriver = webdriver.Chrome('C:\Driver\chromedriver.exe')
chromeDriver.maximize_window()
chromeDriver.get("http://demo:Test@123@test.bookingclap.com/")
searchBox= chromeDriver.find_element_by_xpath('//*[@id="home"]/form/div[1]/div/div[1]/div[1]/input[2]')
# For Dynamic search
# searchInput=input("Enter Location")
# searchBox.send_keys(searchInput)
searchBox.send_keys('London')
sleep(2)
# Select the first suggestion
searchBox.send_keys(Keys.ENTER)
searchBox.send_keys(Keys.TAB)
# Select the next suggestion from list
# searchBox.send_keys(Keys.DOWN)
# Keys.TAB or Keys.Enter we can use
# searchBox.send_keys(Keys.TAB)
searchBox = chromeDriver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[4]/a')
searchBox.send_keys(Keys.ENTER)
searchBtn = chromeDriver.find_element_by_xpath('//*[@id="btn-search-hotel"]')
searchBtn.click()
searchBox = chromeDriver.find_element_by_xpath('//*[@id="booknowbtn_10498"]')
searchBox.click()

sleep(2)
allTabs = chromeDriver.window_handles
#print(allTabs)
for tab in allTabs:
    chromeDriver.switch_to.window(tab)
    #print(chromeDriver.current_url)
    if (chromeDriver.current_url== 'http://test.bookingclap.com/en/hotels/gb/london/london-tower-suites?location=London,%20Greater%20London,%20United%20Kingdom&locationtype=Hotel&lid=2&checkin=22%20Jul%202020&checkout=23%20Jul%202020&RoomsSelector=1-0&rateaccesscode=#choose-room'):
        Room_No = chromeDriver.find_element_by_xpath('//*[@id="choose-room"]/div[1]/div[1]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[6]/select')
        drp = Select(Room_No)
        drp.select_by_index(1)
ChooseRoom = chromeDriver.find_element_by_xpath('//*[@id="choose-room"]/div[1]/div[1]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/button')
ChooseRoom.click()
sleep(1)
EnhanceStay = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div/div[1]/div[2]/div/div/div/div[7]/div/a')
EnhanceStay.click()

EmailLogin = chromeDriver.find_element_by_xpath('//*[@id="btncontinue"]')
EmailLogin.click()

