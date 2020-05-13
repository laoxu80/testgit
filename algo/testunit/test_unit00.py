import unittest
from testunit.test_demo00 import MyClass


class MyclassTest(unittest.TestCase):
    def setUp(self) -> None:
        '''
        测试之前的准备工作
        :return:
        '''
        #self.clac = MyClass(4,3)
        pass

    def tearDown(self) -> None:
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        pass

    def test_add_zz(self):
        number = MyClass(4,3)
        ret = number.add()
        self.assertEqual(ret,7)

    def test_add_fufu(self):
        number02 = MyClass(-3, -3)
        ret = number02.add()
        self.assertEqual(ret,-6)

    def test_sub(self):
        number03=MyClass(1.2,3.2)
        ret = number03.sub()
        self.assertEqual(ret,-2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_add'))
    suite.addTest(MyclassTest('test_sub'))

    runner = unittest.TextTestRunner()
    runner.run(suite)