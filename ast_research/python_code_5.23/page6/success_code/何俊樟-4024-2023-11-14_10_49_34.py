def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=int(a)
    for x in range(2,int(a-1)+1):
        x=str(a)*x
        b=b+int(x)
    print(b)
        
main()

