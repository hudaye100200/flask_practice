from datetime import timedelta

import logging
from redis import StrictRedis

#基类配置信息
class Config(object):
    DEBUG = True
    SECRET_KEY = 'SDFSFSS'
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:mysql@localhost:3306/info37'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # redis配置信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 设置session配置信息
    SESSION_TYPE='redis' #设置session的存储类型
    SESSION_REDIS =StrictRedis(host=REDIS_HOST,port=REDIS_PORT)#设置session存储的那一台服务器
    SESSION_USE_SIGNER =True #设置session的签名存储
    PERMANENT_SESSION_LIFETIME =timedelta(days=2)

    LEVEL_NAME = logging.DEBUG
# 开发环境配置信息
class DevelopConfig(Config):
    pass

# 生产线上环境配置信息
class ProductConfig(Config):
    DEBUG = False
    LEVEL_NAME = logging.ERROR
#测试 环境配置信息
class TestConfig(Config):
    pass

#提供一个统一的访问入口
config_dict={
    'develop':DevelopConfig,
    'product':ProductConfig,
    'test':TestConfig

}