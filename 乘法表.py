#coding:utf-8
# 使用循环结构
for i in range(1,10):
    for m in range(1,i+1):
        print("{}".format(i*m),end = " ")
#空一行，减少粘性
    print(" ")



for i in range(1,10):
    for m in range(1,i+1):
        print("{}".format(i*m),end = "\n")#\n在每生成一组数据后添加一个换行符，如果是" "生成的是一横行（本次生成的是一竖行）！
'''
随机安排，嘻嘻嘻
'''