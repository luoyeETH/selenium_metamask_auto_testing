import selenium_metamask_automation as auto
import time
import wallet
import random
from config import global_config


def runTest(addr):
    # 指定chromedriver路径
    driver_path = global_config.get('path', 'driver_path').strip()
    driver = auto.launchSeleniumWebdriver(driver_path)
    # 打开zkSync2.0测试网
    wait_time = global_config.get('config', 'time')
    driver.implicitly_wait(wait_time)
    driver.get('https://portal.zksync.io/')
    address = addr
    seed_phrase = wallet.getSeedPhraseV2(address)
    password = 'TestPassword'
    # 导入助记词
    auto.metamaskSetup(seed_phrase, password)
    network_name = 'Goerli 测试网络'
    # 切换到测试网络
    auto.changeMetamaskNetwork(network_name)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_xpath('//span[text()="MetaMask"]').click()
    # 连接钱包
    auto.connectToWebsite()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/nav/div[1]/a[2]').click()

    # Faucet
    driver.find_element_by_xpath("//a[text()='Faucet']").click()
    time.sleep(3)
    # 此处获取测试币可能受zkSync影响造成 失败/无法实时到账
    driver.find_element_by_xpath("//button[text()='Request Funds from Faucet']").click()
    driver.find_element_by_xpath("//button[text()=' OK ']").click()
    print('Faucet Success')

    # Deposit
    driver.find_element_by_xpath("//a[text()='Deposit']").click()
    time.sleep(5)
    inputs = driver.find_elements_by_xpath('//input')
    inputs[0].send_keys('0.01')
    driver.find_element_by_xpath("//button[text()='Deposit']").click()
    # 确认交易
    auto.confirmApprovalFromMetamask()
    print('Deposit Success')

    # Withdraw
    driver.find_element_by_xpath("//a[text()='Withdraw']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//p[text()='ETH']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//p[text()='USDC']").click()
    time.sleep(5)
    inputs = driver.find_elements_by_xpath('//input')
    value = random.randint(1, 20)
    inputs[0].send_keys(value)
    driver.find_element_by_xpath("//p[text()='ETH']").click()
    driver.find_element_by_xpath("//p[text()='LINK']").click()
    driver.find_element_by_xpath("//button[text()='Withdraw']").click()
    auto.addAndChangeNetwork()
    auto.signConfirm()
    print('Withdraw Success')

    # Transfer
    driver.find_element_by_xpath("//a[text()=' Wallet']").click()
    driver.find_element_by_xpath("//a[text()='Transfer']").click()
    time.sleep(3)
    inputs = driver.find_elements_by_xpath('//input')
    transfer_addr = global_config.get('config', 'transfer_address').strip()
    inputs[0].send_keys(transfer_addr)
    driver.find_element_by_xpath("//p[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//p[text()='USDC']").click()
    time.sleep(1)
    inputs[1].send_keys('5')
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='Transfer']").click()
    auto.signConfirm()
    print('Transfer Success')

    # 退出
    screenshot_path = global_config.get('path', 'result_path').strip()
    driver.get_screenshot_as_file(str(screenshot_path) + address + '.png')
    driver.quit()
