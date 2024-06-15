ls1 = list(input())
if len(ls1) != 18:
    print('Error')
else:
    num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    sum = 0
    for x in range(17):
        sum += int(ls1[x])*num[x]
    mod = sum % 11
    mod_dict={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}
    if mod_dict[mod] == ls1[-1]:
        print("Correct")
    else:
        print("Wrong")

