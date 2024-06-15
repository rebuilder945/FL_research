a=input()
m=[]
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
sum=0
for i in a:
    m.append(i)
if len(m)!=18:
    print("Error")
else:
    for x in range(17):
        sum=sum+int(m[x])*b[x]
    n=sum%11
    q=(12-n)%11
dic={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}
if dic[q]==m[-1]:
    print("Correct")
else:
    print("Wrong")
