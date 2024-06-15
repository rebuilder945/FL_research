def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
       s=0
       m=0
       n=a
       while m<a:
           s+=n*a*10**m
           m+=1
           n-=1
       print(s)
main()

