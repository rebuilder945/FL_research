def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    b=0
    for i in range(0,a):
        b+=a*(10**(a-1))
        s+=b
    print(s)
main()

