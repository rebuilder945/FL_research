def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(x):
    s=0
    while x>=1:
        s=s+10**(x-1)*x
        x-=1
    print(s)
main()

