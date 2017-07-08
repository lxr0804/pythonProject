# coding=utf-8
from uiautomator import device as d
import unittest


class Mytest(unittest.TestCase):
    def setUp(self):
        print "---初始化工作"

    def tearDown(self):
        print "---退出清理工作"

    def test_click(self):
        d(text="我的课程").click


if __name__=='__main__':
    unittest.main()

