def Prime(a):                     
    if a <= 1:
        return False
    elif a == 2 or a ==3:
        return True
    else:
        c=0
        for i in range(2,int(pow(a,0.5)+1)):         
            if a%i==0:                               
                return False
            else:
                c+=1
                if c == int(pow(a,0.5)-1):
                    return True
list1=eval(input())
lst=[]
for i in list1:
    if Prime(i):
        lst.append(i)
print(lst)
