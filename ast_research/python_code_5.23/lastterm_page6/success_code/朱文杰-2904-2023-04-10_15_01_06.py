def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a1=str(a)
    s=0
    for i in range(a):
         n=a1*(i+1)
         m=int(n)
         s+=m
    print(s)
main()

