a=eval(input())
b=max(a)
c=min(a)
num=a.copy()
for num in a:
    if num==b or num==c:
        a.remove(num)
print(a)
