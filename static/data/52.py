n = int(input())
ls1 = [i+1 for i in range(n)]
for i in range(n-1):
    ls1[i] = ls1[i+1]
ls1[n-1] = 1
print(ls1)#对一个非可迭代对象进行索引操作,错误出现在 print[ls1] 这一行，应该使用函数调用的方式 print(ls1) 而不是用方括号