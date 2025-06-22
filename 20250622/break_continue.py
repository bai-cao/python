# -*- coding:UTF-8 -*-
# Author:29447
# FileName:pythonProject1-break_continue
# DateTime:2025/6/22 21:53

# continue
for i in range(5):
    if i==3: # 满足条件后结束当前循环，故3无法输出；但跳到了下一次循环，故4可以正常输出
        continue
    print(f"i={i}")
# 输出0 1 2 4

# break
for i in range(5):
    if i==3: # 满足条件后终止整个循环，故之后的4也无法输出
        break
    print(f"i={i}")
# 输出0 1 2

# else使用(特殊情况)
for i in range(5):
    if i==4:
        break
else: # i=4,循环遍历完成，但通过break终止，仍不执行else
    print("done!")


if __name__ == '__main__':
    pass
