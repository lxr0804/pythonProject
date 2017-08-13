# coding=utf-8

from time import sleep


class Klt:
    def __init__(self, dr):
        self.dr = dr

    # 投注快乐2
    def sim_kl2(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(4)
        # self.dr.find_element_by_id("KL2").click()
        self.pay1()

    # 投注快乐3
    def sim_kl3(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(4)
        self.dr.find_element_by_id("KL3").click()
        self.pay1()

    # 投注快乐4
    def sim_kl4(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(4)
        self.dr.find_element_by_id("KL4").click()
        self.pay1()

    # 投注快乐5
    def sim_kl5(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(4)
        self.dr.find_element_by_id("KL5").click()
        self.pay1()

    # 首位数投
    def sim_FN1(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(3)
        self.dr.find_element_by_id("FN1").click()
        self.pay1()

    # 首位红投
    def sim_FR1(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(4)
        self.dr.find_element_by_id("FR1").click()
        self.pay1()

    # 二连组
    def sim_TCG2(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(4)
        self.dr.find_element_by_id("TCG2").click()
        self.pay1()

    # 二连直
    def sim_TCA2(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(3)
        self.dr.find_element_by_id("TCA2").click()
        self.pay1()

    # 前三组
    def sim_FTG3(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(4)
        self.dr.find_element_by_id("FTG3").click()
        self.pay1()

    # 前三直
    def sim_FTA3(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(4)
        self.dr.find_element_by_id("FTA3").click()
        self.pay1()

    def pay1(self):
        self.dr.find_element_by_accessibility_id("机选一注").click()
        self.dr.find_element_by_accessibility_id("立即投注").click()
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/btn_confirm_pay").click()  # 确认支付
        sleep(3)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/btn_cashier_pay_confirm").click()  # 确认支付
        sleep(2)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/alert_btn2").click()
        sleep(3)
        self.dr.swipe(35, 84, 35, 84)
        sleep(3)

    # ************复式*********

    # 投注快乐2
    def select_mul(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(3)
        self.dr.find_element_by_accessibility_id("复式").click()

    def mul_kl2(self):
        self.select_mul()
        self.dr.swipe(167, 552, 167, 552)  # 2
        self.dr.swipe(268, 565, 268, 565)  # 3
        self.dr.swipe(355, 560, 355, 560)  # 4
        self.pay2()

    # 投注快乐3
    def mul_kl3(self):
        self.select_mul()
        sleep(3)
        self.dr.find_element_by_id("KL3").click()
        self.dr.swipe(81, 548, 81, 548)  # 1
        # self.dr.swipe(167, 552, 167, 552)  # 2
        self.dr.swipe(268, 565, 268, 565)  # 3
        self.dr.swipe(355, 560, 355, 560)  # 4
        self.dr.swipe(452, 558, 52, 558)  # 5
        self.dr.swipe(557, 547, 557, 547)  # 6
        self.dr.swipe(655, 558, 655, 558)  # 7
        self.dr.swipe(749, 560, 49, 560)  # 8
        self.dr.swipe(854, 560, 854, 560)  # 9
        self.dr.swipe(950, 562, 950, 562)  # 10
        self.dr.swipe(1042, 552, 1042, 552)  # 11
        self.dr.swipe(78, 658, 78, 658)  # 12
        self.dr.swipe(170, 658, 170, 658)  # 13
        self.dr.swipe(268, 658, 268, 658)  # 14
        self.dr.swipe(355, 658, 355, 658)  # 15
        self.dr.swipe(452, 658, 452, 658)  # 16
        self.dr.swipe(557, 658, 557, 658)  # 17
        self.dr.swipe(655, 658, 655, 658)  # 18
        self.dr.swipe(749, 658, 749, 658)  # 19
        self.dr.swipe(854, 658, 854, 658)  # 20
        self.pay2()

    # 投注快乐4
    def mul_kl4(self):
        self.select_mul()
        sleep(3)
        self.dr.find_element_by_id("KL4").click()
        self.dr.swipe(557, 547, 557, 547)  # 6
        self.dr.swipe(655, 558, 655, 558)  # 7
        self.dr.swipe(749, 560, 49, 560)  # 8
        self.dr.swipe(854, 560, 854, 560)  # 9
        self.dr.swipe(950, 562, 950, 562)  # 10
        self.dr.swipe(1042, 552, 1042, 552)  # 11
        self.dr.swipe(78, 658, 78, 658)  # 12
        self.dr.swipe(170, 658, 170, 658)  # 13
        self.dr.swipe(268, 658, 268, 658)  # 14
        self.dr.swipe(355, 658, 355, 658)  # 15
        self.pay2()

    # 投注快乐5
    def mul_kl5(self):
        self.select_mul()
        sleep(3)
        self.dr.find_element_by_id("KL5").click()
        # self.dr.swipe(167, 552, 167, 552)  # 2
        self.dr.swipe(268, 565, 268, 565)  # 3
        self.dr.swipe(355, 560, 355, 560)  # 4
        self.dr.swipe(452, 558, 52, 558)  # 5
        self.dr.swipe(854, 560, 854, 560)  # 9
        self.dr.swipe(950, 562, 950, 562)  # 10
        self.dr.swipe(1042, 552, 1042, 552)  # 11
        self.dr.swipe(78, 658, 78, 658)  # 12
        self.dr.swipe(170, 658, 170, 658)  # 13
        self.dr.swipe(268, 658, 268, 658)  # 14

        self.pay2()

    # 首位数投
    def mul_FN1(self):
        self.select_mul()
        sleep(3)
        self.dr.find_element_by_id("FN1").click()
        self.dr.swipe(854, 560, 854, 560)  # 9
        self.dr.swipe(950, 562, 950, 562)  # 10
        self.dr.swipe(1042, 552, 1042, 552)  # 11
        self.dr.swipe(78, 658, 78, 658)  # 12
        self.dr.swipe(170, 658, 170, 658)  # 13
        self.dr.swipe(268, 658, 268, 658)  # 14
        self.pay2()

    # 二连组
    def mul_TCG2(self):
        self.select_mul()
        sleep(3)
        self.dr.find_element_by_id("TCG2").click()
        # self.dr.swipe(167, 552, 167, 552)  # 2
        self.dr.swipe(268, 565, 268, 565)  # 3
        self.dr.swipe(355, 560, 355, 560)  # 4
        self.dr.swipe(950, 562, 950, 562)  # 10
        self.dr.swipe(1042, 552, 1042, 552)  # 11
        self.dr.swipe(78, 658, 78, 658)  # 12
        self.dr.swipe(170, 658, 170, 658)  # 13
        self.dr.swipe(268, 658, 268, 658)  # 14
        self.pay2()

    # 前三组
    def mul_FTG3(self):
        self.select_mul()
        sleep(3)
        self.dr.find_element_by_id("FTG3").click()
        self.dr.swipe(167, 552, 167, 552)  # 2
        self.dr.swipe(452, 558, 52, 558)  # 5
        self.dr.swipe(854, 560, 854, 560)  # 9
        self.dr.swipe(950, 562, 950, 562)  # 10
        self.dr.swipe(1042, 552, 1042, 552)  # 11
        self.dr.swipe(749, 658, 749, 658)  # 19
        self.dr.swipe(854, 658, 854, 658)  # 20
        self.pay2()

    def pay2(self):
        self.dr.find_element_by_accessibility_id("立即投注").click()
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/btn_confirm_pay").click()  # 确认支付
        sleep(3)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/btn_cashier_pay_confirm").click()  # 确认支付
        sleep(2)
        self.dr.find_element_by_id("com.sankuai.caipao.merchant:id/alert_btn2").click()
        sleep(8)

        # **************胆拖*********

    def select_dt(self):
        self.dr.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        sleep(5)
        self.dr.find_element_by_accessibility_id("胆拖").click()

    def dt_kl2(self):
        self.select_dt()
        # 胆码
        self.dr.swipe(749, 554, 749, 554)  # 8
        # 拖码
        self.dr.swipe(264, 837, 264, 837)  # 3
        self.dr.swipe(362, 815, 362, 815)  # 4
        self.pay2()

    # 投注快乐3

    def dt_kl3(self):
        self.select_dt()
        sleep(3)
        self.dr.find_element_by_id("KL3").click()
        # 胆码
        self.dr.swipe(261, 558, 261, 558)  # 3
        # self.dr.swipe(362, 815, 362, 815)  # 4
        # 拖码
        self.dr.swipe(740, 836, 740, 836)  # 8
        self.dr.swipe(946, 830, 946, 830)  # 10
        self.dr.swipe(1044, 837, 1044, 837)  # 11

        self.pay2()

    # 投注快乐4

    def dt_kl4(self):
        self.select_dt()
        sleep(3)
        self.dr.find_element_by_id("KL4").click()
        # 胆码
        self.dr.swipe(264, 837, 264, 837)  # 3
        self.dr.swipe(749, 554, 749, 554)  # 8
        self.dr.swipe(246, 824, 246, 824)  # 14

        # 拖码
        self.dr.swipe(463, 725, 463, 725)  # 5
        self.dr.swipe(468, 720, 468, 720)  # 16
        self.dr.swipe(946, 830, 946, 830)  # 10
        self.dr.swipe(1044, 837, 1044, 837)  # 11
        self.pay2()

    # 投注快乐5

    def dt_kl5(self):
        self.select_dt()
        sleep(4)
        self.dr.find_element_by_id("KL5").click()
        # 胆码
        self.dr.swipe(261, 558, 261, 558)  # 3
        self.dr.swipe(460, 558, 460, 558)  # 5
        # 拖码
        self.dr.swipe(740, 836, 740, 836)  # 8
        self.dr.swipe(845, 835, 845, 835)  # 9
        self.dr.swipe(946, 830, 946, 830)  # 10
        self.dr.swipe(1044, 837, 1044, 837)  # 11
        self.pay2()

    # 二连组

    def dt_TCG2(self):
        self.select_dt()
        sleep(3)
        self.dr.find_element_by_id("TCG2").click()
        # 胆码
        self.dr.swipe(261, 558, 261, 558)  # 3
        # 拖码
        self.dr.swipe(740, 836, 740, 836)  # 8
        self.dr.swipe(845, 835, 845, 835)  # 9
        self.dr.swipe(946, 830, 946, 830)  # 10

        self.pay2()

    # 前三组

    def dt_FTG3(self):
        self.select_dt()
        sleep(3)
        self.dr.find_element_by_id("FTG3").click()
        # 胆码
        self.dr.swipe(264, 837, 264, 837)  # 3
        self.dr.swipe(460, 558, 460, 558)  # 5
        # 拖码
        self.dr.swipe(557, 833, 557, 833)  # 6
        self.dr.swipe(653, 828, 653, 828)  # 7
        self.dr.swipe(746, 831, 746, 831)  # 8
        self.pay2()
