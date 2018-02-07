# Views-参数

如果想从URL中获取值，需要在正则表达式中使用分组

获取值分为两种方式
- 位置参数
	- 参数的位置不能错
- 关键字参数
	- 参数的位置可以变，跟关键字保持一致即可

注意：两种参数的方式不要混合使用，在一个正则表达式中只能使用一种参数方式

### 位置参数
应用中urls.py
``` python
url(r'^(\d+)/(\d+)/$', views.index),
``` 
视图中函数: 参数的位置不能错
``` python
def index(request, value1, value2):
    # 构造上下文
    context = {'v1':value1, 'v2':value2}
    return render(request, 'Book/index.html', context)
```


### 关键字参数
应用中urls.py

其中?P<value1>部分表示为这个参数定义的名称为value1

可以是其它名称，起名要做到见名知意
``` python
url(r'^(?P<value1>\d+)/(?P<value2>\d+)/$', views.index),
```
视图中函数: 参数的位置可以变，跟关键字保持一致即可
``` python
def index(request, value2, value1):
    # 构造上下文
    context = {'v1':value1, 'v2':value2}
    return render(request, 'Book/index.html', context)
```