def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    c=0
    d=a
    while c<a:
        b+=d*a*10**c
        c+=1
        d-=1
    print(b)
main()

