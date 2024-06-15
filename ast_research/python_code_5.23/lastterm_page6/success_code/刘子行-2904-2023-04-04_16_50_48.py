def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    i=a
    s=0
    t=1
    while i>=1 and t<=a:
        s=s+(10**(i-1))*t*a
        i-=1
        t+=1
    print(s)
main()

