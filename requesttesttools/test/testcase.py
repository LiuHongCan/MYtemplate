import unittest

import openpyxl
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
        # self.excelread.get_Session()
    def tearDown(self) -> None:
        pass

    # 进行参数化装饰
    @parameterized.expand(data)
    def testrun(self, row, expect, sheet, excelfile, jsonfile):
        #可以增加一个配置文件进行用例文件名的配置，达到执行多个文件内的用例的目的，具体参数化，查看ini文件配置和ReadExcelData()中的参数化方法
        self.excelread.workbook = openpyxl.load_workbook(excelfile)

        #由于对每个excel文件进行了参数化，可能其对应的json参数数据配置也需要对应，需要进行参数化传人，或许还要针对sheet页设置json参数。（！！！）
        self.excelread.jsonfile = jsonfile
        #对excel的sheet页做了参数化，自动遍历所以sheet页，根据是否有执行控制字段进行用例执行
        # （可以将sheet页出差到列表中进行参数化，这样可以达到指定执行某一页的用例，但是需要手动配置到config文件中，不是很灵活）
        self.excelread.exceldata = self.excelread.workbook[sheet]
        # 获取用例名字，描述，用于被html报告捕获
        self._testMethodDoc = self.excelread.read_casename(row)
        # print(row, expect)
        # 如果期望值存在
        if expect:
            try:
                # 获取实际结果
                actualresult = self.requestsmethod.get_actual_result(row)
                add_logs().info("实际结果为：{}".format(actualresult))
                # 如果是不执行的用例，跳过校验
                if self.excelread.read_is_excute(row) != False:
                    # 对期望结果和实际结果进行断言
                    self.assertEqual(actualresult, expect, "校验实际结果和期望值")
            # 断言失败，则抛出异常，打印实际结果
            except AssertionError as e:
                add_logs().error("断言失败，请查看错误信息========>：")
                raise e
        # 如果期望不存在，则直接获取响应结果
        else:
            return self.requestsmethod.getresponse(row)


if __name__ == '__main__':
    pass
