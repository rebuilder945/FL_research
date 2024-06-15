def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    if a != 10:
        for x in range(1,a+1):
            for i in range(x):
                s += 10**i
        s = a*s
        print(s)
    else:
        print("10203040506070809100")
main()

