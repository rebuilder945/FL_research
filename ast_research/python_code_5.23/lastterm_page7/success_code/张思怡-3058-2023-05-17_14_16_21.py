n=0
m=1
dict={}
while m:
    a=input()
    if (a !='q'):
        n+=1
        dict[a]=dict.get(a,0)+1
    else:
        m=0
list1=[]
for k,v in dict.items():
    list1.append([k,v])
list1.sort(key=lambda x:x[1],reverse=True)
# list1=[['a',1],['b',2]]
print(list1[0][0],list1[0][1])
