from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
from selenium.common.exceptions import NoSuchElementException

EXTENSION_PATH = os.path.abspath(r"..") + '/selenium_metamask_automation/extension_metamask.crx'

EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'


def downloadMetamaskExtension():
    print('Setting up metamask extension please wait...')

    url = 'https://xord-testing.s3.amazonaws.com/selenium/10.0.2_0.crx'
    urllib.request.urlretrieve(url, os.getcwd() + '/extension_metamask.crx')


def launchSeleniumWebdriver(driverPath):
    print('path', EXTENSION_PATH)
    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
    time.sleep(5)
    print("Extension has been loaded")
    return driver


def metamaskSetup(recoveryPhrase, password):
    driver.switch_to.window(driver.window_handles[0])

    driver.find_element_by_xpath('//button[text()="开始使用"]').click()
    driver.find_element_by_xpath('//button[text()="导入钱包"]').click()
    driver.find_element_by_xpath('//button[text()="我同意"]').click()

    time.sleep(5)

    inputs = driver.find_elements_by_xpath('//input')
    inputs[0].send_keys(recoveryPhrase)
    inputs[1].send_keys(password)
    inputs[2].send_keys(password)
    driver.find_element_by_css_selector('.first-time-flow__terms').click()
    driver.find_element_by_xpath('//button[text()="导入"]').click()

    time.sleep(8)

    driver.find_element_by_xpath('//button[text()="全部完成"]').click()
    time.sleep(2)

    # # closing the message popup after all done metamask screen
    # driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
    # time.sleep(2)
    print("Wallet has been imported successfully")
    # time.sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def changeMetamaskNetwork(networkName):
    # opening network
    print("Changing network")
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('chrome-extension://{}/home.html'.format(EXTENSION_ID))
    time.sleep(5)
    try:
        element = driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button')
    except NoSuchElementException as e:
        # 打印异常信息
        print(e)
        print("no popup")
        # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
        print("closing popup")
    # driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
    # 打开网络下拉框
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span').click()
    # 跳转开启测试网设置
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[1]/div[3]/span/a').click()
    time.sleep(2)
    # 显示测试网
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/div/div[1]/div[2]/div').click()
    time.sleep(2)
    # 滑到最上方
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(2)
    # 打开网络下拉框
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span').click()
    time.sleep(2)
    print("opening network dropdown")
    # elem = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div')
    time.sleep(2)
    # 以太坊 Ethereum 主网络
    # Ropsten 测试网络
    # Kovan 测试网络
    # Rinkeby 测试网络
    # Goerli 测试网络
    all_li = driver.find_elements_by_tag_name('li')

    time.sleep(2)
    for li in all_li:
        text = li.text
        if text == networkName:
            li.click()
            print(text, "is selected")
            time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
            return
    time.sleep(2)
    print("Please provide a valid network name")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)


def addAndChangeNetwork():
    time.sleep(3)
    print("添加并切换网络开始")
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('chrome-extension://{}/home.html'.format(EXTENSION_ID))
    time.sleep(8)
    driver.find_element_by_xpath("//button[text()='批准']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='切换网络']").click()
    time.sleep(8)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)


def connectToWebsite():
    time.sleep(3)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
    driver.find_element_by_xpath('//button[text()="下一步"]').click()
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    driver.find_element_by_xpath('//button[text()="连接"]').click()
    time.sleep(3)
    print('Site connected to metamask')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)


def confirmApprovalFromMetamask():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(10)
    # confirm approval from metamask
    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]').click()
    driver.find_element_by_xpath('//button[text()="确认"]').click()
    time.sleep(12)
    print("Approval transaction confirmed")

    driver.close()
    # switch back
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)


def rejectApprovalFromMetamask():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(10)
    # confirm approval from metamask
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[1]').click()
    time.sleep(8)
    print("Approval transaction rejected")

    # switch to dafi
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    print("Reject approval from metamask")


def confirmTransactionFromMetamask():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(10)

    # # confirm transaction from metamask
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]').click()
    time.sleep(13)
    print("Transaction confirmed")

    # switch to dafi
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(3)


def rejectTransactionFromMetamask():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(5)
    # confirm approval from metamask
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[1]').click()
    time.sleep(2)
    print("Transaction rejected")

    # switch to web window
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

def addToken(tokenAddress):
    # opening network
    print("Adding Token")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('chrome-extension://{}/home.html'.format(EXTENSION_ID))
    print("closing popup")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()

    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span').click()
    # time.sleep(2)

    print("clicking add token button")
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div/div/div[3]/div/div[3]/button').click()
    time.sleep(2)
    # adding address
    driver.find_element_by_id("custom-address").send_keys(tokenAddress)
    time.sleep(10)
    # clicking add
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[2]/div[2]/footer/button[2]').click()
    time.sleep(2)
    # add tokens
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[3]/footer/button[2]').click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)


def signConfirm():
    print("sign")
    time.sleep(3)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(5)
    while True:
        try:
            element = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/div[1]')
        except NoSuchElementException:
            time.sleep(1)
            break
        else:
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/div[1]').click()
            driver.find_element_by_xpath('//button[text()="签名"]').click()
            time.sleep(1)
            break
    print('Sign confirmed')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)


def signReject():
    print("sign")
    time.sleep(3)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[1]').click()
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    # time.sleep(3)
    print('Sign rejected')
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
