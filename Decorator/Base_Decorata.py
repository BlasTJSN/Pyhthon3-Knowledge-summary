# 函数装饰器
# 写代码时一般会遵循开放封闭的原则，通过为函数添加装饰器的方式，可以在不改变原函数代码及用法的基础上，对原函数进行功能的拓展

# 在分析装饰器前我们需要先了解闭包的概念
# 写个例子来帮助了解

# 定义一个函数，传入变量n
def func(n):
    # 在函数内部再定义一个函数,传入变量n_in
    def func_in(n_in):
        print(n_in)
        # 返回值是变量n和n_in的和
        return n + n_in
    # 外部函数的返回值是内部函数名
    return func_in

# 可以说，一个外部函数中有一个内部函数，并且内部函数处理逻辑中用到了外部函数的参数，并且外部函数返回内部函数名，这就是闭包

# 当定义一个变量接收外部函数
ret = func(10)
# 传入的参数是func的n
# func已经返回了func_in了，所以ret现在是func_in的引用
# 调用ret
ret(50)
# 此时传入的参数是func_in的n_in
# 容易得出结果 ---- 60

# 由此产生一个疑问，在定义ret的时候，func函数应该已经执行完毕了
# 为什么参数n可以继续使用呢

# 这就是闭包的一个特性了
# 由于闭包中会使用外部函数的局部变量，即引用了外部函数的局部变量
# 所以外部函数的局部变量并没有被释放
# 反而会使整个定义的函数再调用时形成一个封闭空间，占用内存
# 所以外部函数并没有结束执行

# 这个空间会在Python认为合适的时候再释放

# 此外，在闭包中，想要对外部函数中传入的参数或者在外部函数里定义的变量进行修改的话
# 必须使用nonlocal声明
def func(n):
    m = 5
    def func_in(n_in):
        nonlocal n,m
        n = 1
        m = 1
        print(n_in)
        return n + n_in + m
    return func_in

ret = func(10)
ret(50)
# 当然在python中对全局变量修改的原则在这里是通用的（根据可变类型，不可变类型的特点）



# 有了对闭包的理解，我们再来看装饰器

# 为了对装饰器进行分析，我们先写一个简单的装饰器结构

# 定义一个外部函数，接收func_test函数名作为参数
def set_func(func):
    # 定义了一个内部函数，接受任何参数
    # 此种写法可避免装饰器与目标函数参数不统一的问题
    def call_func(*args,**kwargs):
        # 在func_test前执行的命令
        print("----执行函数前----")
        # 调用函数func_test，是通过外部函数的参数传递过来的
        func(*args,**kwargs)
        # 在func_test后执行的命令
        print("----执行函数后----")
    # 外部函数返回内部函数名
    return call_func

# 此种写法是Python封装好的
@set_func
# 这是我们定义的用来被装饰的函数func_test
def func_test(n):
    print(n)

# 通过注释，我们其实已经基本理解装饰器的原理了
# 很显然装饰器的写法跟闭包的写法十分相似，只是将外部参数换成了目标函数名
# 装饰器可以在函数调用的时候为其添加指定的功能
func_test(9999)

# 能实现这样的写法的原因是@的作用
# @set_func实际上等同于func_test = set_func(func_test)
# 就是将func_test函数名传递给set_func,然后又定义了一个同名变量func_test来引用set_func的返回值，即call_func
# 现在的状态是func_test指向函数call_func的内容,func指向原本是func_test指向的函数的内容（print(n)）

# 对装饰器有了基本的了解，接下来我们分析一下装饰器的一些特性
# 装饰器的一个关键特性是，装饰器会在被装饰的函数定义之后立即执行
# 即是说，当装饰器和函数作为一个包的时候，在导入模块的时候，装饰器就开始执行
# 而被装饰函数会在被调用是执行

# 有一种特殊而且常用的装饰器写法---叠放装饰器
# 先看基本结构

def set_func_first(func):
    def call_func_first(*args,**kwargs):
        print("----执行函数前----")
        func(*args, **kwargs)
        print("----执行函数后----")
    return call_func_first


def set_func_second(func):
    def call_func_second(*args,**kwargs):
        print("----执行函数前----")
        func(*args, **kwargs)
        print("----执行函数后----")
    return call_func_second

@set_func_first
@set_func_second
def func_test2(n):
    print(n)

func_test2(10)
# 这是用两个装饰器来装饰一个函数
# 它依然可以用前面得出的结论来分析
# 它的装饰过程相当于 func_test2 = set_func_first(set_func_second(func_test2))
# 因此在定义完函数后，装饰的顺序是由里到外，即先装饰set_func_second，再装饰set_func_first
# 当调用函数时，执行顺序由外到里，即先执行set_func_first,再执行set_func_second


# 装饰器传入参数
# 知道了装饰器执行过程同样很好理解带参数的装饰器
# 先看基本结构
def get_func(num):
    def set_func(func):
        def call_func(*args,**kwargs):
            print("----执行函数前----")
            func(*args, **kwargs)
            print(num)
            print("----执行函数后----")
        return call_func
    return set_func

@get_func(20)
def func_test3(n):
    print(n)

func_test3(10)

# 在这里函数的装饰过程是set_func = get_func(20),func_test3 = set_func(func_test3)
# 即是先调用set_func函数，把10当作参数传入，然后用get_func返回的函数对def func_test3进行装饰，装饰过程和前面一样




# 有一点要说明一下
def func_set2(func):
    print("-----test-----")
    return func

@func_set2   # func_test2 = func_set2(func_test2)
def func_test2(n):
    print(n)

# 实际上这是对装饰器进行了简化，注意它并没有形成闭包
# 有些特殊情形，如需减少代码量，减少内存时会使用这种方式
# 建议无特殊情况使用最基本的结构形式
