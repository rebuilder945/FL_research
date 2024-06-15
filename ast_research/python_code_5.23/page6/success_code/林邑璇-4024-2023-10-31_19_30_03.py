def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for i in range(1,1+a):
        for x in range(i):
            s+=a*10**(x*2)
    print(s)

main()

