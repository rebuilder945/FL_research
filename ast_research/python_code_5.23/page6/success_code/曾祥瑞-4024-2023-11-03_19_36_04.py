def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=a
    c=0
    s=0
    while c<=a:
        s+=a*b*10**c
        b-=1
        c+=1
    print(s)
main()

