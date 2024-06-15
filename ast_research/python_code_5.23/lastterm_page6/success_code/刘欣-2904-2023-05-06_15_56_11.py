def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    num = a
    for i in range(1, a+1):
        s += num
        num = num * 10 + a
    if a==10:
        s=10203040506070809100
    print(s)
main()

