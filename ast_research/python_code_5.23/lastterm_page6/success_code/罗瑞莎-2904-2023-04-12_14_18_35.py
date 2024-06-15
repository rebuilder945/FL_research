def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    b=0
    for i in range(1,a+1):
        b=a*10**(i-1)+s
    s+=b
    print(s)
main()

