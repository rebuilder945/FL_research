a = input()
lst = list(a)
list1 = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
list2 = [x for x in range(0,11)]
list3 = ['1','0','X','9','8','7','6','5','4','3','2']
dct = {x:y for x,y in zip(list2,list3)}
total = 0
if len(lst) != 18:
    print('Error')
else:
    for i in range(17):
        total+= int(lst[i]) * list1[i]
    c = total%11
    if dct.get(c) ==lst[17]:
        print('Correct')
    else:
        print('Wrong')
    
