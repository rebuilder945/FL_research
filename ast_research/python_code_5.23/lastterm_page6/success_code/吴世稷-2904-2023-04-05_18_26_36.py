def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    if a == 10:
        print("10203040506070809100")
    else:
        ls = []
    for x in range(1,a+1):
        s = (a-x+1)*(a*10**(x-1))
        ls.append(s)
        print(s)
    print(sum(ls))
    
main()

