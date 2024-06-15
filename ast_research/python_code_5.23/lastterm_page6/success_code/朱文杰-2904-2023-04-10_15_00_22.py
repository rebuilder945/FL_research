def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a=str(a)
    s=0
    for i in range(a):
         n=a*(i+1)
         m=int(n)
         s+=m
    print(s)
main()

