# coding=utf-8
from appium import webdriver


class Connector:
    def __init__(self):
        self.dr = None
        print "Connect __init__ finished."

    def open_connection(self, platform):
        desired_caps = {}
        desired_caps['platformName'] = platform  # 测试平台
        desired_caps['platformVersion'] = '6.0.1'  # 平台版本
        desired_caps['deviceName'] = 't1host'  # 设备名称，多设备时需区分
        desired_caps['appPackage'] = 'com.sankuai.caipao.merchant'  # app package名
        desired_caps['appActivity'] = '.ui.splash.SplashScreenActivity'  # app默认Activity
        self.dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动Remote RPC
        return self.dr

    def close_connection(self):
        self.dr.quit()
