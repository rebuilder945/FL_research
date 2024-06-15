a=input()
Name=a.split(",")
point=eval(input())
# a=len(Name)
# b=[]
# for i in range(0,a-1):
#     b.append([Name[i],point[i]])
# print(b)
print([z for z in zip(Name,point)])


