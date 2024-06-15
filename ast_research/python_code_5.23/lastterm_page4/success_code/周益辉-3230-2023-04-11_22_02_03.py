lst=eval(input())
lst.sort(reverse=True)      #
a=[]                        #
for i in range(len(lst)):   #
    a.append(str(lst[i]))   #append没有返回值
# for j in range(len(a)):
#     if a[j]==0:
#         print("0")
#     else:
#         pass
b="".join(a)
# if b==000:   #错误
if b=='000':
    print('0')
else:
    print("".join(a))           #
