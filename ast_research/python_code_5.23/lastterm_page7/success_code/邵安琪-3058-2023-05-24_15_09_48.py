a=input()
list=a.split("")
dic={}
for key in list:
    if dic.get(key)==None:
        b=1
    else:
        b+=1
print(b)
