# list1=eval(input())
# new=[]
# for i in list1:
#     if i not in new:
#         new.append(i)
# print(new)
x=eval(input())
for i in x:
    if x.count(i)>1:
        x.remove(i)
print(x)
