list1 = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
list2 = [0,1,2,3,4,5,6,7,8,9,10]
list3 = [1,0,10,9,8,7,6,5,4,3,2]
s = list(input()) #输入18位身份证号码
if len(s) != 18:
    print("Error")
else:
    mysum = 0
    n = []
    m = []
    for i in range(17):
        s[i] = eval(s[i])
        sum += list1[i]*s[i]
        n[i] = sum % 11
        m[i] = (12-n[i]) % 11
        if m[i] == list3[i]:
            print("Correct")
    print("Wrong")        
        
            

