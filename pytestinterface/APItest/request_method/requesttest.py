import re
import requests
from APItest.common.ReadExcelData import Readexceldata


class RequestMethod:
    def __init__(self):
        self.session = requests.session()
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                      " AppleWebKit/537.36 (KHTML, like Gecko)"
                                      " Chrome/86.0.4240.183 Safari/537.36",
                        "MSO": "SID&1604912638"}
        # self.cookie = {"MSO": "SID&1604912638"}
        self.session.headers.update(self.headers)
        # self.session.cookies.update(self.cookie)
        self.exceldata = Readexceldata()

    def send_request(self, row):
        """
        发送请求
        :param row:
        :return:
        """
        method = self.exceldata.read_request_method(row)
        url = self.exceldata.read_request_url(row)
        # print(url)
        params = self.exceldata.read_params(row)
        if method == "GET" and params != None:
            return self.session.get(url=url, params=params, verify=False)
        elif method == "POST" and params != None:
            if self.exceldata.read_front_case_id(row) == None:
                return self.session.post(url=url, data=params, verify=False)
            else:
                params = self.updata_params_dic(row)
                # print(params)
                return self.session.post(url=url, data=params, verify=False)
        else:
            return self.session.get(url, verify=False)

    def get_response(self, row):
        """
        获取响应文本，json格式或者text
        :param row:
        :return:
        """
        res =self.send_request(row)
        res_data = None
        try:
            res_data = res.json()
            return res_data
        except:
            res_data = res.text
            return res_data

    def get_regular_data(self, row):
        frontcaseid = self.exceldata.read_front_case_id(row)
        countrow = self.exceldata.get_cell_max_row()

        if frontcaseid:
            for i in range(2, countrow + 1):
                caseid = self.exceldata.read_testcaseid(i)

                if frontcaseid == caseid:
                    frontres = self.get_response(i)
                    rel = self.exceldata.read_relguar(i)
                    data = re.findall(rel, frontres)
                    key = self.exceldata.read_dependent_fields(i)
                    value = data[0]
                    return {key: value}

    def updata_params_dic(self, row):
        prams = self.exceldata.read_params(row)
        dict1 = self.get_regular_data(row)
        prams.update(dict1)
        return prams

    def get_regular_actual(self, row):
        response = self.get_response(row)
        reg = self.exceldata.read_relguar(row)
        if reg:
            try:
                ac = re.findall(reg, response)
                return ac[0]
            except:
                return response[reg]
        else:
            return response



if __name__ == '__main__':
    rm = RequestMethod()
    # rm.get_regular_actual(6)
    # for row in range(2, rm.exceldata.get_cell_max_row() + 1):
    #     if rm.exceldata.read_case_execute_branch(row):
    #         print(rm.get_response(row))

    print(rm.get_regular_actual(7))


