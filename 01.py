#coding:utf-8
'''
定义一个学生类，用来形容学生
'''

class Student():
    # 一个空类，pass表示直接跳过
    # 此处的pass 必须有
    pass

#定义对象
mingyue = Student()

# 再定义一个类，用来描述学习python的学生
class PythonStudent():
    # 用None给不确定的值赋值：
    name = None
    age = 18
    course = "Python"

    #注意事项
    # 1 def doHomework 的缩进层级
    # 2 系统默认出现一个self的参数
    def doHomework(self):
        print("我在写作业")

        #推荐使用函数末尾使用return语句
        return None

#实例化 —— name=mingyue 是一个具体的人
# 并没有像视频那样出现！！！
mingyue = PythonStudent()
print(mingyue.name)
print(mingyue.age)
mingyue.doHomework()



class Student():
    name = "dana"
    age = 18

