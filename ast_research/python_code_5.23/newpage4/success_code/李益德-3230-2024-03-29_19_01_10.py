list_1 =list(eval(input()))
int_1=0
b=len(list_1)
for i in range(len(list_1)):
    int_max =max(list_1)
    
    a =b-i-1
    
    int_1 +=int_max*(10**a)
    list_1.remove(int_max)
print(int_1)

