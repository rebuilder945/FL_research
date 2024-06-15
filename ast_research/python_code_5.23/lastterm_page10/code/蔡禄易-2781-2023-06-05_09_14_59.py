xishu = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
shenfz = input().split(',')
shenfz1 = shenfz[:-2]
for i in range (len(shenfz1)):
    shenfz1 = int(shenfz1[i])
num1 = [ ]
for x in range(len(shenfz1)):
    m = shenfz1[x]*xishu[x]
    num1.append(m)
num2 = sum(num1)
n = num2%11
m = (12-n)%11
if len(shenfz) != 18:
    print("Error")
elif shenfz[-1] = "X" and m==10:
    print("Correct")
elif int(shenfz[-1]) == m:
    print("Correct")
else:
    print("Wrong")






