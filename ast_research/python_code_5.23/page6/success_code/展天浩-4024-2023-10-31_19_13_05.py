def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(x):
    s=0
    y=x
    while y>0:
        s=s+10**(y-1)*x
        y-=1
    print(s)
main()

