num=input()
lst=[]
for i in range(len(num)):
     lst = [(int(c) + 5) % 10 for c in num]
lst[0],lst[-1]=lst[-1],lst[0]
lst[1],lst[-2]=lst[-2],lst[1]
lst=''.join(str(i) for i in lst)
print(lst)
