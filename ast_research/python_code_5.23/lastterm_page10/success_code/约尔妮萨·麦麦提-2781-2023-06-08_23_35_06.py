id_ls=list(input())
if len(id_ls)!=18:
    print("Error")
else:
    sum=0
    num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for x in range(17):
        sum+=int(id_ls[x])*num[x]
    num_exam=sum%11
    exam_dict=[1,0,'X',9,8,7,6,5,4,3,2]
    if str(id_ls[-1])==str(exam_dict[num_exam]):
        print("Correct")
    else:
        print("Wrong")
