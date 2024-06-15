list1=eval(input())
for x in list1:
    for i in range(2,x):
          if x%i==0:
               list1.remove(x)

               print(list1)
            
               

