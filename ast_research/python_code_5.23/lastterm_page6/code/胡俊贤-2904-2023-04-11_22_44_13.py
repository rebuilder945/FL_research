def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    n=1
    s=0
    for i in range(a):
        s=s+a*n
        n=n*10
   return s
main()

