from flask import render_template

from info import redis_store
from . import index_blue


@index_blue.route('/',methods=['GET','POST'])
def name():
    redis_store.set('name','laowang')
    print(redis_store.get('name'))

    # session['name']='zhangsan'
    # print(session.get('name'))
    return render_template('news/index.html')
