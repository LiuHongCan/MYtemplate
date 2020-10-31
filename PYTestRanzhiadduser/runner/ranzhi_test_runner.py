import os
import time
import unittest
from unittestreport import TestRunner

from common.print_log import add_log
from common.readini import Get_ini_data
from common.send_emails_report import sendemails


class Runner:

    def runner(self):
        # 实例化一个测试套件
        testsuite = unittest.TestSuite()
        # 获取测试用例的绝对路径
        case_path = Get_ini_data().get_case_path()
        # 加载测试用例
        testsuite.addTests(unittest.TestLoader().discover(case_path, pattern='ranzhi_document_test.py'))
        tim = '然之测试报告{}.html'.format(time.strftime('%Y_%m_%d_%H_%M_%S'))
        htmlreportpath = Get_ini_data().get_htmlreport_path()
        reportfilename = htmlreportpath+tim

        test_runner = TestRunner(suite=testsuite,
                                 filename=reportfilename,
                                 report_dir=reportfilename,
                                 title='测试报告',
                                 tester='老林',
                                 desc="然之项目测试生产的报告",
                                 templates=2)
        test_runner.run()

        sendemails(reportfilename)
        add_log().info('邮件已经发送:{}'.format(reportfilename))


if __name__ == '__main__':
    Runner().runner()
