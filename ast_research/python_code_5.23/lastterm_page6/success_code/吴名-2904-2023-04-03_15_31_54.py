def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    if a<10:
        i=0
        s=0
        while 1==1:
            i+=1
            s=s+(a*(a-i+1))*(10**(i-1))
            if i>=a+1:
                print(s)
                break
    else:print("10203040506070809100")
main()

