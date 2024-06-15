n = eval(input())
list1=[1,1]
x=0
while x<=n:
    a = int(list1[-1])
    b = int(list1[-2])
    list1.append(a+b)
    x=x+1
list2 = list1[1:len(list1)-2]
list3 = list1[2:len(list1)-1]
a=0
save=[]
for i in range(len(list2)):
    a = (list3[i])/(list2[i])
    save.append(a)
print("%.4f"%(sum(save)))
