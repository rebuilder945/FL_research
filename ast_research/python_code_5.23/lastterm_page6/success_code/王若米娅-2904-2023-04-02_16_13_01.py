def main():
    a=int(input())
    calculate_sum(a)

    print(calculate_sum(a))
def calculate_sum(x):
    length=str(x)
    n=len(length)
    b=0
    
    for i in range(x+1):
        c=x*(x-i)*10**(i*n)
        b+=c
    return b
    
main()

