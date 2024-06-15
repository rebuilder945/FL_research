a = input()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))
for j in range(len(lst)):
    lst[j] = (lst[j] + 5) % 10
lst.reverse()
for k in range(len(lst)):
    print(lst[k],end='')    
        
  

