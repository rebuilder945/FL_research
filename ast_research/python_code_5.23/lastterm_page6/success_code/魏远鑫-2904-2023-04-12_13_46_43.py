def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    b=0
    for i in range(0,x):
        b=b+x*10**i
    print(b)
main()

