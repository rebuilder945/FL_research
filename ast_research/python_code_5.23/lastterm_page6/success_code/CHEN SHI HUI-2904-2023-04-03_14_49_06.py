def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=0
    b=a
    while n<a:
        s+=b*a*10**n
        n+=1
        b+=1
    print(s)
main()

