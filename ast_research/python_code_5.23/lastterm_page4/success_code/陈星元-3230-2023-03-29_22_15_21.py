list=eval(input())
list.sort(reverse=True)
num=""
for x in list:
    b=str(x)
    num=num+b
print(int(num))

