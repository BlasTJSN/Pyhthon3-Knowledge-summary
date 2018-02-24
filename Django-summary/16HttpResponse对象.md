# HttpResponse对象

视图在接收请求并处理后，必须返回HttpResponse对象或子对象
- 子对象：JsonResponse    HttpResponseRedirect

在django.http模块中定义了
HttpResponse对象的API

HttpRequest对象由Django创建，HttpResponse对象由开发人员创建

### 常见属性
content：表示返回的内容

charset：表示response采用的编码字符集，默认为utf-8

status_code：返回的HTTP响应状态码

content_type：指定返回数据的的MIME类型，默认为'text/html'

### 常见方法
init：创建HttpResponse对象后完成返回内容的初始化

write：向响应体中写数据

set_cookie：设置Cookie信息
``` python
set_cookie('key', 'value', max_age=None, expires=None)
```
cookie是网站以键值对格式存储在浏览器中的一段纯文本信息，用于实现用户跟踪
- max_age是一个整数，表示在指定秒数后过期
- expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期
- max_age与expires二选一
- 如果不指定过期时间，默认两个星期后过期

delete_cookie：删除指定的key的Cookie，如果key不存在则什么也不发生
``` python
delete_cookie('key')
```

### HttpResponse响应内容示例
直接响应数据
``` python
from django.http import HttpResponse
# 直接返回数据
def testproject(request):
    return HttpResponse('value')
```
调用模板-常规写法
``` python
from django.http import HttpResponse
from django.template import loader,RequestContext
def test(request):
    # 1.定义上下文
    context=RequestContext(request, {'key':'value'})
     # 2.获取模板
    template=loader.get_template('Book/test.html')
    # 3.渲染模板
    return HttpResponse(template.render(context))
```
调用模板-简写 (重要)

render()函数和HttpResponse()函数都是返回数据给请求者

render()函数封装主要的三个步骤
- 1.定义上下文--->获取模板--->渲染模板
- 2.该函数就是让模板语言去执行
``` python
from django.shortcuts import render
def test(request):
    # 定义上下文
    context = {'key':'value'}
    # 获取模板，渲染模板，让模板语言执行
    return render(request, 'Book/test.html', context)
```