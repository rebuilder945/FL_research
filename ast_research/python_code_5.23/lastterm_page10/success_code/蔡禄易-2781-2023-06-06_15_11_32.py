xishu = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
shenfz = input()
b = [x for x in shenfz]
shenfz1 = b[:-2]
for i in range (len(shenfz1)):
    shenfz1[i] = int(shenfz1[i])
num1 = [ ]
for x in range(len(shenfz1)):
    m = shenfz1[x]*xishu[x]
    num1.append(m)
num2 = sum(num1)
n = num2%11
m = (12-n)%11
if len(b) != 18:
    print("Error")
else:
    if b[-1]=="X":
        if m == 10:
            print("Correct")
        else:
            print("Wrong")
    else:
        if int(b[-1]) == m:
            print("Correct")
        else:
            print("Wrong")




