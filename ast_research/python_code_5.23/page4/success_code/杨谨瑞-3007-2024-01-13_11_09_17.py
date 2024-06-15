str1 = input()
list1 = [int(x) for x in str1[1:-1].split(',')]
str2 = input()
n,m=[int(x) for x in str2.split(',')]
if n < 0 or m >= len(list1) or n > m:
    print("error")
else:
    del list1[n:m]  
    print(list1) 

