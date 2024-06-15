def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   a1=str(a)
   n=0
   for i in range(a):
    m=int(a1*(i+1))
    n+=m
print(n)
main()

