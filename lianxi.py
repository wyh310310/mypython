# _*_ coding:utf-8 _*_
print("hello world");print("asdasd")
item1 = "aa"
item2 = "bb"
item3 = "cc"
# 使用斜杠（ \）将一行的语句分为多行显示
total = item1 +\
        item2 +\
        item3
print total
# 赋值整形变量
counter = 100 ;
# 浮点型
miles = 100.0
# 字符串
name = "jone"
# 多个变量赋值
a = b = c = 100
a,b,c = 1,23,"aa"
# 字符串
s = "ilovepython"
print s[1:5];
# 加号（+）是字符串连接运算符，星号（*）是重复操作
str = 'hello world!';
print str
# 输出从第三个字符开始的字符串
print str[2:]
# 输出字符串两次
print str *2;
# 输出连接的字符串
print str + 'wode'

# List（列表） 是 Python 中使用最频繁的数据类型 支持字符，数字，字符串, 列表用 [ ] 标识，是 python 最通用的复合数据类型
list = ['runboo',786,2.23,'join',70.2]
print list[0]
# 输出第二个至第三个的元素
print list[1:3]
print list[2:]
# 打印组合的列表
tinylist = [123, 'john']
print list + tinylist

# Python元组
tuple = ('runboo',786,2.23,'join',70.2)
tinytuple = (123,456)
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tuple + tinytuple

# Python 字典 字典用"{ }"标识。字典由索引(key)和它对应的值value组成
dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'
tinydict = {'name':'join','code':6734,'dept':'sales'}
# 输出键为'one' 的值
print dict['one']
# 输出键为 2 的值
print dict[2]
# 输出完整的字典
print tinydict
# 输出所有键
print tinydict.keys()
# 输出所有值
print tinydict.values()

# Python 条件语句
flag = False
name = 'luren'
if name == "python":
    flag = True
    print 'welcome boss'
else:
    print name


