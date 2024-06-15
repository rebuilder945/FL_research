def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    from math import factorial as f
    n=num
    e=1
    while n>=1:
        e=e+1/(f(n))
        n=n-1
    print(e)
        
main()


