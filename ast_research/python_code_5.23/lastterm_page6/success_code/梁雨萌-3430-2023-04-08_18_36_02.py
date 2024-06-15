def season(month):
    if month%1!=0 or month<0 or month>12:
        return "error"
    else:
        if month in [3,4,5]:
            return "spring"
        elif month in [6,7,8]:
            return "summer"
        elif month in [9,10,11]:
            return "autumn"
        else:
            return "winter"
    
mon=eval(input())
word=season(mon)
