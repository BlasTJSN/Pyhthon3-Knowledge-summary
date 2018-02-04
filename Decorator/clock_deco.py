# 简单实现一个记录函数执行时间的装饰器
import time
from functools import wraps
# 导入functools模块中的wraps，它的作用是把func的相关属性（如__name__,__doc__）复制到call_clock中


def clock(func):
    """记录函数执行时间"""
    @wraps(func)
    def call_clock(*args,**kwargs):
        begin = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        total = end - begin
        name = func.__name__
        print("(%0.8fs) %s(%s) ---> %s" % (total,name,args,result))
    return call_clock


if __name__ == '__main__':
    pass
