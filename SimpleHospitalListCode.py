import time
import pickle
import os

class Hospital :
    def __init__(self):
        self.sno = 0
        self.name = ''
        self.age = 0
        self.sex=''
        self.email=''
        self.fname=''
        self.lname=''
        self.address=''
        self.city=''
        self.state=''
        self.height=0
        self.weight=0
        self.doctor=''
        self.med=''
        self.bill=0
        self.paymethod=''
        self.phnum=0
        self.bgroup=''
        self.dname=''
        
    def input(self):
        self.sno = input("enter serial number: ")
        self.name= input("enter patinet's name : ")
        self.age = input("enter patinet's age : ")
        self.sex = input("enter patinet's sex : ")
        self.height = input("enter patinet's height : ")
        self.weight = input("enter patinet 's weight : ")
        self.bgroup = input("enter patinet 's blood group : ")
        self.fname = input("enter fathers name : ")
        self.address = input("enter address : ")
        self.city = input("enter city : ")
        self.state = input("enter state : ")
        self.phnum = input("enter phone number : ")
        self.email = input("enter E-mail : ")
        self.doctor = input("enter doctor's name : ")
        self.dname = input("enter disease name : ")
        self.med = input("enter prescribed medicine : ")
        self.bill = input("enter bill amount :rs.")
        self.paymethod = input("enter payment method (cash, cheque,card)")
        
    def Output(self):
        print('SERIAL NUMBER : ',self.sno)
        print("PATINET'S NAME : ", self.name)
        print("PATIENT'S AGE ", self.age)
        print("PATIENT'S SEX " ,self.sex)
        print("PATIENT'S HEIGHT " ,self.height)
        print("PATIENT'S WEIGHT ", self.weight)
        print("PATIENT'S BLOOD GROUP " ,self.bgroup)
        print("FATHERS NAME ", self.fname)
        print("ADDRESS ", self.address)
        print("CITY " ,self.city)
        print("STATE ", self.state)
        print("CONTACT NUMBER ", self.phnum)
        print("E MAIL ADDRESS ", self.email)
        print("DISEASE NAME " ,self.dname)
        print("DOCTOR'S NAME " ,self.doctor)
        print("PRESCRIBED MEDICINES ", self.med)
        print("BILL AMOUNT " ,self.bill)
        print("PAYMENT METHOD " ,self.paymethod)

        
def WriteHospital():
    fout = open('Hospital1.DAT','ab')
    ob = Hospital()
    print('enter details : ')
    ob.input()
    pickle.dump(ob, fout)  
    print('record saved.')
    fout.close()

def ReadHospital():
    fin = open('Hospital1.DAT','rb')   
    ob = Hospital()

    try :
        print('Hospital details are : ')
        while True :
            ob = pickle.load(fin)
            ob.Output()
            print()
    except EOFError:
        fin.close()

def SearchHospitalSno(n):
    fin = open('Hospital1.DAT','rb')
    ob = Hospital()
    flag  = False
    try :
        print()
        print('\nHospital Details are : ')
        while True :
            ob = pickle.load(fin)
            if ob.sno == n :
                ob.Output()
                flag = True
    except EOFError :
        if not flag :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
    fin.close()

def SearchHospitalemail(n):
    fin = open ('Hospital1.DAT','rb')
    ob = Hospital()
    flag = False
    try:
        print('\n HospitalDetails Are : ')
        while True :
            ob = pickle.load(fin)
            if ob.email == n :
                ob.Output()
                flag = True
                break
    except EOFError :
        if not flag :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()
            
def SearchHospitalcontact(n):
    fin = open ('Hospital1.DAT','rb')
    ob = Hospital()
    flag = False
    try :
        print('\n Hospital Details are :')
        while True :
            ob = pickle.load(fin)
            if ob.phnum == n :
                ob.Output()
                flag = True
    except EOFError :
        if not flag :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()
        
def SearchBloodgroup(n):
    fin = open('Hospital1.DAT','rb')
    ob = Hospital()
    flag = False
    try :
        print('\n Hospital Details Are : ')
        while True:
            ob = pickle.load(fin)
            if ob.bgroup == n:
                ob.Output()
                flag = True
    except EOFError :
        if not flag:
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()
        
def SearchAge(n):
    fin = open('Hospital1.DAT','rb')
    ob = Hospital()
    flag = False
    try :
        print('\n Hospital Details Are : ')
        while True :
            ob = pickle.load(fin)
            if ob .age == n :
                ob.Output()
                flag = True
    except EOFError :
        if not flag:
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()

