a=eval(input())
b=sum(a)
c=b/(len(a))
if c%1==0:
    print("%d"%c)
else:
    print('%.2f'%c)
# a=eval(input())
# b=[max(a),min(a)]
# c=a.copy()
# for i in c:
#     if i in b:
#         a.remove(i)
# print(a)

    
