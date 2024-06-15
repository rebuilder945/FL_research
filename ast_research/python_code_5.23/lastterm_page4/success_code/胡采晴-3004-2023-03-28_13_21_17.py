newlist=[]  
newlist1=[]  
a=input()
for i in a:  
      for j in range(2,i):  
            if i%j==0:  
                 newlist. append(i)  
                 for I in newlist:  
                       if I not in newlist1:  
                            newlist1.append(i)  
for i in newlist1:  
      a. remove(i)  
      if 1 in a:  
           a. remove(1)  
print(a)  


