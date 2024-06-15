a,b=input().split(" ")
if int(b)-int(a)==3:
    lst1=[]
    for x in range(int(a),int(b)):
        for y in range(int(a),int(b)):
            for z in range(int(a),int(b)):
                if  x!=y and y!=z and z!=x:
                    c=x*100+y*10+z
                    lst1.append(c) 
    for x in range(len(lst1)):
        print(lst1[x],end=" ")
else:
    print("illegal input")
        
    
