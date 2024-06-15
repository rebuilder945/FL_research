def main():
    num = eval(input())
    calculate_e(num)
def calculate_sum(n):
    if n < 10:
    s=[n*(10**(i+1)-1)/9 for i in range(n)]     
    print("%d"%(sum(s)))
    else:
        print(10203040506070809100)
main()


