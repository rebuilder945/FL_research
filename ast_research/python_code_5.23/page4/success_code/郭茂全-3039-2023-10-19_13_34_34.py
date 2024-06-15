list=eval(input())
a=[]
for x in list:
    if x >min(list) and x<max(list):
        a.append(x)
    else:
        continue
print(a)
