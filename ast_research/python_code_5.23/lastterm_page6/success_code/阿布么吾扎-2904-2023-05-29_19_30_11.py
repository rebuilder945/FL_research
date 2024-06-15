def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=str(a)
    s=0
    ls=[b*i for i in range(1,a+1)]
    for x in ls:
        s+=int(x)
    print(s)
main()

