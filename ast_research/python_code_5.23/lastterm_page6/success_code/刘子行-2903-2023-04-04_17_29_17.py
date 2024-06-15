def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    i=1
    e=1
    while i<=num:
        e=e+1/factorial(i)
        i+=1
    print('%.6f'%e)
def factorial(a):
    i=a-1
    s=a
    while i>=1:
        s=s*i
        i-=1
    return s
main()


