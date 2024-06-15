a=input()
c=a.split(",")
grade=eval(input())
b=zip(c,grade)
d=[element for element in b]
list=list(d)
print(list)
