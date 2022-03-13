import selenium_metamask_automation as auto
import time
import wallet


# 指定chromedriver路径
driverPath = '/Users/luoye/Downloads/tools/chromedriver'
driver = auto.launchSeleniumWebdriver(driverPath)
# 打开Uniswap
driver.get('https://app.uniswap.org/#/swap')
# 助记词明文导入(不建议)
# seed_phrase = 'sign noodle smooth title mountain squeeze asthma tiger canal refuse sphere half below escape manual hub hockey lawn glance strike rapid pelican logic puppy'
# 从文件按地址导入助记词
filename = '20220312_eth_uniswap_10.xlsx'
address = '0xfd10b2f7a0cc10065f8e5f0e54eb288134fde7af'
seed_phrase = wallet.getSeedPhrase(filename, address)
password = 'TestPassword'
# 导入助记词
auto.metamaskSetup(seed_phrase, password)
networkName = 'Kovan 测试网络'
# 切换到测试网络
auto.changeMetamaskNetwork(networkName)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.find_element_by_xpath('//*[@id="connect-wallet"]').click()
driver.find_element_by_xpath('//*[@id="connect-METAMASK"]').click()
# 连接钱包
auto.connectToWebsite()
time.sleep(5)
driver.find_element_by_xpath('//span[text()="选择代币"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div[text()="DAI"]').click()
time.sleep(5)
inputs = driver.find_elements_by_xpath('//input')
inputs[0].send_keys('0.001')
time.sleep(8)
driver.find_element_by_xpath('//*[@id="swap-button"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="confirm-swap-or-send"]').click()
time.sleep(10)
# 确认交易
auto.confirmApprovalFromMetamask()
time.sleep(2)
driver.find_element_by_xpath('//div[text()="关闭"]').click()
