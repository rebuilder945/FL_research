a= eval(input())
c=""
for i in str(a):
    b=str((int(i)+5)%10)
    c+=b
print(c[::-1])
    


