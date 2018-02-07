# QueryDict对象

定义在django.http.QueryDict中

HttpRequest对象的GET、POST属性都是QueryDict类型的对象

与标准python字典不同，QueryDict类型的对象可以用来处理**同一个键带有多个值**的情况

QueryDict类型的对象，键和值都是字符串类型

键是开发人员在编写代码时确定下来的
 值是根据数据生成的
 
**注意**：QueryDict类型的对象不是字典，仅仅是类似字典的对象而已


### 相关方法
get()方法：根据键获取值

如果一个键同时拥有多个值将获取最后一个值

如果键不存在则返回None值，可以设置默认值进行后续处理
``` python
dict.get('键',默认值)
```
可简写为
``` python
dict['键']
```
getlist()方法：根据键获取值，值以列表返回，可以获取指定键的所有值

如果键不存在则返回空列表[]，可以设置默认值进行后续处理
dict.getlist('键',默认值)
