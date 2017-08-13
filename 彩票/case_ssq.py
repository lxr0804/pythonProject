# coding=utf-8

from time import sleep


class Ssq:
    def __init__(self, dr):
        self.dr = dr

    def select_s(self):
        # TODO 智能获取节点
        self.dr.tap([(367, 500)])
        sleep(3)

    def pay(self):
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/btn_confirm_pay").click()  # 确认支付
        sleep(3)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/btn_cashier_pay_confirm").click()  # 确认支付
        sleep(2)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/alert_btn2").click()
        sleep(3)
        self.dr.swipe(35, 84, 35, 84)
        sleep(3)

    #   ****单式******
    def sim(self):
        self.select_s()
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/machine_choose_1").click()  # 机选一注
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/submit_result").click()  # 立即投注
        # TODO 模拟获取
        response = self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/tan_chuang")

        print response  # {'success': 0, 'value': None, 'sessionId': self.session_id}

        if (response.get_property("value") == None):
            self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/tan_chuang").click()
            self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/fan_hui").click()
            sleep(10)
            self.test_sim()
        else:
            self.pay()

    # ****复式******
    def mul(self):
        self.select_s()
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/shuangseqiu_fushi").click()
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/machine_choose_1").click()  # 机选复式
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/fu_machine_confirm").click()  # 确定机选
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/submit_result").click()  # 立即投注
        sleep(2)
        self.pay()

    #   *****胆施******
    def ds(self):
        self.select_s()
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/shuangseqiu_dantuo").click()
        # 胆码
        self.dr.tap([(280, 386)])  # 3
        self.dr.tap([(383, 396)])  # 4

        # 拖码
        self.dr.tap([(483, 762)])  # 5
        self.dr.tap([(580, 750)])  # 6
        self.dr.tap([(682, 750)])  # 7
        self.dr.tap([(788, 735)])  # 8
        self.dr.tap([(889, 743)])  # 9
        self.dr.tap([(991, 738)])  # 10

        # 篮球
        self.dr.swipe(1046, 856, 1046, 317)
        self.dr.tap([(1094, 702)])

        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/submit_result").click()  # 立即投注

        self.pay()


