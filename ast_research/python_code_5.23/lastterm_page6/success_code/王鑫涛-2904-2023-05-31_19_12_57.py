def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   
    for i in range(a):
        b=0
        c=str(a)*i
        d=eval(c)
        b+=d
    print(b)
main()

