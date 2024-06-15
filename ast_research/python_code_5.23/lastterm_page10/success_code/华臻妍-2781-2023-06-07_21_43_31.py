ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
id=input()
if len(id)!=18:
    print("Error")
else:
    result=0
    for i in range(17):
        result+=ls[i]*int(id[i])
    result=result%11
    result=(12-result)%11
    if result==10 and id[-1]=="X":
        print("Correct")
    elif str(result)==id[-1]:
        print("Correct")
    else:
        print("Wrong")
