from selenium import webdriver

chromeDriver = webdriver.Chrome('C:\Driver\chromedriver.exe')

chromeDriver.get('https://www.google.com')
searchBox=chromeDriver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys("Booking.com")
searchBtn=chromeDriver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchBtn.click()
searchBtn=chromeDriver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a')
searchBtn.click()
