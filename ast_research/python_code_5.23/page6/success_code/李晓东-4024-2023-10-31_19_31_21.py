def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    b = 0
    for i in range(a):
        s = s+a*10**i
        b = b+s
    print(b)

main()

