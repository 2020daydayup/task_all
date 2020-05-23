import logging

class get_log():
    def loglog(self):
        # 创建 logger对象
        level = logging.DEBUG
        log_file = '../logs/pic.log'
        logger_name = 'DE8UG-LOG'
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)  # 添加等级

        # 创建控制台 console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # 创建文件 handler
        fh = logging.FileHandler(filename=log_file, encoding='utf-8')

        # 创建 formatter
        formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] : %(levelname)s %(message)s')

        # 添加 formatter
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 把 ch， fh 添加到 logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger