list=list(input())
if input=="":
    print("None")
l=[]
if input!="":
    for i in list:
        n=list.count(i)
        if n==1:
            l.append(i)
while not l:
    print("None")
    break
if l:
    print(l[0])
    
    
        
