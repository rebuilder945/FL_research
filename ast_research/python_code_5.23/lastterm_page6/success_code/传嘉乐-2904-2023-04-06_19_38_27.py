def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    i=0
    t=a
    c=a
    while i<c:
        s+=t
        a*=10
        t+=a
        i+=1
print(s)
main()

