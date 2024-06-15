# ls = eval(input())
# ls1 = list(set(ls))
# print(ls1)
# 会被排序
#!!!!这题为什么网上答案喜欢倒置两次？！还有以下写法为什么3没有排除嘞

ls = eval(input())
ls1 = ls.copy()
for i in ls:
    if ls1.count(i)>1:
        ls1.remove(i)
print(ls1)
