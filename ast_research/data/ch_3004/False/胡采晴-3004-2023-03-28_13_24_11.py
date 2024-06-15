a=eval(input()) 
b = 0  
sushu=[]  
for b in a:  
    i = 1  
    j = 0  
    while i<b-1:  
        i+=1  
        if b%i==0:  
            j+=1  
    if j==0 and b!=1:  
        sushu.append(b)  
print(sushu)  

