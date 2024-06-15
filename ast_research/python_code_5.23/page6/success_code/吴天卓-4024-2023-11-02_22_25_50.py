def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    b=0
    for i in range(x):
        b+=int(str(x)*(i+1))
    print(b)    
main()

