from selenium.webdriver import Chrome

def Start_browser():
    print("Starting the test case")
    global driver
    chrome_path = "./Drivers//chrome.exe"
    driver = Chrome(executable_path=chrome_path)
    return  driver

def CLose_Browser():
    driver.close()