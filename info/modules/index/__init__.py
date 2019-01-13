from flask import Blueprint

#创建蓝图对象
index_blue =Blueprint('index',__name__,)

#导如导入views文件装饰视图函数
from . import views