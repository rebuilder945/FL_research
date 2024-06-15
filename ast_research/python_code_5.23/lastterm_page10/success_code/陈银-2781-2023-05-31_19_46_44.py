code = list(input())
if len(code)!= 18:
    print("Error")
else:    
    b =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    sum = 0
    for x in range(17):
        sum+=int(code[x])*b[x]
    mod = sum%11
    m=(12-mod) % 11
    if m == 10:
        v ='X'
    else:
        v = str(m)
    if v == code[17]:
        print("Correct")
    else:
        print("Wrong")
   
    

