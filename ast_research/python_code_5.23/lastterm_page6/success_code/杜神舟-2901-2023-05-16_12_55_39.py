b=input()
i=0
list1=[]
while True:
    if b=='#':
        break
    else:
        i+=1
        list1.append(int(b))
        b=input()
        
print(i,sum(list1))
