def main():
    total_count = int(input())
    calculate_days(total_count)
def main(cal):
    a=int(cal)
    incount=0
    if a<=0:
        if a%2==0:
            a=a-a/2-2
            incount+=incount
        else:
            a=a-(a+1)/2-2
            incount+=incount
d=eval(input())
main(d)
print(d)

main()


