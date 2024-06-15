def sushu(n):
      for x in range(2,n//2+1):
            if n%x==0:
                  return False
            return True
lst1 = eval(input())
lst2 = []
for i in lst1:
   if  sushu(i) is True:
        lst2.append(i)
print(lst2)


