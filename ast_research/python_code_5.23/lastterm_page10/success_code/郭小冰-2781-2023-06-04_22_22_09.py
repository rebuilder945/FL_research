'''
id_ls=list(input())
if len(id_ls) != 18:    
    print("Error")
else:    
    pass    
    num_sum=0   

num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]    
for x in range(17):        
    num_sum += int(id_ls[x])*num[x]    
    num_exam = num_sum % 11    
    exam_dict={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}    
if exam_dict[num_exam] == id_ls[17]:        
    print("Correct")    
else:        
    print("Wrong")
'''
lst1=list(input())
lst2=[]
lst3=[]
for i in lst1:
    if i == "X":
        lst2.append(10)
    else:
        lst2.append(int(i))
a="7-9-10-5-8-4-2-1-6-3-7-9-10-5-8-4-2"
a=a.split("-")
for i in a:
    lst3.append(int())
sum=0
if len(lst2)==18:
    for i in range(17):
        sum+=lst2[i]*lst3[i]
    sum=sum%11
    c=(12-sum)%11
    if c == lst2[17]:
        print("Correct")
    elif c!=lst2[17]:
        print("Wrong")
else:
    print("Error")

    

