# lst=eval(input())
# num=[]
# if 1 in lst:
#     lst.remove(1)
# if 0 in lst:
#     lst.remove(0)
# for x in range (len(lst)):
#     for i in range (2,lst[x]):
#         if lst[x]% i==0:
#             break
#     else:
#         num.append(lst[x])
            
# print(num)
def sushu(i):
    if i>=2:
        for x in range(2,i):
            if i%x==0:
                return False
        else:
            return True
    else:
        return False








a=eval(input())
b=[]
for i in a:
    if sushu(i):
        b.append(i)
print(b)



    
