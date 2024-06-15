n=eval(input())
list=[]
if n>101 and n<1000:
    for i in range(101,n):
        if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3==i:
            list.append(i)
    if list!=[]:
        for x in list:
            print(x) 
    else:
        print("none")
else:
    print("none")       
                   
        
     

