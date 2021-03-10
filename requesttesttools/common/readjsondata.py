import json
from common.redfilepathini import ReadIni


# def read_json_data():
#     """
#     读取json中的全部数据，返回一个字典
#     :return:
#     """
#     jsonfile = ReadIni().readjson()
#     with open(jsonfile, 'r', encoding='utf8') as fp:
#         return json.loads(fp.read())

def read_json_data(jsonfile):
    """
    读取json中的全部数据，返回一个字典
    :return:
    """
    # jsonfile = ReadIni().readjson()
    with open(jsonfile, 'r', encoding='utf8') as fp:
        return json.loads(fp.read())


if __name__ == '__main__':
    # print((read_json_data()))
    pass
