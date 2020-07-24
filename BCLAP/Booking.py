
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
chromeDriver = webdriver.Chrome('C:\Driver\chromedriver.exe')
chromeDriver.maximize_window()
chromeDriver.get("http://demo:Test@123@test.bookingclap.com/")
searchBox = chromeDriver.find_element_by_xpath('//*[@id="home"]/form/div[1]/div/div[1]/div[1]/input[2]')
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
sleep(2)

searchBtn = chromeDriver.find_element_by_xpath('//*[@id="btn-search-hotel"]')
searchBtn.click()
sleep(2)
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
sleep(2)

EnhanceStay = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div/div[1]/div[2]/div/div/div/div[7]/div/a')
EnhanceStay.click()

EmailLogin = chromeDriver.find_element_by_xpath('//*[@id="btncontinue"]')
EmailLogin.click()
sleep(2)
Fname = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div[2]/input')
Fname.send_keys('Python')

Lname= chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[4]/div/div[2]/input')
Lname.send_keys('Test')
Email = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[5]/div/div[2]/input')
Email.send_keys('zaheen.akhtar@innovanda.com')
Mobile = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[6]/div/div[2]/input')
Mobile.send_keys('555444')

PurposeOfTravel = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[7]/div/div/label[2]/input')
PurposeOfTravel.click()
PurposeOfTravel.send_keys(Keys.TAB)
sleep(2)
#PurposeOfTravel= chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[8]/div/div[2]/input')
#PurposeOfTravel.send_keys('test')
Address = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[8]/div/div[2]/textarea')
Address.send_keys('TestAddress')
sleep(2)
chromeDriver.execute_script("window.scrollBy(0,400)", "")

City = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[9]/div/div[2]/input')
City.send_keys('TestCity')
Country = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[10]/div/div[2]/select')
sleep(2)
dropdown=Select(Country)
dropdown.select_by_index(1)

PostCode = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[11]/div/div[2]/input').send_keys('32165')
SpecialRequest = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[12]/div/div/textarea')
SpecialRequest.send_keys('test request')
sleep(2)
CheckBox = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[13]/div/div[2]/div/input[1]').is_selected()
chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[13]/div/div[2]/div/input[1]').click()

chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[15]/a').click()
sleep(2)

Card = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[2]/div/div[1]/div/div/select')
sleep(2)
dropdown = Select(Card)
dropdown.select_by_index(2)

CardNum = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[2]/div/div[2]/div/div/input')
sleep(2)
CardNum.send_keys('5555555555554444')
ExpMonth = chromeDriver.find_element_by_xpath('//*[@id="ExpiryMonth"]')
sleep(2)
drp = Select(ExpMonth)
drp.select_by_index(2)

ExpYear = chromeDriver.find_element_by_xpath('//*[@id="ExpiryYear"]')
sleep(2)
drp = Select(ExpYear)
drp.select_by_index(2)
sleep(2)

CardHolderName = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[2]/div/div[5]/div/div/input')
CardHolderName.send_keys('test')

CVV = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[2]/div/div[6]/div/div/input')
CVV.send_keys('111')

CompleteBooking = chromeDriver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[6]/a')
CompleteBooking.click()
