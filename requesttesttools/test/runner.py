import time
import unittest
from unittestreport import TestRunner
from common.redfilepathini import ReadIni


class Runner:
    def __init__(self):
        self.inidata = ReadIni()

    def runner(self):
        # 实例化测试套件
        testsuite = unittest.TestSuite()
        # 获取测试用例文件
        testcasepath = self.inidata.readtestcasepath()
        # 加载测试用例
        testsuite.addTest(unittest.TestLoader().discover(testcasepath, self.inidata.readtestcasefilename()))
        # 设置测试报告的名称格式
        tim = 'BAT接口测试报告{}.html'.format(time.strftime('%Y_%m_%d_%H_%M_%S'))
        # 读取测试报告的保存路径
        httpreportpath = self.inidata.readresultpath()
        # 组合成完整的测试报告路径
        reportfilename = httpreportpath + tim
        # 使用TestRunner插件加载测试套
        test_runer = TestRunner(suite=testsuite,
                                filename=reportfilename,
                                report_dir=httpreportpath,
                                title="BAT接口测试报告",
                                tester="L",
                                desc="测试报告",
                                templates=1)
        # 运行
        test_runer.run()


if __name__ == '__main__':
    Runner().runner()
