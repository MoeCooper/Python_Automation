from selenium import webdriver


chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.github.com/login')

get_username = chrome_browser.find_element_by_id('login_field')
get_username.clear()
get_username.send_keys('jc70240@gmail.com')

get_password = chrome_browser.find_element_by_id('password')
get_password.clear()
get_password.send_keys('')

login_button = chrome_browser.find_element_by_name('commit').click()

select_new = chrome_browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a').click()
