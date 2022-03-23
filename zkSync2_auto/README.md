## 简介
使用selenium实现对zkSync2.0测试网及其上首个dex项目muteSwitch的自动化交互

## 环境准备
*在使用之前，请确认已经准备好以下环境:*  
### python3.6及以上  
通过 [该网站](https://www.runoob.com/python/python-install.html) 完成 Python 环境搭建

### selenium库  
使用pip安装：
```bash
pip install selenium
```

### openpyxl库  
```bash
pip install openpyxl
```

### configparser库
```bash
pip install configparser
```

### Chrome浏览器和Chromedriver驱动  
[下载安装谷歌浏览器](https://www.google.cn/chrome/)  
[Chrome 浏览器驱动下载地址](https://chromedriver.storage.googleapis.com/index.html)
>注意: 浏览器驱动 应与浏览器版本匹配  

### 包含钱包地址及助记词的xlxs格式表格
推荐使用 [CoinTool](https://cointool.app/createWallet/eth) 批量生成  
>注意: 由此生成的钱包 应仅作测试网使用  

### MetaMask钱包插件
推荐自行下载官方渠道的crx格式MetaMask钱包插件  
重命名为extension_metamask.crx  
替换到`selenium_metamask_automation`目录下  

### Python集成开发环境
推荐使用 [Pycharm](https://www.jetbrains.com/pycharm/)  

## 开始使用  

### **1.配置chromedriver驱动、excel、运行结果路径**  
参考`config.ini`中的注释完成相关配置  

[comment]: <> (### **1.修改chromedriver驱动存放目录**  )

[comment]: <> (`zkSync2_run_test.py`中`driver_path`)

[comment]: <> (```python)

[comment]: <> (def runTest&#40;filename, addr&#41;:)

[comment]: <> (    # 指定chromedriver路径)

[comment]: <> (    driver_path = '/Users/luoye/Downloads/tools/chromedriver')

[comment]: <> (```  )

[comment]: <> (`muteSwitch_run_test.py`中`driver_path`)

[comment]: <> (```python)

[comment]: <> (def runMuteSwitchTestnet&#40;filename, addr&#41;:)

[comment]: <> (    # 指定chromedriver路径)

[comment]: <> (    driver_path = '/Users/luoye/Downloads/tools/chromedriver')

[comment]: <> (```)

[comment]: <> (### **2.修改`Wallet`目录下`__init__.py`中excel路径**)

[comment]: <> (```python)

[comment]: <> (def getAddress&#40;filename&#41;:)

[comment]: <> (    if len&#40;filename&#41; == 0:)

[comment]: <> (        print&#40;'未指定地址文件'&#41;)

[comment]: <> (        return)

[comment]: <> (    # 用户地址路径，以xlsx格式保存)

[comment]: <> (    file = '/Users/luoye/Downloads/TestNetwork/' + filename)

[comment]: <> (    address_list = Excel&#40;file&#41;.getColValues&#40;1&#41;)

[comment]: <> (    return address_list)


[comment]: <> (def getSeedPhrase&#40;filename, address&#41;:)

[comment]: <> (    input_address = address)

[comment]: <> (    if len&#40;filename&#41; == 0:)

[comment]: <> (        print&#40;'未指定地址文件'&#41;)

[comment]: <> (        return)

[comment]: <> (    # 用户助记词路径，以xlsx格式保存，该路径由用户自行修改)

[comment]: <> (    file = '/Users/luoye/Downloads/TestNetwork/' + filename)

[comment]: <> (    address_list = Excel&#40;file&#41;.getColValues&#40;1&#41;)

[comment]: <> (    mnemonic_list = Excel&#40;file&#41;.getColValues&#40;3&#41;)

[comment]: <> (```)

[comment]: <> (### **3.修改运行完成时截图存放路径**  )

[comment]: <> (在`zkSync2_run_test.py`和`muteSwitch_run_test.py`查找  )

[comment]: <> (*get_screenshot_as_file* 并修改)

[comment]: <> (```python)

[comment]: <> (driver.get_screenshot_as_file&#40;'/Users/luoye/Downloads/TestNetwork/zkSync2/' + address + '.png'&#41;)

[comment]: <> (```)

[comment]: <> (```python)

[comment]: <> (driver.get_screenshot_as_file&#40;)

[comment]: <> (                    '/Users/luoye/Downloads/TestNetwork/zkSync2/muteSwitch/' + addr + '.png'&#41;)

[comment]: <> (```)

[comment]: <> (### **4.修改`run_full_test.py`文件中Excel名及执行结果保存路径**  )

[comment]: <> (```python)

[comment]: <> (filename = '20220317_eth_zkSync_muteSwitch_100.xlsx')

[comment]: <> (address_list = wallet.getAddress&#40;filename&#41;)

[comment]: <> (result = open&#40;'/Users/luoye/Downloads/TestNetwork/zkSync2/full/result.txt', mode='a', encoding='utf-8'&#41;)

[comment]: <> (```)
### **2.使用CoinTool提供的批量转账功能向钱包地址转账**  
连接 [CoinTool](https://cointool.app/multiSender/eth) ，切换到Goerli测试网络，按页面提示完成批量转账
>建议每个地址转入的测试币大于0.05ETH  

### **3.设定好循环次数，开始自动化测试**
```python
for i in range(1, 101):
    address = address_list[i]
    try:
        zkSync.runTest(address)
        time.sleep(3)
        muteSwitch.runMuteSwitchTestnet(address)
        time.sleep(3)
```
>注意：循环应从1开始
## FAQ
```
Q:访问不了README中的蓝色超链接？  
A:请使用科学上网
```
```
Q:为什么需要修改这么多路径
A:第一个项目，没有做好设计，现在已经新增了getSeedPhraseV2()方法，下一个项目会减少各种路径配置
```
```
Q:没有Goerli测试币
A:我也没有
```
```
Q:循环执行过程中有成功也有失败
A:受网速及测试网区块出块速度影响，可能会有偶现失败。如果遇到某问题必然出现，可以提issue反馈。
```
### 其它  
联系方式：luoyeeth@gmail.com  
演示视频：[zkSync2.0](https://www.bilibili.com/video/BV13i4y1C79m) [muteSwitch](https://www.bilibili.com/video/BV1Sr4y1B7VV)  
修改版本：[@ChinaHERO88](https://twitter.com/ChinaHERO88/status/1505815806810427395?s=20&t=ED6LNMyNWnLZ-wa3KanFYA)
