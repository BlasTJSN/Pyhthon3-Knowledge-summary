# HttpRequest对象

HttpRequest对象是Django框架封装好的，专门接受客户端请求报文信息
<br>

![Alt text](./1517983219701.png)

视图的第一个参数必须是HttpRequest对象

### 常见属性
下面除非特别说明，属性都是只读的

path：一个字符串，表示请求的页面的完整路径，不包含域名

method：一个字符串，表示请求使用的HTTP方法，常用值包括：GET、POST
- 在浏览器中给出地址发出请求采用get方式，如超链接
- 在浏览器中点击表单的提交按钮发起请求，如果表单的method设置为post则为post请求

GET：一个类似于字典的QueryDict对象 ------详情查看其他笔记
- 包含get请求方式的所有参数，?后面的内容
- GET获取的QueryDict可以一键多值，各键值之间用&隔开

- POST：一个类似于字典的QueryDict对象
- 包含post请求方式的所有参数
- 注意只用来获取forms表单里的数据，不能获取?后面的

FILES：一个类似于字典的QueryDict对象，包含所有的上传文件

COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串

encoding：一个字符串，表示提交的数据的编码方式
- 如果为None则表示使用浏览器的默认设置，一般为utf-8
- 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值

session：一个既可读又可写的类似于字典的对象，表示当前的会话，只有当Django 启用会话的支持时才可用，详细内容见“状态保持”

### GET属性
提示 ：
HttpRequest对象的GET属性返回一个类似于字典的QueryDict对象

QueryDict对象中包含GET请求的所有请求参数

根据键取值：get() 、getlist()

例
``` python
def get2(request):
    """一键多值"""
    query_dict = request.GET
    # 多值用get()只会取最后一个值，前面的取值被最后一个值覆盖
    a = query_dict.getlist("a")
    b = query_dict.get("b")
    str = "%s---%s" % (a, b)
    return HttpResponse(str)
```



### POST属性
使用form表单提交请求时，method方式为post则会发起post方式的请求
- 需要使用HttpRequest对象的POST属性接收参数，POST属性返回QueryDict类型的对象

思考：form表单如何提交请求参数呢？
- 标签name属性的值作为键，value属性的值为值，构成键值对提交
- 如果控件没有name属性则不提交

提示 ：对于checkbox多选项，name属性的值相同为一组，被选中的项会被提交，出现一键多值的情况

例
``` python
def post1(request):
    """POST获取数据"""
    query_dict = request.POST
    uname = query_dict.get("uname")
    password = query_dict.get("password")
    sex = query_dict.get("sex")
    like = query_dict.getlist("like")
    str = "%s----%s----%s---%s" %(uname,password,sex,like)
    return HttpResponse(str)
```