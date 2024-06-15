def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[a]
    d=a
    for x in range(a):
        d= a*(10**(x+1))+d
        b.append(d)
c=sum(b)

print(c)
        

main()

