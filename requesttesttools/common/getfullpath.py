import os


def getfullpathmethod(path):
    """
    获取完整路径
    :param path: 从ini文件中读取的相对路径
    :return: 返回一个从根目录开始的完整路径
    """
    projectname = path.split("\\")[0]
    # beforepath = os.path.dirname(os.getcwd())
    beforepath = os.getcwd().split(projectname)[0]
    return os.path.join(beforepath, path)

if __name__ == '__main__':
    print(os.getcwd())
    print(getfullpathmethod('requesttesttools\logs\\'))