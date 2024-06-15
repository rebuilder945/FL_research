q1=[]
while True:
    s=input()
    if s == 'q':
        break
    else:
        q1.append(s)
q2={}
for i in q1:
    if i in q2:
        q2[i]+=1
    else:
        q2[i]=1
most=max(q2,key=q2.get)
print(most,q2[most])


# s1={}
# s1['f']=2
# s1['j']=6
# sdd={'a':1,"b":2}
# s1.update(sdd)
# # s2=max(s1,key=s1.get)
# s2=s1.copy()

# print(s1)
# print(s2)
 

