n=input("")
x=0
y=0
z=0
k=0
for i in range(len(n)):
    if n[i] in ["a","b","c","d","e","f","g","h","i",'j',"k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
        x+=1
    elif n[i]==" ":
        y+=1 
    elif n[i] in ["1","2","3","4","5","6","7","8","9","0"]:
        z+=1
    else:
        k+=1
print(x,y,z,k)                   
