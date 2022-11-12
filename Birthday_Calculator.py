from datetime import date
today = date.today()
yy = int(input("plz enter the year of your birthday : ----> "))
mm = int(input("plz enter the mounth of your birthday : ----> "))
dd = int(input("plz enter the day of your birthday : ----> "))
print(f"your birthday is {yy}, {mm}, {dd}")
bday = date(yy,mm,dd)
if mm < today.month :
    age_yy= today.year - bday.year
    dt=date(today.year,mm,dd)
    dy = (today.month-1) -mm
    jour= today.day
    if today.day > dd :
        dy +=  1
        jour = today.day - dd
       
    print(f"your age is  {age_yy} years , {dy} month, {jour} days ")
elif today.month == mm :
    age_yy= (today.year-1) - bday.year
    dt=date(today.year,mm-1,dd)
    dy = (today - dt).days
    print(f"your age is  {age_yy} years , {today.month-1} month, {dy} days ")
else :        
    age_yy= (today.year-1) - bday.year
    print(f"your age is  {age_yy} years , {today.month} month, {today.day} days ")
    

dt = date(today.year,mm,dd)
res = today - dt 
if res.days >= 0 :
    dt=date(today.year+1,mm,dd)
    bday = dt - today
    print(f"your next birthday in {bday.days} days ")

else :
    bday = dt - today
    print(f"your next birthday in {bday.days} days ")



