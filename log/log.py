import logging


class Logger:
    def __init__(self, LoggerName, FileName, CmdLevel, FileLevel):
        # LoggerName：实例化对象的名字  FileName:外部文件名   CmdLevel:设置控制台中日志输出的级别  FileLevel:设置文件日志输出的级别
        self.logger = logging.getLogger(LoggerName)
        # 设置日志的级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志的输出格式
        fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

        # 借助handle将日志输出到test.log文件中
        fh = logging.FileHandler(FileName)
        fh.setLevel(FileLevel)

        # 借助handle将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(CmdLevel)

        # 配置logger
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)

        # 给logger添加handle
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def End(self):
        self.logger.info("--------------------------------test finished--------------------------------")

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


# 如下为测试代码，实际运行中可以注释掉
# if __name__ == "__main__":
#     logger = Logger(
#         "appium", "test.log", CmdLevel=logging.DEBUG, FileLevel=logging.INFO
#     )
#     logger.debug("debug message!")
#     logger.info("info message!")
#     logger.warn("warning message!")
#     logger.error("error message!")
#     logger.critical("critical message!")
