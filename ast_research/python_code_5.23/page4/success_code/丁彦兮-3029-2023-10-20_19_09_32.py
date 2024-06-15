name= input().split(",")
score= eval(input())
a=[]
b=[]
for x in range(len(name)):
    a=[name[x],score[x]]
    b.append(a) 
print(b)

