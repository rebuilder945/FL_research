def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=0
    for i in range(a):
        x+=i*a*10**(a+1-i)
    print(x)
main()

