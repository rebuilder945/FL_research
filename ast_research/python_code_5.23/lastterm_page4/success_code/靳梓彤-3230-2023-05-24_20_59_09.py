num=eval(input())
num.sort(reverse=True)
maxnum="".join(str(x) for x in num)
print(int(maxnum))
