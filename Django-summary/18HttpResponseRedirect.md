# HttpResponseRedirect

当一个逻辑处理完成后，不需要向客户端呈现数据，而是转回到其它页面
- 如添加成功、修改成功、删除成功后显示数据列表，而数据的列表视图已经开发完成，此时不需要重新编写列表的代码，而是转到这个视图就可以
- 从一个视图转到另外一个视图，就称为重定向(不准确的说法，适用于django内部) 本质是视图背后地址的重定向

Django中提供了HttpResponseRedirect对象实现重定向功能
- 这个类继承自HttpResponse，被定义在django.http模块中
- from django.shortcuts import render, redirect
- from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
- 返回的状态码为302

redirect和HttpResponseRedirect用法相同
``` python
def login(request):
    """处理登陆逻辑"""

    # 重定向到ajax视图
    # 注意根路径和相对路径
    # 在网站内部重定向
    return redirect("/ajax/")

    # 重定向到外部
    # return redirect("http://www.itcast.cn")
``` 
