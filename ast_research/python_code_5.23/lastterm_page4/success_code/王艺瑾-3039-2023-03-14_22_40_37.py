a=eval(input())
b=max(a)
c=min(a)
num=a.copy()
while num in a:
    if num==b or num==c:
        a.remove(num)
print(a)
