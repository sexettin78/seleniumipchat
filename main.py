from selenium import webdriver
import time
pat = input("Web driver yolu giriniz: ")
driver_path = (pat)

browser = webdriver.Chrome(executable_path=driver_path)

browser.get("http://ipchat.rf.gd/")
time.sleep(4)
yazi = browser.find_element_by_xpath("/html/body/form/font[1]/input")
yazi.send_keys("SELENYUM TEST")
time.sleep(2)
browser.find_element_by_xpath("/html/body/form/button/font").click()
