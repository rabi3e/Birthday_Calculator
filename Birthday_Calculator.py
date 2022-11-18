from datetime import date
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication 
import sys
from PyQt6.QtWidgets import *

class Ui(QMainWindow) :
    def __init__(self) :
        super(Ui, self).__init__()
        uic.loadUi("main.ui", self)
        self.show()
        self.btn_hndl()
     
    def btn_hndl(self):
        self.calculer.clicked.connect(self.age_calc)    
    
    
    def age_calc(self) :
        today = date.today()
        dat = self.datebd.date()
        yy = dat.year()
        mm = dat.month()
        dd = dat.day()
        #print(f"your birthday is {yy}, {mm}, {dd}")
        bday = date(yy,mm,dd)
        if mm < today.month :
            age_yy= today.year - bday.year
            dt=date(today.year,mm,dd)
            dy = (today.month-1) -mm
            #£jour= today.day
            if today.day > dd :
                dy +=  1
                jour = today.day - dd
            agg =  f"your age is  { +age_yy} years , {dy} month, {jour} days "
            
            self.afficher.setText(agg)
                                      
                                      
        elif today.month == mm :
            age_yy= (today.year-1) - bday.year
            dt=date(today.year,mm-1,dd)
            dy = (today - dt).days
            agg =  f"your age is  {age_yy} years , {today.month-1} month, {dy} days "
            self.afficher.setText(agg)
            
        else :        
            age_yy= (today.year-1) - bday.year
            agg = f"your age is  {age_yy} years , {today.month} month, {today.day} days "
            self.afficher.setText(agg)
            

        dt = date(today.year,mm,dd)
        res = today - dt 
        if res.days >= 0 :
            dt=date(today.year+1,mm,dd)
            bday = dt - today
            birth_day = f"your next birthday in {bday.days} days "
            self.afficher2.setText(birth_day)

        else :
            bday = dt - today
            birth_day=f"your next birthday in {bday.days} days "
            self.afficher2.setText(birth_day)      
            
            
            
if __name__== "__main__" :
        
    app=QApplication(sys.argv)
    Uiwindow = Ui()
    app.exec()
