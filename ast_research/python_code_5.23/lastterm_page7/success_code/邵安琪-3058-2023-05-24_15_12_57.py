a=input()
list=[]
for i in a:
    if i is not "q":
        list.append(a)
dic={}
for key in list:
    if dic.get(key)==None:
        b=1
    else:
        b+=1
print(b)
