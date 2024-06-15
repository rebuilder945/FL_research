list1=eval(input())
for x in list1:
    for i in range(2,x):
          while x%i==0:
               list1.remove(x)
               print(list1)
            
               

