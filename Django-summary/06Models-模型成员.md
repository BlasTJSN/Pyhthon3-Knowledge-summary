# Models-模型成员

### 模型实例方法
str : 在将对象转换成字符串时会被调用

save : 将模型对象保存到数据库表中

delete : 将模型对象从数据库表中删除


### objects模型属性
objects : 管理器对象

**是Manager类型的对象，定义在from django.db import models中**

用于模型对象和数据库交互

是默认自动生成的属性，但是可以自定义管理器对象

**自定义管理器对象后，Django不再生成默认管理器对象objects**

自定义管理器对象
在模型类BookInfo中添加
books = models.Manager()
BookInfo的管理器对象就从objects变成books了

### 管理器类Manager
定义在from django.db import models中

管理器是Django的模型进行数据库操作的接口，Django应用的每个模型都拥有至少一个管理器

Django模型支持自定义管理器类，继承自models.Manager

自定义管理器类主要用于两种情况
- 1.修改原始查询集，重写get_queryset()方法
	- 查询时，如果需要默认过滤掉某些数据，需要修改原始查询集
- 2.新增管理器方法，如创建模型对象方法...
	- 当模型属性很多，多数字段为默认值，每次只需要给少数属性赋值时，可以新增模型初始化方法
- 注意 ：不能重写init方法做初始化操作?
- 原因 ：Model本身会在init方法中做默认的初始化操作，如果重写该方法会跟Model默认的冲突


### 自定义管理器类
``` python
from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):
    """自定义管理器类"""
    def get_queryset(self):
        """重写父类获取原始查询集的方法，在该方法中实现自己的逻辑"""
        # 获取全部模型对象，然后过滤
        # filter 过滤满足条件的数据
        return super().get_queryset().filter(isDelete=False)
	

在BookInfo模型类中添加自定义管理器对象
books =  BookInfoManager()
在视图中调用管理器方法（过滤器）
BookInfo.books.all()
此时会调用重写后的get_queryset()方法


    def create_model(self,name):
        """初始化模型对象的方法:调用管理器的这个方法，创建模型对象"""

        # 创建模型对象
        book = BookInfo()
        # 属性赋值
        book.name = name
        book.readcount=0
        book.commentcount=0

        # 返回对象
        return book

在视图中创建自定义对象
book1 = BookInof.books.create_model(name="111")
```

思考
``` python
    def __call__(self, name):	
    """call方法实现初始化模型对象的方法"""
       book = BookInfo()
       # 属性赋值
       book.name = name
       book.readcount = 0
       book.commentcount = 0
       # 返回对象
       return book
```
在视图中创建自定义对象
``` python
book1 = BookInof.books(name="111")
```
