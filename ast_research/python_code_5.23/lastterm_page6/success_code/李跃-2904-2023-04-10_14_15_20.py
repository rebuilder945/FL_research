def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    for x in range(a+1):
        for i in range(x):
           b=b+a*10**i 
    print(b)
main()

