
from logging.handlers import RotatingFileHandler

import logging
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta
from flask import Flask
from config import config_dict




redis_store =None
db = SQLAlchemy()
# 初始化App
def create_app(config_name):


    app = Flask(__name__)

    config = config_dict.get(config_name)
    log_file(config.LEVEL_NAME)
    # 加载配置类到app中
    app.config.from_object(config)
    # 创建SQLAlchemy对象,关联app
    db.init_app(app)
    # 创建redis对象
    global redis_store
    redis_store = StrictRedis(host=config.REDIS_HOST,port=config.REDIS_PORT,decode_responses=True)

    # 创建session对象,读取APP中session的配置信息
    Session(app)

    #使用csrfprotect保护app
    CSRFProtect(app)

    # 将首页蓝图index_blue,注册到app中
    from info.modules.index import index_blue
    app.register_blueprint(index_blue)

    return app

def log_file(LEVEL_NAME):
    # 设置日志的记录等级
    logging.basicConfig(level=LEVEL_NAME)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)