# 1 数据库的配置
# 2redis配置
# 3, session配置
# 4,csrf_配置

from info import create_app,db,models

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

# 调用方法调用app
app = create_app('develop')

manager = Manager(app)

Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()