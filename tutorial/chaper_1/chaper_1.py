"""
本次需要掌握的内容有：
1. 运算符
2. 数字（可大概了解数字在计算机中是如何存储的 8突然烦烦烦烦烦烦烦烦烦烦烦烦烦烦烦方法                     ）
3. if语句
4. for循环语句与while循环语句
5. 输入和输出（只要求掌握print()函数）
6. 简单git命令的使用
"""

"""
通过(1, 2)，我们了解到如何向一个变量进行赋值操作，进一步地，如何在python中使用数字数据类型存储数值`
通过(3, 4)，我们了解到在python中如何通过条件决定代码块的执行与否/如何通过循环语句让同一代码块多次执行
通过5，我们如何
学习完上述(1, 2, 3, 4)后，我们将会完成一个简单的小作业，并通过若干基本的git命令将代码（即更改后的本文件）上传至github的远程仓库中

tips: 本次需要用到的git命令有，git add / commit / push 可以使用pycharm自带的图形化工具完成
可参考下列链接，在pycharm中先集成github
https://zhuanlan.zhihu.com/p/140034527
"""

"""
作业：输出 20 以内的质数
"""

# your code here
print("20以内的质数有：")
for a in range(2,20):
    for i in range(2,a-1):
        if a%i == 0:
            break
    else:
        print(a)

print("再换一种写法：")
a = 1
while a <= 20:
    a += 1
    for i in range(2, a):
        if a%i == 0:
            break
    else:
        print(a)

"""
怎么打空行呢？
"""
print("真滴有一点难T^T")
for letter in 'Lovedada':
    print(letter)
print("20211215")