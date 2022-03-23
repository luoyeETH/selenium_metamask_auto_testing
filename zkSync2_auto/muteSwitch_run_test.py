import selenium_metamask_automation as auto
import time
import wallet
import random
from selenium.common.exceptions import NoSuchElementException
from config import global_config


def runMuteSwitchTestnet(addr):
    # 指定chromedriver路径
    driver_path = global_config.get('path', 'driver_path').strip()
    driver = auto.launchSeleniumWebdriver(driver_path)
    wait_time = global_config.get('config', 'time')
    driver.implicitly_wait(wait_time)

    def init():
        address = addr
        seed_phrase = wallet.getSeedPhraseV2(address)
        password = 'TestPassword'
        # 导入助记词
        auto.metamaskSetup(seed_phrase, password)
        # 打开MuteSwitch测试网
        driver.get('https://testnet.switch.mute.io/')
        time.sleep(3)
        auto.connectToWebsite()
        auto.addAndChangeNetwork()
        print('init success')

    # Swap TokenA for TokenB
    def swap(a, b):
        token_x = a
        token_y = b
        driver.find_element_by_xpath("//button[text()='Select token']").click()
        driver.find_element_by_xpath("//p[text()='" + token_x + "']").click()
        driver.find_element_by_xpath("//button[text()='Select token']").click()
        driver.find_element_by_xpath("//p[text()='" + token_y + "']").click()
        time.sleep(3)
        inputs = driver.find_elements_by_xpath('//input')
        value = random.randint(20, 30)
        inputs[0].send_keys(value)

        while True:
            try:
                element = driver.find_element_by_xpath('//button[text()="Approve"]')
            except NoSuchElementException:
                print("Swap")
                driver.find_element_by_xpath('//button[text()="Swap"]').click()
                auto.signConfirm()
                driver.find_element_by_xpath("//*[@alt='Close']").click()
                break
            else:
                print("Approve")
                driver.find_element_by_xpath('//button[text()="Approve"]').click()
                auto.signConfirm()
                auto.signConfirm()
                driver.find_element_by_xpath("//*[@alt='Close']").click()
                break
        print('run swap success')

    # Add Liquidity TokenA and TokenB
    def addLP(a, b):
        token_x = a
        token_y = b
        driver.find_element_by_xpath("//a[text()='Pool']").click()
        driver.find_element_by_xpath("//button[text()='Add Liquidity']").click()
        driver.find_element_by_xpath("//button[text()='Select token']").click()
        driver.find_element_by_xpath("(//p[text()='" + token_x + "'])[last()]").click()
        driver.find_element_by_xpath("//button[text()='Select token']").click()
        driver.find_element_by_xpath("//p[text()='" + token_y + "']").click()
        time.sleep(3)
        inputs = driver.find_elements_by_xpath('//input')
        value = random.randint(10, 20)
        inputs[0].send_keys(value)
        time.sleep(5)
        driver.find_element_by_xpath('//button[text()="Supply"]').click()
        auto.signConfirm()
        auto.signConfirm()
        driver.find_element_by_xpath("//*[@alt='Close']").click()
        print('run add LP success')

    def farming():
        driver.find_element_by_xpath("//a[text()='Farming']").click()
        driver.find_element_by_xpath('//*[@id="app"]/main/div/div[3]/div/div/div[1]').click()
        while True:
            try:
                element = driver.find_element_by_xpath("//button[text()='Approve']")
            except NoSuchElementException:
                driver.find_element_by_xpath('//button[text()="Harvest"]').click()
                time.sleep(3)
                screenshot_path = global_config.get('path', 'result_path').strip()
                driver.get_screenshot_as_file(str(screenshot_path) + addr + '.png')
                break
            else:
                print("Approve")
                driver.find_element_by_xpath("//button[text()='Approve']").click()
                auto.signConfirm()
                driver.find_element_by_xpath('//button[text()="MAX"]').click()
                driver.find_element_by_xpath('//button[text()="Deposit"]').click()
                auto.signConfirm()
                auto.signConfirm()
                driver.find_element_by_xpath('//button[text()="Harvest"]').click()
                screenshot_path = global_config.get('path', 'result_path').strip()
                driver.get_screenshot_as_file(str(screenshot_path) + addr + '.png')
                break

    init()
    token_list_a = ['DAI', 'USD Coin', 'Chainlink']
    token_list_b = ['Ethereum', 'Wrapped Bitcoin']
    token_a = random.choice(token_list_a)
    token_b = random.choice(token_list_b)
    dai = 'DAI'
    eth = 'ETH'
    swap(token_a, token_b)
    addLP(dai, eth)
    farming()
    driver.quit()


