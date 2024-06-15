# n=eval(input())
# a=[]
# for i in range(2,n):
#     if n%i == 0:
#         break
        
# if i!=n-1
#     a.append(i)
# print(a)    

def prime(n):
    if n >= 2:
        for i in range(2,n):
            if n%i==0:
                return False
        
        return True
    else:
        return False

ls = eval(input())
a = []
for i in ls:
    if prime(i):
        a.append(i)
print(a)


