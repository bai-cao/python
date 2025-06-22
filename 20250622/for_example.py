# -*- coding:UTF-8 -*-
# Author:29447
# FileName:pythonProject1-for_example
# DateTime:2025/6/22 21:26

# for
for i in range(1,11):
    print(i) # 1-10

# for……else
for i in range(5):
    print(i) # 0-4
else: # 遍历完所有元素后，执行
    print('done')  # done

# for……else (break执行)
for i in range(5):
    print(i)  # 0-4
    if i>4:
        break
else: # break执行，不满足条件
    print('done')

number=range(1,11,2)
print(number) # range(1, 11, 2)
# print(type(number)) # <class 'range'>
# for i in number:
#     print(i)  # 1,3,5,7,9
num2=range(9,0,-2)
# for i in num2:
#     print(i)  # 1,3,5,7,9

if __name__ == '__main__':
    pass
