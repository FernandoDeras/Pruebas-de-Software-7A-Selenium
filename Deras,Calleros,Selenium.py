from selenium import webdriver
import time

driver= webdriver.Chrome(executable_path=r'C:\Users\ferna\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://demo-store.seleniumacademy.com/')
Profile = driver.find_element_by_css_selector('a.skip-link.skip-account')
Profile.click()
Register= driver.find_element_by_link_text('Register')
Register.click()
search_box_firstname= driver.find_element_by_id('firstname')
search_box_firstname.send_keys('Fernando ')
search_box_middlename= driver.find_element_by_id('middlename')
search_box_middlename.send_keys('José ')
search_box_lastname= driver.find_element_by_id('lastname')
search_box_lastname.send_keys('Zapata Rodriguez')
search_box_email_address= driver.find_element_by_id('email_address')
search_box_email_address.send_keys('estoesunaprueba@gmail.com')
search_box_password= driver.find_element_by_id('password')
search_box_password.send_keys('charmander22')
search_box_confirmation= driver.find_element_by_id('confirmation')
search_box_confirmation.send_keys('charmander22')
button_is_subscribed= driver.find_element_by_name('is_subscribed').click()
button_submit = driver.find_element_by_xpath("//button[@title='Register'][@type='submit'][@class='button']").click()



time.sleep(300)
driver.quit()