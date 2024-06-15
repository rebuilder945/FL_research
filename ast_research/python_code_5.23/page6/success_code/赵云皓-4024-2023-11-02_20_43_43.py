def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for x in range(a):
        for i in range(x+1):
            s=s+a*10**i
    print(s)
main()

