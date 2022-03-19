import selenium_metamask_automation as auto
import time
import wallet
import random


def runTest(filename, addr):
    # 指定chromedriver路径
    driver_path = '/Users/luoye/Downloads/tools/chromedriver'
    driver = auto.launchSeleniumWebdriver(driver_path)
    # 打开zkSync2.0测试网
    driver.get('https://portal.zksync.io/')
    address = addr
    seed_phrase = wallet.getSeedPhrase(filename, address)
    password = 'TestPassword'
    # 导入助记词
    auto.metamaskSetup(seed_phrase, password)
    network_name = 'Goerli 测试网络'
    # 切换到测试网络
    auto.changeMetamaskNetwork(network_name)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    driver.find_element_by_xpath('//span[text()="MetaMask"]').click()
    # 连接钱包
    auto.connectToWebsite()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/nav/div[1]/a[2]').click()

    # Faucet
    time.sleep(5)
    driver.find_element_by_xpath("//a[text()='Faucet']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='Request Funds from Faucet']").click()
    time.sleep(20)
    driver.find_element_by_xpath("//button[text()=' OK ']").click()

    # Deposit
    time.sleep(5)
    driver.find_element_by_xpath("//a[text()='Deposit']").click()
    time.sleep(10)
    inputs = driver.find_elements_by_xpath('//input')
    inputs[0].send_keys('0.01')
    time.sleep(8)
    driver.find_element_by_xpath("//button[text()='Deposit']").click()
    time.sleep(15)
    # 确认交易
    auto.confirmApprovalFromMetamask()
    time.sleep(15)

    # Withdraw
    time.sleep(5)
    driver.find_element_by_xpath("//a[text()='Withdraw']").click()
    time.sleep(15)
    driver.find_element_by_xpath("//p[text()='ETH']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//p[text()='USDC']").click()
    time.sleep(5)
    inputs = driver.find_elements_by_xpath('//input')
    value = random.randint(1, 20)
    inputs[0].send_keys(value)
    time.sleep(5)
    driver.find_element_by_xpath("//p[text()='ETH']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//p[text()='LINK']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[text()='Withdraw']").click()
    time.sleep(10)
    auto.addAndChangeNetwork()
    time.sleep(3)
    auto.signConfirm()
    time.sleep(15)
    driver.find_element_by_xpath("//button[text()='Back to Balances']").click()
    # 退出
    time.sleep(10)
    driver.get_screenshot_as_file('/Users/luoye/Downloads/TestNetwork/zkSync2/' + address + '.png')
    driver.quit()


# filename = '20220313_eth_zkSync2_50.xlsx'
# address_list = wallet.getAddress(filename)
# result = open('/Users/luoye/Downloads/TestNetwork/zkSync2/result.txt', mode='a', encoding='utf-8')
# for i in range(1, 51):
#     address = address_list[i]
#     try:
#         runTest(filename, address)
#     except Exception as e:
#         print(e)
#         print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行失败")
#         print(address + " run test failed", file=result)
#         continue
#     else:
#         print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行成功")
#         print(address + " run test success", file=result)
