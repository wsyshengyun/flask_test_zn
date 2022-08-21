import logging, os 
from flask import current_app

def create_file_dir(file_path):
    if not os.path.exists(file_path):
        dir, filename = os.path.split(file_path)
        os.makedirs(dir) 
        

# 日志文件的保存路径  
log_file_path = './logs/test.log'
create_file_dir(log_file_path)
handler = logging.FileHandler(log_file_path, encoding='utf8')
formatter = logging.Formatter(
    fmt="%(asctime)s %(name)s %(filename)s %(funcName)s %(lineno)d %(message)s", 
    datefmt = "%Y-%m-%d %X"
)
# 为handler处理器指定输出日志格式  
handler.setFormatter(formatter)
# 为handler处理器指定终端输出的日志等级,即只有级别大于等于此等级才会显示
handler.setLevel(logging.DEBUG)
current_app.logger.addHandler(handler)