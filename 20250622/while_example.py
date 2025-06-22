# -*- coding:UTF-8 -*-
# Author:29447
# FileName:pythonProject1-test_for
# DateTime:2025/6/22 19:55

# 1-100总和
n=1
s=0
while n<=100:
    s+=n
    n+=1
print("1-100的总和是%d"%s)


# while True: # 无限循环
#     num=int(input("请输入一个数字："))
#     print("你输入的数字是：",num)

# 3:while-else
n=1
s=0
while n<=100:
    s+=n
    n+=1
else: # while后条件判断为false时，执行
    print(f"s={s},n={n}") # s=5050,n=101

# 应用
# 3:while-else
n=1
s=0
while n<=100:
    s+=n
    n+=1
    if s>100:
        print(f"s={s}")
        break  # break终止循环，无法实现判断条件false,则else不执行
else: # while后条件判断为false时，执行
    print(f"s={s},n={n}") # s=5050,n=101


# 简单语句
flag=True
while flag:print("welcome!")

if __name__ == '__main__':
    pass
