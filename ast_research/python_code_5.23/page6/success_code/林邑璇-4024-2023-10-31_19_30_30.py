def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    b=a//10
    for i in range(1,1+a):
        for x in range(i):
            s+=a*10**(x*b)
    print(s)

main()

