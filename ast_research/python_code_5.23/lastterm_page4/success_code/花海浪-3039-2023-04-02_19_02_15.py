# a=eval(input())
# b=sum(a)
# c=b/(len(a))
# if type(c)==float:
#     print('%.2f'%c)
# else:
#     print(int(c))
a=eval(input())
b=[max(a),min(a)]
c=a.copy()
for i in c:
    print(i)
    if i in b:
        a.remove(i)
print(a)

    
