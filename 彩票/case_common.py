# coding=utf-8

from time import sleep


class CommonCase:
    def __init__(self, dr):
        self.dr = dr

    # 登录操作
    def login(self):
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/tv_set_host").click()  # 切换环境
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/rb_test").click()
        sleep(1)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/btn_ok").click()
        sleep(2)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/rl_no_login").click()  # 登录
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/rl_login").click()  # 商户登录
        sleep(2)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/username").send_keys('18614028606')  # 输入用户名
        sleep(1)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/password").send_keys('asd123')  # 输入密码
        sleep(1)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/login").click()
        sleep(3)
