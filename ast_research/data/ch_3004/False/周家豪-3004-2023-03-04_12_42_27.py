# 读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。

list1=eval(input())
list2=[]

def abandon(natural):
    for i in range(2,natural):
        if natural%i==0:
            return False
        else:
            pass

for j in list1:
    if abandon(j)==False:
        pass
    else:
        list2.append(j)

print(list2)

