import unittest
from parameterized import parameterized
from common.addlogs import add_logs
from common.readexcel import ReadExcelData
from requestmethod.requestmd import RequestMethod


class Itest(unittest.TestCase):
    # 获取参数化数据
    data = ReadExcelData().paramsexpectdata()

    def setUp(self) -> None:
        # 实例化请求方法类
        self.requestsmethod = RequestMethod()
        # 实例化excel的读取类
        self.excelread = ReadExcelData()
    def tearDown(self) -> None:
        pass

    # 进行参数化装饰
    @parameterized.expand(data)
    def testrun(self, row, expect):
        # 获取用例名字，描述，用于被html报告捕获
        self._testMethodDoc = self.excelread.read_casename(row)
        # print(row, expect)
        # 如果期望值存在
        if expect:
            try:
                # 获取实际结果
                actualresult = self.requestsmethod.get_actual_result(row)
                # 对期望结果和实际结果进行断言
                self.assertEqual(actualresult, expect, "测试通过")
            # 断言失败，则抛出异常，打印实际结果
            except AssertionError as e:
                add_logs().error("断言失败：{}".format(e))
                raise e
        # 如果期望不存在，则直接获取响应结果
        else:
            return self.requestsmethod.getresponse(row)


if __name__ == '__main__':
    pass
