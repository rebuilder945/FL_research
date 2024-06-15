def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for x in range(a):
        s+=a*(10**x)
    print(s)
main()

