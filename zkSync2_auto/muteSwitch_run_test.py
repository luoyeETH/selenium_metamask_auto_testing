import selenium_metamask_automation as auto
import time
import wallet
import random
from selenium.common.exceptions import NoSuchElementException


def runMuteSwitchTestnet(addr):
    # 指定chromedriver路径
    driver_path = '/Users/luoye/Downloads/tools/chromedriver'
    driver = auto.launchSeleniumWebdriver(driver_path)

    def init():
        address = addr
        seed_phrase = wallet.getSeedPhrase(filename, address)
        password = 'TestPassword'
        # 导入助记词
        auto.metamaskSetup(seed_phrase, password)
        time.sleep(3)
        # 打开MuteSwitch测试网
        driver.get('https://testnet.switch.mute.io/')
        time.sleep(10)
        auto.connectToWebsite()
        time.sleep(3)
        auto.addAndChangeNetwork()
        time.sleep(3)
        print('init success')

    # Close popup
    def closePopup():
        while True:
            try:
                element = driver.find_element_by_xpath("//*[@alt='Close']")
            except NoSuchElementException:
                time.sleep(20)
                driver.find_element_by_xpath("//*[@alt='Close']").click()
                break
            else:
                driver.find_element_by_xpath("//*[@alt='Close']").click()
                break

    # Swap TokenA for TokenB
    def swap(a, b):
        time.sleep(3)
        token_x = a
        token_y = b
        driver.find_element_by_xpath("//button[text()='Select token']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//p[text()='" + token_x + "']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[text()='Select token']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//p[text()='" + token_y + "']").click()
        time.sleep(3)
        inputs = driver.find_elements_by_xpath('//input')
        value = random.randint(10, 30)
        inputs[0].send_keys(value)
        time.sleep(10)
        while True:
            try:
                element = driver.find_element_by_xpath('//button[text()="Approve"]')
            except NoSuchElementException:
                print("Swap")
                driver.find_element_by_xpath('//button[text()="Swap"]').click()
                auto.signConfirm()
                time.sleep(3)
                closePopup()
                break
            else:
                print("Approve")
                driver.find_element_by_xpath('//button[text()="Approve"]').click()
                auto.signConfirm()
                time.sleep(3)
                closePopup()
                time.sleep(5)
                # driver.find_element_by_xpath('//button[text()="Swap"]').click()
                auto.signConfirm()
                time.sleep(3)
                closePopup()
                break
        print('run swap success')

    # Add Liquidity TokenA and TokenB
    def addLP(a, b):
        token_x = a
        token_y = b
        time.sleep(3)
        driver.find_element_by_xpath("//a[text()='Pool']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[text()='Add Liquidity']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[text()='Select token']").click()
        time.sleep(3)
        driver.find_element_by_xpath("(//p[text()='" + token_x + "'])[last()]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[text()='Select token']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//p[text()='" + token_y + "']").click()
        time.sleep(3)
        inputs = driver.find_elements_by_xpath('//input')
        value = random.randint(10, 30)
        inputs[0].send_keys(value)
        time.sleep(10)
        driver.find_element_by_xpath('//button[text()="Supply"]').click()
        time.sleep(3)
        auto.signConfirm()
        time.sleep(15)
        time.sleep(3)
        auto.signConfirm()
        closePopup()
        print('run add LP success')

    def farming():
        time.sleep(3)
        driver.find_element_by_xpath("//a[text()='Farming']").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/main/div/div[3]/div/div/div[1]').click()
        driver.find_element_by_xpath("//button[text()='Approve']").click()
        while True:
            try:
                element = driver.find_element_by_xpath("//button[text()='Approve']")
            except NoSuchElementException:
                print("Swap")
                driver.find_element_by_xpath('//button[text()="Harvest"]').click()
                time.sleep(3)
                driver.get_screenshot_as_file(
                    '/Users/luoye/Downloads/TestNetwork/zkSync2/muteSwitch' + address + '.png')
                break
            else:
                print("Approve")
                driver.find_element_by_xpath("//button[text()='Approve']").click()
                auto.signConfirm()
                time.sleep(10)
                driver.find_element_by_xpath('//button[text()="MAX"]').click()
                time.sleep(5)
                driver.find_element_by_xpath('//button[text()="Deposit"]').click()
                time.sleep(3)
                auto.signConfirm()
                time.sleep(3)
                driver.find_element_by_xpath('//button[text()="Harvest"]').click()
                time.sleep(3)
                driver.get_screenshot_as_file(
                    '/Users/luoye/Downloads/TestNetwork/zkSync2/muteSwitch' + address + '.png')
                break

    init()
    # token_list_a = ['DAI', 'USD Coin', 'Chainlink']
    # token_list_b = ['Ethereum', 'Wrapped Bitcoin']
    # token_a = random.choice(token_list_a)
    # token_b = random.choice(token_list_b)
    token_a = 'DAI'
    token_b = 'ETH'
    swap(token_a, token_b)
    time.sleep(3)
    addLP(token_a, token_b)
    # dai = 'DAI'
    # eth = 'Ethereum'
    # time.sleep(3)
    # addLP(dai, eth)
    time.sleep(3)
    farming()


filename = '20220313_eth_zkSync2_50.xlsx'
address_list = wallet.getAddress(filename)
result = open('/Users/luoye/Downloads/TestNetwork/zkSync2/result.txt', mode='a', encoding='utf-8')
for i in range(1, 51):
    address = address_list[i]
    try:
        runMuteSwitchTestnet(address)
    except Exception as e:
        print(e)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行失败")
        print(address + " run test failed", file=result)
        continue
    else:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行成功")
        print(address + " run test success", file=result)

