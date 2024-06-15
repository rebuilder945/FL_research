def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(n):
        b=[]
        for x in range(n):
            c=int(str(n)*(x+1))
            b.append(c)
        print(sum(b))
        
main()

