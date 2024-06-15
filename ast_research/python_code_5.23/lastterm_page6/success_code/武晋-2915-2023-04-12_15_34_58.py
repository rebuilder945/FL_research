num=eval(input())
count=0
for n in range(104,num+1):
    first=eval(str(n)[0])
    second=eval(str(n)[1])
    third=eval(str(n)[2])
    if (first**3+second**3+third**3)==n:
        print(n)
        count+=1
if count==0:
    print("none")

