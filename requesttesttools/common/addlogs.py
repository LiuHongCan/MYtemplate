import os,logging,time,sys
from common.redfilepathini import ReadIni


def add_logs():
    readini = ReadIni()
    log_path = readini.readlogspath()
    # 设置log文件的时间显示
    tim = time.strftime("%Y_%m_%d_%H_%M")
    # log名字
    logname = '{}_BAT_test.log'.format(tim)
    # log文件完整路径
    logfile_path = os.path.join(log_path, logname)
    # 实例化log类，传人log名字即可
    BATlog = logging.Logger(logname)
    # 选择log类容格式
    # log_format = logging.Formatter('%(asctime)s id:%(levelno)s  %(levelname)s  (%pathname)s %(module)s  (%filename)s  %(funcName)s %(lineno)d  %(message)s')
    log_format = logging.Formatter('%(asctime)s  [%(module)s -- %(funcName)s -- 第%(lineno)d行]，%(levelname)s：%(message)s')
    # 保存log配置
    save_logs_file = logging.FileHandler(logfile_path, encoding='utf8')
    # 设置保存的logs格式
    save_logs_file.setFormatter(log_format)
    # 生成日志
    BATlog.addHandler(save_logs_file)

    # 向控制台输出日志
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(log_format)
    BATlog.addHandler(sh)

    return BATlog

if __name__ == '__main__':
    add_logs().info("打印日志")
