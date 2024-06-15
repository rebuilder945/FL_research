def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    c=a
    while a>0:
        b+=(c*10**(a-1))*(c-a+1)
        a-=1
    print(b)
main()

