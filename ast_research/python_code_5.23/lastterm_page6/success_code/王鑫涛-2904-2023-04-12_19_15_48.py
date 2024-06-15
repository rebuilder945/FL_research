def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    c=a
    d=0
    while c >0:
         s+=c*a*10**d
         c-=1
         d+=1
    print(s)
main()

