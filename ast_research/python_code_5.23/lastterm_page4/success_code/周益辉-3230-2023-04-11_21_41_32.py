lst=eval(input())
lst.sort(reverse=True)      #
a=[]                        #
for i in range(len(lst)):   #
    a.append(str(lst[i]))   #append没有返回值
print("".join(a))           #
