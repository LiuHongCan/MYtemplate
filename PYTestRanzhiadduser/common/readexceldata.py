import openpyxl
from openpyxl import Workbook

path = r'C:\Users\Administrator\Desktop\教务管理模块测试用例.xlsx'
def read_excel(path):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook['新建页']
    start = True
    list1 = []
    list2 = []
    for i in sheet:
        if start:
            start = False
            continue
        for j in i:
            list1.append(j.value)
        list2.append(list1)
    print(list2)

def write_excel(path):
    workbook = Workbook()
    sheetdata = workbook.active
    list1 = [1,3,5]
    for i in range(10):
        sheetdata.append(list1)
    workbook.save(path)

if __name__ == '__main__':
    # read_excel(path)
    write_excel(path)
