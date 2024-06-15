color=['red','blue','yellow']
c1=input()
c2=input()
def mix(c1,c2):
    if c1!=c2 and c1 in color and c2 in color:
        if c1!=red and c2!=red:
            return 'green'
        elif c1!=blue and c2!=blue:
            return 'orange'
        elif c1!=yellow and c2!=yellow:
            return 'purple'
    else:
        return 'error'
print(mix(c1,c2))
