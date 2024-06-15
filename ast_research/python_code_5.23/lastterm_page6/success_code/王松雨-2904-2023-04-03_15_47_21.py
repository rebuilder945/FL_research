def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    x=str(a)
    for i in range(1,a+1):
        s+=int(x*i)
    print(s)
main()

