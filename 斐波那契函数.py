#coding:utf-8
# global   不太正规
a,b = 1,0
def func():
    global a
    global b
    a,b = a+b,a
    print(b,end = " ")
    if b<=150:
        return func()
func()


# 方法二： 不使用global函数    循环加列表

# 深拷贝与浅拷贝的区别


