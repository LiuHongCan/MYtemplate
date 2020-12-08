import openpyxl, re
from common.readjsondata import read_json_data
from common.redfilepathini import ReadIni
from config.EXCELcells import ExcelCells


# 读取Excel内容的类
class ReadExcelData:

    def __init__(self):
        # 实例化ReadIni类，用于获取Excel的路径
        getdata = ReadIni()
        # 通过readexcel方法，获取excel文件的完整路径
        excelfile = getdata.readexcel()
        # 打开excel文件，准备进行读取
        workbook = openpyxl.load_workbook(excelfile)
        # 从配置文件中读取Sheet页的名字
        sheet = getdata.redexcelsheet()
        # 获取excel数据，并将其公有化
        self.exceldata = workbook[sheet]
        # 实例化ExcelCells类，用于获取表格单元格的常量，比如A列单元格
        self.excelcell = ExcelCells()

    def read_excel_data(self, column, row):
        """
        读取Excel单元格内容的方法
        :param column: 列
        :param row: 行
        :return: 返回获取到的数据
        """
        return self.exceldata["{}{}".format(column, row)].value

    def read_excel_url(self, row):
        """
        获取url数据
        :param row:
        :return:
        """
        column = self.excelcell.CELL_REQUEST_URL
        url = self.read_excel_data(column, row)
        if url != None:
            # 如果URL中带有ms_session参数，将其更换为最新的参数
            if "ms_session" in url:
                session = self.read_session()
                session = re.subn(":", "%3A", session)
                session = session[0]
                # regular = re.compile("ms_session=(.+?)")
                str1 = re.findall("&ms_session=(.+?)&", url)

                url = re.subn(str1[0], session, url)
                return url[0]
            else:
                return url
        else:
            print("数据错误")
            return False

    def read_case_id(self, row):
        """
        获取用例ID
        :param row:
        :return:
        """
        column = self.excelcell.CELL_TEST_ID
        return self.read_excel_data(column, row)

    def read_request_method(self, row):
        """
        获取请求方法
        :param row:
        :return:
        """
        column = self.excelcell.CELL_REQUEST_METHOD
        return self.read_excel_data(column, row)

    def read_params(self, row):
        """
        获取请求参数，这里一般指用于POST方法的参数（data）
        :param row:
        :return:
        """
        column = self.excelcell.CELL_REQUEST_PARAMS
        paramstitle = self.read_excel_data(column, row)
        parmas = read_json_data().get(paramstitle)
        if parmas != None:
            if "ms_session" in parmas:
                parmas["ms_session"] = self.read_session()
                return parmas
            else:
                return parmas
        else:
            return parmas

    def read_headers(self, row):
        """
        获取请求头，请求头一般可以指保存一个在json中，但是需要每天维护session参数
        :param row:
        :return:
        """
        column = self.excelcell.CELL_REQUEST_HEADERS
        headerstitle = self.read_excel_data(column, row)
        headers = read_json_data().get(headerstitle)
        # 将headers中的session更换为最新的
        if headers != None:
            if "ms_session" in headers:
                headers["ms_session"] = self.read_session()
                return headers
            else:
                return headers
        else:
            return headers

    def read_beforecaseid(self, row):
        """
        读取前置用例ID
        :param row:
        :return:
        """
        column = self.excelcell.CELL_BEFORECASEID
        return self.read_excel_data(column, row)

    def get_max_row(self):
        """
        获取最大行数
        :return:
        """
        return self.exceldata.max_row

    def get_max_column(self):
        """
        获取最大列数
        :return:
        """
        return self.exceldata.max_column

    def read_regular(self, row):
        """
        获取最大行数
        :param row:
        :return:
        """
        column = self.excelcell.CELL_REGULAR
        return self.read_excel_data(column, row)

    def read_dependent(self, row):
        """获取依赖字段，用于更新params"""
        column = self.excelcell.CELL_DEPENDENT
        return self.read_excel_data(column, row)

    def read_expect(self, row):
        """
        读取期望字段
        :param row:
        :return:
        """
        column = self.excelcell.CELL_EXPECT
        return self.read_excel_data(column, row)

    def read_is_excute(self, row):
        """
        获取是否执行该用例的控制字段
        :param row:
        :return:
        """
        column = self.excelcell.CELL_ISEXCUTE
        return self.read_excel_data(column, row)

    def read_casename(self, row):
        """
        读取用例名字，用例描述
        :param row:
        :return:
        """
        column = self.excelcell.CELL_CASENAME
        return self.read_excel_data(column, row)

    def read_session(self):
        """
        读取session，用于更换prams和header中的session
        :param row:
        :return:
        """
        column = self.excelcell.CELL_SESSION
        return self.read_excel_data(column, 2)

    # 参数化数据
    def paramsexpectdata(self):
        """
        对用例执行时进行参数化配置，在参数化中调用该方法，即可传入相关参数
        :return:
        """
        self.list1 = []
        for row in range(2, self.get_max_row() + 1):
            expect = self.read_expect(row)
            self.list1.append((row, expect))
        return self.list1


if __name__ == '__main__':
    # print(type(ReadExcelData().get_max_column))
    e = ReadExcelData()
    s = e.read_headers(4)
    print(s)
    pass