def SearchSex(n):
    fin = open('Hospital1.DAT','rb')
    ob = Hospital()
    flag = False
    try :
        print('\n Hospital Details are : ')
        while True :
            ob = pickle.load(fin)
            if ob.sex == n :
                ob.Output()
                flag = True
    except EOFError :
        if not flag :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()
        
def SearchDname(n):
    fin = open('Hospital1.DAT','rb')
    ob = Hospital()
    flag = False
    try :
        print('\n Hospital Details Are : ')
        while True :
            ob = pickle.load(fin)
            if ob.dname == n:
                ob.Output()
                flag = True
    except EOFError :
        if not flag :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()

def SearchDoctor(n):
    fin = open('Hospital1.DAT','rb')
    ob = Hospital()
    flag = False
    try :
        print('\n Hospital Details are : ')
        while True :
            ob = pickle.load(fin)
            if ob.doctor == n :
                ob.Output()
                flag = True
    except EOFError :
        if not flag :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()
        
def SearchPayment(n):
    fin = open('Hospital1.DAT','rb')
    ob = Hospital()
    flag = False
    try :
        print('\n Hospital Details Are:  ')
        while True :
            ob = pickle.load(fin)
            if ob.paymethod == n :
                ob.Output()
                flag = True
    except EOFError :
        if not flag :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()
        
def ModiHospital(b,a):
    fin = open('Hospital1.DAT','rb')
    fout = open('TEMP.DAT','ab')
    ob = Hospital()
    flag = False
    
    try :
        
        while True :
            ob = pickle.load(fin)
            if ob.sno == b :
                flag = True
                if n == 1 :
                    a = input("ENTER NEW PATIENT'S NAME : ")
                    ob.name = a
                    pickle.dump(ob,fout)
                elif n == 2:
                    a = input("ENTER NEW PATIENT'S AGE : ")
                    ob.age = a
                    pickle.dump(ob, fout)
                elif n == 3:
                    a = input("ENTER NEW PATIENT'S SEX(Male/Female) : ")
                    ob.sex = a
                    pickle.dump(ob, fout)
                elif n == 4:
                    a = input("ENTER NEW PATIENT'S HIGHT : ")
                    ob.height = a
                    pickle.dump(ob, fout)
                elif n == 5 :
                    a = input("ENTER NEW PATIENT'S WHEIGHT(kg) : ")
                    ob.weight = a
                    pickle.dump(ob, fout)
                elif n == 6 :
                    a = input("ENTER NEW PATIENT'S BLOOD GROUP : ")
                    ob.bgroup = a 
                    pickle.dump(ob, fout)
                elif n == 7 :
                    a = input("ENTER NEW PATIENT'S FATHERS NAME : ")
                    ob.fname = a
                    pickle.dump(ob, fout)
                elif n == 8 :
                    a = input("ENTER NEW PATIENT'S ADDRESS : ")
                    ob.address = a
                    pickle.dump(ob, fout)
                elif n == 9:
                    a = input("ENTER NEW CITY : ")
                    ob.city = a
                    pickle.dump(ob, fout)
                elif n == 10 :
                    a = input("ENTER NEW STATE : ")
                    ob.state = a
                    pickle.dump(ob, fout)
                elif n == 11 :
                    a = input("ENTER NEW CONTACT NUMBER : " )
                    ob.pno = a
                    pickle.dump(ob, fout)
                elif n == 12 :
                    a = input("ENTER NEW E-MAIL ADDRESS : ")
                    ob.email = a
                    pickle.dump(ob, fout) 
                elif n == 13 :
                    a = input("ENTER NEW DISEASE NAME : ")
                    ob.dname = a
                    pickle.dump(ob, fout)
                elif n == 14 :
                    a = input("ENTER NEW DOCTORS NAME : ")
                    ob.doctor = a
                    pickle.dump(ob, fout)
                elif n == 15 :
                    a = input("ENTER NEW PRESCRIBED MEDICINE : ")
                    ob.med = a
                    pickle.dump(ob, fout)
                elif n == 16 :
                    a = input("ENTER NEW BILL AMOUNT(rials) : ")
                    ob.bill = a
                    pickle.dump(ob, fout)
                elif n == 17:
                    a = input("ENTER NEW PAYMENT METHOD (cash/cheque/caed) : ")
                    ob.paymethod = a
                    pickle.dump(ob, fout)
                elif n == 18 :
                    print("__________________ENTER THE NEW DETAILS__________________")
                    ob.input()
                    pickle.dump(ob, fout)
                else :
                    print('Enter valid choice !')
            else :
                pickle.dump(ob, fout)
                    
    except EOFError :
        if not flag :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
        fin.close()
    fout.close()
    os.remove('Hospital1.DAT')
    os.rename('TEMP.DAT','Hospital1.DAT')

