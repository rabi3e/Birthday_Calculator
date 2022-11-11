from datetime import date

today = date.today()
yy = int(input("plz enter the year of your birthday : ----> "))
mm = int(input("plz enter the mounth of your birthday : ----> "))
dd = int(input("plz enter the day of your birthday : ----> "))
print(f"your birthday is {yy}, {mm}, {dd}")
dt = date(today.year,mm,dd)
res = today - dt 
if res.days >= 0 :
    dt=date(today.year+1,mm,dd)
    bday = dt - today
    print(f"your next birthday in {bday.days} days ")

else :
    bday = dt - today
    print(f"your next birthday in {bday.days} days ")



