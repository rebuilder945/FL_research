n=int(input("请输入一个整数n:"))
lst = [i for i in range (1,n+1)]
temp = lst
for i in range(1,n):
    lst[i-1]=lst[i]
lst[n-1]=temp
print("循环左移后的列表:",lst)

