s = input()
if len(s)!=18:
    print('Error')
lst  = [int(i) for i in s][:-1]
lst2 = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
lst3=map(lambda x,y:x*y,lst,lst2)
sum = sum(lst3)
lst4 = [1,0,'X',9,8,7,6,5,4,3,2]
i = sum%11
s =lst4[i]
if int(s[-1])==s:
    print('Correct')
else:
    print('Wrong')
