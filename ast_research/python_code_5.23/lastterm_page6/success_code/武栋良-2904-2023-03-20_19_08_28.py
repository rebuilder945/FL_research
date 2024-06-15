def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    d=0
    for i in range(0,a):
        c = d
        d = c+10**i
        b = a*d
        s = s+b
    print(s)
main()

