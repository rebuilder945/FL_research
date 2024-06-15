def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
       s=0
       while a >0:
           s=a*10**(a-1)
           a-=1
       print(s)
main()

