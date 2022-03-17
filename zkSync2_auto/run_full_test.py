import time
import wallet
import zkSync2_run_test as zkSync
import muteSwitch_run_test as muteSwitch

filename = '20220317_eth_zkSync_muteSwitch_100.xlsx'
address_list = wallet.getAddress(filename)
result = open('/Users/luoye/Downloads/TestNetwork/zkSync2/full/result.txt', mode='a', encoding='utf-8')
for i in range(1, 101):
    address = address_list[i]
    try:
        zkSync.runTest(filename, address)
        time.sleep(3)
        muteSwitch.runMuteSwitchTestnet(filename, address)
    except Exception as e:
        print(e)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行失败")
        print(address + " run test failed", file=result)
        continue
    else:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行成功")
        print(address + " run test success", file=result)
