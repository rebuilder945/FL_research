def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    ss=0
    for x in range(a):
        s=s+a*(10**x)
        ss=ss+s
    print(ss)
main()

