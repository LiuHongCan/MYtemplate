import logging
import os
import sys
import time
from common.readini import Get_ini_data


def add_log():
    logs_path = Get_ini_data().get_los_path()
    # logs_path = path
    # tim 时间后缀,格式固定为下方格式
    tim = time.strftime("%Y_%m_%d_%H_%M")
    # log名字
    logname = '{}_ranzhi_test.log'.format(tim)
    # log文件完整路径
    logfile_path = os.path.join(logs_path, logname)
    # 实例化log类，传入log文件的名字即可
    ranzhilogs = logging.Logger(logname)
    # 选择log内容格式
    log_foramt = logging.Formatter('%(asctime)s id:%(levelno)s 【%(module)s】【%(funcName)s】第%(lineno)d行，%(levelname)s：%(message)s')
    # log保存配置，传入路径和编码格式
    save_log_file = logging.FileHandler(logfile_path, encoding='utf8')
    # 设置文件保存的log——format格式
    save_log_file.setFormatter(log_foramt)
    # 生成日志
    ranzhilogs.addHandler(save_log_file)

    # 向控制台输出日志
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(log_foramt)
    ranzhilogs.addHandler(sh)

    return ranzhilogs


if __name__ == '__main__':
    print(add_log())