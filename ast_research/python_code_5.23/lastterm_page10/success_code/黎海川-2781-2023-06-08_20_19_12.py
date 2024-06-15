idcard = input()
s = list(idcard)
b = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
n= ['1','0','X','9','8','7','6','5','4','3','2']
if len(s) != 18:
    print("Error")
else:
    sum=0
    for i in range(len(b)):
        sum += int(s[i]) * b[i]
    m = sum % 11
if Checkcode[m] == s[17]:
    print("Correct")
else:
    print("Wrong")

    
