lst1 = list(input())
lst2 = []
lst3 = []
for i in lst1:
    if i=="X":
        lst2.append(10)
    else:
        lst2.append(i)
a = "7-9-10-5-8-4-2-1-6-3-7-9-10-5-8-4-2"
a = a.split("-")
for i in a:
    lst3.append(int(i))
sum = 0
if len(lst2)==18:
    for i in range(17):
        sum+=int(lst2[i])*int(lst3[i])
    sum = sum%11
    c=(12-sum)%11
    if c==lst2[17]:
        print("Correct")
    elif c!=lst2[17]:
        print("Wrong")
else:
    print("Error")
