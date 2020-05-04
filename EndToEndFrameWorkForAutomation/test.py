from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# chrome_path="C://Users//harisha//PycharmProjects//EndToEndFrameWorkForAutomation//chromedriver.exe"
chrome_path= "Drivers/chromedriver.exe"
driver=Chrome(executable_path=chrome_path)
driver.get("http://thetestingworld.com/testings")

# maximize window
driver.maximize_window()
# driver.find_elements_by_xpath("//input[@id='tab2']").click()

# driver.find_element_by_name("fld_username").send_keys("harish")
# driver.find_element_by_name('fld_email').send_keys("harishram3@gmail.com")
# driver.find_element_by_name('fld_password').send_keys("Test@12345")
# driver.find_element_by_name('fld_cpassword').send_keys("Test@12345")
# driver.find_element_by_id('datepicker').send_keys(" 04/08/2020")
# driver.find_element_by_name('phone').send_keys("9880647735")
# driver.find_element_by_name('address').send_keys("ayodya")
# driver.find_element_by_xpath("//input[@value='home']").click()
#
# selectgender=Select(driver.find_element_by_name('sex'))
# selectgender.select_by_visible_text("Male")
#
# selectCountry = Select(driver.find_element_by_xpath("//*[@id='countryId']"))
# selectCountry.select_by_visible_text("India")
#
# # selectState=Select(driver.find_element_by_xpath("//*[@id='stateId']"))
# # selectState.select_by_visible_text("Karnataka")
# #
# # selectState=Select(driver.find_element_by_xpath("//*[@id='cityId']"))
# # selectState.select_by_visible_text("Tumkur")
#
# driver.find_element_by_name("zip").send_keys("572137")
# driver.find_element_by_name('terms').click()
# driver.find_element_by_xpath("//input[@type='submit']").click()
# success=driver.find_element_by_class_name('vd_alert-icon')
# assert success.text=='User is successfully Register. Now You can Login',"text is not present"
# #  User is successfully Register. Now You can Login
#
# # to close the browser
# driver.close()