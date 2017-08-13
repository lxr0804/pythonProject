# coding=utf-8
import unittest

import connector

import case_common
import case_ssq
import case_klt


class Ssq(unittest.TestCase):
    def setUp(self):
        self.connector = connector.Connector()  # 初始化连接器
        self.dr = self.connector.open_connection('Android')  # 获取连接器

        self.common = case_common.CommonCase(self.dr)
        self.ssq = case_ssq.Ssq(self.dr)
        self.kit = case_klt.Klt(self.dr)

    def tearDown(self):
        self.connector.close_connection()

    # 登录
    def test_login(self):
        self.common.login()

    # ****双色球-单式******
    def test_ssq_sim(self):
        self.ssq.sim()

    # ****双色球-复式******
    def test_ssq_mul(self):
        self.ssq.mul()

    # *****双色球-胆拖******
    def test_ssq_ds(self):
        self.ssq.ds()


if __name__ == '__main__':
    suit = unittest.TestLoader.loadTestsFromTestCase(Ssq)
    unittest.TextTestRunner(verbosity=2).run(suit)
