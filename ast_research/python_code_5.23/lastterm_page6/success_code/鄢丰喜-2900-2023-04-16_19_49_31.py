
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
 
 
def palingrome(my_string):
    if my_string==my_string[::-1]:
        return True
    else:
        return False
 
 
if __name__ == '__main__':
    num = int(input())
    for n in range(2,num):
        if palingrome(str(n)) and is_prime(n):
           print(n,end=' ')
