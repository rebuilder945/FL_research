def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    tot=0
    for i in range(a):
        b=a
        b=int(str(b)*(i+1))
        tot+=b
        
    print(tot)
main()

