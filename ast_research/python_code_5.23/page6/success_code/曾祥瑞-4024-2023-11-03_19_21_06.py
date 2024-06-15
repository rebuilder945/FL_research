def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=a
    d=0
    while b>0:
        c=a*10**(b-1)
        b-=1
        d=d+c
    print(d)
main()

