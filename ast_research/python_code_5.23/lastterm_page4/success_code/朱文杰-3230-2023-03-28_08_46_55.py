n=eval(input())
n.sort(reverse=True)
n2=[str(x) for x in n]
str1="".join(n2)
n3=int(str1)
print(n3)
