import time
import wallet
from config import global_config
import zkSync2_run_test as zkSync
import muteSwitch_run_test as muteSwitch

wallet = wallet.getWallet()
address_list = wallet[0]
result_path = global_config.get('path', 'result_path').strip()
result = open(str(result_path) + 'result.txt', mode='a', encoding='utf-8')

for i in range(1, 101):
    address = address_list[i]
    try:
        zkSync.runTest(address)
        time.sleep(3)
        # muteSwitch可能存在一系列未知问题
        muteSwitch.runMuteSwitchTestnet(address)
        time.sleep(3)
    except Exception as e:
        print(e)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行失败")
        print(address + " run test failed", file=result)
        continue
    else:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行成功")
        print(address + " run test success", file=result)
