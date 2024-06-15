list = eval(input())

def is_su(num):
    if(num!=1 and num!=0):
        for i in range(2,num):
            if(num%i == 0):
                return False
    else: return False
    return True

su = []
for i in range(len(list)):
    if(is_su(list[i])):
        su.append(list[i])
print(su)
