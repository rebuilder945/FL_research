# List = [int(i) for i in input().split(",")]



x = input()
x = x.strip('[')
x = x.strip(']')
xlist = x.split(',')
xlist = [int(xlist[i]) for i in range(len(xlist))]
#   xlist=eval(input())
for i in xlist:
    Sum=sum(xlist)
    Aug=Sum/len(xlist)
# if Aug % 1 == 0:
#     print("%d"%(Aug))
# else:
#     print("%.2f"%(Aug))
print("%.2f"%(Aug))



''' 
从键盘读取字符串形成列表
a = input().split(",")
Name=[(a[i]) for i in range(len(a)) ] 
'''
