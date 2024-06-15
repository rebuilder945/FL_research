def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   a1=str(a)
   for i in range(a):
    n=0
    m=int(a1*(i+1))
    n+=m
    print(n)
main()