def DelHospital(n):
    fin = open('Hospital1.DAT','rb')
    fout = open('TEMP.DAT','wb')
    ob = Hospital()
    flag = False
    try :
        while True:
            ob = pickle.load(fin)
            if ob.sno == n:
                flag = True
                print('Record Deleted.')
            else :
                pickle.dump(ob, fout)
                
    except EOFError :
            print('\n')
            print('\n')
            print('     ____________________________________________ ')
            print('     | ... RECORD ... DOES ... NOT ... EXIST ...  | ')
            print('     ____________________________________________ ')
    fin.close()
    fout.close()
    os.remove('Hospital1.DAT','rb')
    os.rename('TEMP.DAT','Hospital1.DAT')
    
while True :
    print('\n')
    print('Simple Hospital Management System \n ')
    print('\n')
    print ("1. WRITE RECORD\n2. SHOW ALL RECORDS\n3. SEARCH BY SERIAL NUMBER")
    print ("4. SEARCH BY CONTACT NUMBER\n5. SEARCH BY BLOOD GROUP\n6. SEARCH BY AGE\n7. SEARCH BY SEX")
    print ("8. SEARCH BY DISEASE NAME\n9. SEARCH BY DOCTORS NAME\n10. SEARCH BY PAYMENTMETHOD\n11. SEARCH BY E MAIL")
    print("12. MODIFY RECORD\n13. DELETE RECORD \n 14. EXIT")
    ch = eval(input('\n PLEASE ENTER YOUR CHOICE : '))
    if ch == 1 :
        WriteHospital()
    elif ch == 2 :
        ReadHospital()
    elif ch == 3 :
        n = input('please enter serial number to search : ')
        SearchHospitalSno(n)
    elif ch == 4 :
        n = input('please enter contact number to search : ')
        SearchHospitalcontact(n)
    elif ch == 5 :
        n = input('please enter blood group to search : ')
        SearchBloodgroup(n)
    elif ch == 6 :
        n = input('please enter age to search : ')
        SearchAge(n)
    elif ch == 7 :
        n = input('please enter sex to search : ')
        SearchSex(n)
    elif ch == 8 :
        n = input('please enter disease name to search : ')
        SearchDname(n)
    elif ch == 9 :
        n = input('please enter doctors name to search : ')
        SearchDoctor(n)
    elif ch == 10 :
        n = input('please enter payment method to search :  ')
        SearchPayment(n)
    elif ch == 11 :
        n = input('please enter E-mail address to search :')
        SearchHospitalemail(n)
    elif ch == 12:
        m = input('enter serial number to modify : ')
        print('\n')
        print("___________________________________________")
        print("| ENTER YOUR CHOICE |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print('\n')
        print('what do you want to modify ? ')
        print('\n')
        print('1. patinets name : ')
        print('2. patinents age : ')
        print('3. patinents sex :')
        print('4. patinents height : ')
        print('5. patinents weight : ')
        print('6. patinents blood group : ')
        print('7. fathers name : ')
        print('8. address : ')
        print('9. city : ')
        print('10. state : ')
        print('11. contact number :')
        print('12. E-mail address : ')
        print('13. disease name : ')
        print('14. doctors name : ')
        print('15. prescribed medicines : ')
        print('16. bill amount : ')
        print('17. payment method : ')
        print('18. ALL :')
        n = eval(input (': ....'))
        ModiHospital(m, n)
    elif ch == 13 :
        n = input('enter serial number to delete :')
        DelHospital(n)
    elif ch == 14 :
        print('EXITING')
        time.sleep(.8)
        print('.')
        time.sleep(.8)
        print('.')
        time.sleep(.8)
        print('.') 
        time.sleep(.8)
        print('.')
        time.sleep(.8)
        print('.')
        break
    else :
        print('Analysing your input. ')
        time.sleep(.6)
        print('.')
        time.sleep(.6)
        print('.')
        time.sleep(.6)
        print('.')
        time.sleep(.6)
        print('.')
        time.sleep(.6)
        print('.')
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~WRONG CHOICE ~~~~~~~~~~~~~~~~~~~\n\n\n")
