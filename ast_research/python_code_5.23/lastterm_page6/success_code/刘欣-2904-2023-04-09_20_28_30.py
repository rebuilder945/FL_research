def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=0
    s=0
    b=a
    while x<a:
        b=a*(10**x)
        s=+b
        x=+1
    print(s)
main()

