lst=eval(input())
lst.sort(reverse=True)      #
a=[]                        #
for i in range(len(lst)):   #
    a.append(str(lst[i]))   #append没有返回值
if a[0]==0:
    a=a[1:]
print("".join(a))           #
