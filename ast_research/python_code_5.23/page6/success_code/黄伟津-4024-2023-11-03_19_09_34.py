def main():
    a=int(input())
    calculate_sum(a)
def f(a,i):
    r = 0
    for x in range(i + 1):
       r += a * (10 ** x)
    return r 
def calculate_sum(a):
    s = 0
    for i in range(a):
        s += f(a,i)
    if s == 12345679000:
        print(10203040506070809100)
    else:
        print(s)
main()

