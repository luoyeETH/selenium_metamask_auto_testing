from selenium import webdriver

EXTENSION_PATH = '/Users/luoye/Downloads/tools/extension_metamask.crx'
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)


driver = webdriver.Chrome(chrome_options=opt)
driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.implicitly_wait(5)
driver.find_element_by_xpath('//button[text()="开始使用"]').click()
driver.find_element_by_xpath('//button[text()="导入钱包"]').click()
driver.find_element_by_xpath('//button[text()="我同意"]').click()

# After this you will need to enter you wallet details

inputs = driver.find_elements_by_xpath('//input')
NEW_PASSWORD = 'WLj0158.'
inputs[0].send_keys('sign noodle smooth title mountain squeeze asthma tiger canal refuse sphere half below escape manual hub hockey lawn glance strike rapid pelican logic puppy')
inputs[1].send_keys(NEW_PASSWORD)
inputs[2].send_keys(NEW_PASSWORD)
driver.find_element_by_css_selector('.first-time-flow__terms').click()
driver.find_element_by_xpath('//button[text()="导入"]').click()
driver.implicitly_wait(7)
driver.find_element_by_xpath('//button[text()="全部完成"]').click()

EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

driver.execute_script("window.open('https://app.uniswap.org/#/swap');")
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="connect-wallet"]').click()
driver.find_element_by_xpath('//*[@id="connect-METAMASK"]').click()
driver.implicitly_wait(5)
# driver.execute_script("window.open('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/popup.html');")
driver.switch_to.window(driver.window_handles[2])
# driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]').click()
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
driver.implicitly_wait(2)
driver.close()
driver.switch_to.window(driver.window_handles[1])