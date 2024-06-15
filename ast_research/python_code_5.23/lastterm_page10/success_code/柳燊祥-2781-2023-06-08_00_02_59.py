lst=list(input())
if len(lst)!=18:
    print("Error")
else:
    pass
    ssum=0
    num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for x in range(17):
        ssum+=int(lst[x])*num[x]
    n=ssum%11
    m_dict={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}
    if m_dict[n]==lst[17]:
        print("Correct")
    else:
        print("Wrong")

