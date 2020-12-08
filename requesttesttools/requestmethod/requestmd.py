import requests
import re, json
from common.addlogs import add_logs
from common.readexcel import ReadExcelData


class RequestMethod:
    def __init__(self):
        # 实例化请求类
        self.session = requests.Session()

        # 实例化读取excel的类，用于读取excel的内容
        self.exceldata = ReadExcelData()
        # 避免https忽略证书验证时的警告
        requests.packages.urllib3.disable_warnings()  # 避免https报错

    # 发送请求，返回响应数据
    def sendrequest(self, row):
        """
        发送请求，获得响应数据
        row表示传人的excel用例的行号
        :param row:excel行号
        :return:返回响应数据
        """
        # 读取请求头
        headers = self.exceldata.read_headers(row)
        # 如果请求头不为空，则进行请求，为空则返回None
        if headers != None:
            # 将headers更新到请求中,这里如果headers都相同，可以在Excel中填相同的headers字段，用于json数据读取
            self.session.headers.update(headers)
            add_logs().info("Headers:{}".format(headers))
        # 读取请求方法，参数，URL地址
        method = self.exceldata.read_request_method(row)
        add_logs().info("Method:{}".format(method))
        params = self.exceldata.read_params(row)
        add_logs().info("参数:{}".format(params))
        url = self.exceldata.read_excel_url(row)
        add_logs().info("URL:{}".format(url))

        # 对带参数的GET请求进行发送，主要是避免没有填写响应选项程序报错
        # GET请求如果将参数拼接到URL中会显得excel中的字段比较长，所以将参数分离到json文件中，如果不想分离，也可以正常进行请求
        try:
            if method == "GET" and params != None and url != None:
                response = self.session.request(method=method, url=url, params=params, verify=False)
                return response
            # 对不带参数的GET请求进行发送
            if method == "GET" and params == None and url != None:
                response = self.session.request(method=method, url=url, verify=False)
                return response

            # 进行POST方法的请求
            if method == "POST" and params != None and url != None:
                # 如果依赖字段为空，则直接进行请求
                if self.exceldata.read_dependent(row) == None:
                    response = self.session.request(method=method, url=url, data=json.dumps(params), verify=False)
                    return response
                # 依赖字段不为空时，更新params（data）再进行请求
                else:
                    params = self.updateparams(row)
                    response = self.session.request(method=method, url=url, data=json.dumps(params), verify=False)
                    return response
        except Exception as e:
            add_logs().error("请求错误:{}".format(e))


    # 获取响应数据json或者text格式
    def getresponse(self, row):
        # 如果用例是需要执行的，通过是否执行字段来控制用例执行
        if self.exceldata.read_is_excute(row) != False:
            # 打印用例名字/用例描述
            add_logs().info("用例名：{}".format(self.exceldata.read_casename(row)))
            # print(self.exceldata.read_casename(row))
            response = self.sendrequest(row)
            if response != None:
                responsedata = None
                try:
                    # 尝试获取json格式的返回数据
                    responsedata = response.json()
                    add_logs().info("json格式完整的响应数据{}:".format(responsedata))
                    return responsedata
                except:
                    # 获取文本格式的返回数据
                    responsedata = response.text
                    # add_logs().info("完整的响应数据{}".format(responsedata))
                    return responsedata
            else:
                # 如果响应为空，返回
                add_logs().warning("没有获取到响应数据")
                return

    """ 
    对上下文相关的接口进行处理，获取相关参数，更新到下个请求中
    获取前置用例中的依赖数据，通过正则表达式
    """

    # 通过正则表达式提取出需要更新的字段，然后返回一个字典
    def getupdatedata(self, row):
        # 读取前置用例ID
        beforecaseid = self.exceldata.read_beforecaseid(row)
        add_logs().info("前置用例ID读取成功：{}".format(beforecaseid))
        # 获取excel表格最大数据行数
        maxcolumn = self.exceldata.get_max_row()
        add_logs().info("获取最大表格行数成功:{}".format(maxcolumn))
        # 获取前置用例的行数,前置用例ID，以及执行前置用例获取响应值
        for i in range(2, maxcolumn):
            if self.exceldata.read_case_id(i) == beforecaseid:
                # 获取前置用例的响应数据
                response = self.sendrequest(i)
                # 读取正则表达式
                regular = self.exceldata.read_regular(i)
                # 读取key，相关参数需要更新的键值
                key = self.exceldata.read_dependent(row)
                # 如果正则表达式存在，响应数据存在
                if regular != None and response != None:
                    try:
                        data = self.getregular_data(regular, response.json())
                        add_logs().info("通过json提取出数据成功:{}".format(data))
                    except:
                        data = self.getregular_data(regular, response.text)
                        add_logs().info("通过正则表达式匹配文本提取数据成功:{}".format(data))

                    # 如果data不为空,key不为空
                    if data and key:
                        value = data[0]
                        return {key: value}
                    else:
                        add_logs().error("没有匹配到需要更新的数据，或者key值不存在")


    # 更新post参数的方法
    def updateparams(self, row):
        # 读取参数
        params = self.exceldata.read_params(row)
        # 获取字典
        newdict = self.getupdatedata(row)
        add_logs().info("获取到新参数字典为：{}".format(newdict))
        if newdict and params:
            params.update(newdict)
            add_logs().info("New参数:{}".format(params))
            return params
        else:
            add_logs().error("没有获取到字典,或者参数不正确")

    # 正则提取响应数据
    def getregular_data(self, regular, response):
        # 进行正则匹配，返回匹配到的列表数据，如果匹配失败则返回None
        regulardata = re.findall(regular, str(response))
        if regulardata:

            return regulardata
        else:
            add_logs().error("正则表达式没有匹配到数据，请检查是否正确")
            return None

    # 获取真实的响应结果
    def get_actual_result(self, row):
        # 拿到响应数据，json或者text格式的
        response = self.getresponse(row)
        # 如果期望值为空，则进行请求获得响应数据
        if self.exceldata.read_expect(row) == None:
            return response
        # 如果期望值不为空，则进行请求获得期望数据
        else:
            regular = self.exceldata.read_regular(row)

            # 如果有需要提取的字段，就进行提取
            if regular != None and response != None:
                # actual_result = re.findall(regular, str(response))
                # return actual_result[0]
                # 提取json数据
                try:
                    return response[regular]
                # 提取正则字段匹配数据
                except:
                    actual_result = re.findall(regular, str(response))
                    if actual_result:
                        return actual_result[0]

                # 如果没有需要提取的字段，就返回响应数据
            else:
                add_logs().info("没有期望字段，直接返回请求数据")
                return response


if __name__ == '__main__':
    # for row in range(2, 8):
    #     print(RequestMethod().get_actual_result(row))
        # print(RequestMethod().getresponse(row))
    print(RequestMethod().getresponse(4))
