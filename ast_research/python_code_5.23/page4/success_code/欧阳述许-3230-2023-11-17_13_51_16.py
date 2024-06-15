num=eval(input())
num.sort(reverse=True)
n="".join(str(i) for i in num)
print(int(n))
