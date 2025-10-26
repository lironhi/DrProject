from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from DrProjectApp.models import new_Patient
from DrProjectApp.models import doctor_identification
from django.contrib import messages
import mysql.connector

# Create your views here.

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="drproject"
)
cursor = db_connection.cursor()
print(db_connection)

# START PAGE WITH ANIMATION
def login(request):
    return render(request,'login.html')
def newanalyze(request):
    return render(request,'newanalyze.html')
def home(request):
    return render(request,'home.html')
#--------------------------------------------------------------------#   



#----------------------------USERS FUNCTIONS (REGISTRATIONS, ADD ,SUPP ) ! ---------------------------#

def login_dr(request):
    result = []
    cursor.execute("SELECT * FROM `drproject_auth`")
    data = cursor.fetchall() 
    if request.method =='POST':
         logintest=request.POST.get('login')
         passwordtest=request.POST.get('password')
         idnumbertest=request.POST.get('idnumber')
    for item in data:
        id, login, password, idnumber, type, checktype = item
        if logintest == login and passwordtest == password and idnumbertest == idnumber:
             return home(request)
        else :
            messages.error(request,'הפרטים שהוזנו לא נמצאים במערכת')   
            return login(request) 

def registration_new_patient(request): 
    if request.method=='POST':
        saverecord=new_Patient()
        saverecord.firstname=request.POST.get('firstname')
        saverecord.lastname=request.POST.get('lastname')
        saverecord.age=request.POST.get('age')
        saverecord.gender=request.POST.get('gender')
        saverecord.idnum=request.POST.get('idnum')
        saverecord.wbc=request.POST.get('wbc')
        saverecord.neut=request.POST.get('neut')
        saverecord.lymph=request.POST.get('lymph')
        saverecord.rbc=request.POST.get('rbc')
        saverecord.hct=request.POST.get('hct')
        saverecord.urea=request.POST.get('urea')
        saverecord.hb=request.POST.get('hb')
        saverecord.creatin=request.POST.get('creatin')
        saverecord.iron=request.POST.get('iron')
        saverecord.hdl=request.POST.get('hdl')
        saverecord.alkaph=request.POST.get('alkaph')
        saverecord.smocker=request.POST.get('smocker')
        saverecord.fever=request.POST.get('fever')
        saverecord.vomiting=request.POST.get('vomiting')
        saverecord.diarrhea=request.POST.get('diarrhea')
        saverecord.medic=request.POST.get('medic')
        saverecord.diet=request.POST.get('diet')
        saverecord.sport=request.POST.get('sport')
        saverecord.pregnant=request.POST.get('pregnant')
        saverecord.save()
        messages.success(request,'! הנתונים נקלטו בהצלחה')
        return newanalyze(request)
    else:
        return newanalyze(request)



#----------------------------Txt Creator ---------------------------#

def txtcreator(request):
    if request.method=='POST':
        firstnametxt=request.POST.get('firstname') # no calc
        lastnametxt=request.POST.get('lastname') # no calc
        agetxt=request.POST.get('age')
        gendertxt=request.POST.get('gender')
        idnumtxt=request.POST.get('idnum') # no calc
        wbctxt=request.POST.get('wbc')
        neuttxt=request.POST.get('neut')
        lymphtxt=request.POST.get('lymph')
        rbctxt=request.POST.get('rbc')
        hcttxt=request.POST.get('hct')
        ureatxt=request.POST.get('urea')
        hbtxt=request.POST.get('hb')
        creatintxt=request.POST.get('creatin')
        irontxt=request.POST.get('iron')
        hdltxt=request.POST.get('hdl')
        alkaphtxt=request.POST.get('alkaph')
        smockertxt=request.POST.get('smocker')
        fevertxt=request.POST.get('fever')
        vomitingtxt=request.POST.get('vomiting')
        diarrheatxt=request.POST.get('diarrhea')
        medictxt=request.POST.get('medic')
        diettxt=request.POST.get('diet')
        sporttxt=request.POST.get('sport')
        pregnanttxt=request.POST.get('pregnant')

        stats = []
        help = []
        first = ['Name:' + firstnametxt + ', ' + lastnametxt, 'Age: ' + agetxt, 'Gender: ' + gendertxt, 'Questions:',  'Smocker: ' + smockertxt, 'Fever: ' + fevertxt, 'Vomoting: ' + vomitingtxt, 'Diarrhea: ' + diarrheatxt, 'Medicament: ' + medictxt, 'Diet: ' + diettxt, 'Sport: ' + sporttxt, 'Pregnancy: ' + pregnanttxt ]
        with open('result.txt', 'w+') as f:
            f.write('\n'.join(first))
        

        if int(agetxt) <= 3:
            if int(wbctxt) < 6000:
                stats[0] = 'Wbc : LOW'
            elif int(wbctxt) > 17500:
                stats[0] = 'Wbc : HIGH'
            else: stats[0] = 'Wbc : OK'
        elif int(agetxt) <= 17 and int(agetxt) >= 4:
            if int(wbctxt) < 5500:
                stats[0] = 'Wbc : LOW'
            elif int(wbctxt) > 15500:
                stats[0] = 'Wbc : HIGH'
            else: stats[0] = 'Wbc : OK'
        elif int(agetxt) >= 18:
            if int(wbctxt) < 4500:
                stats[0] = 'Wbc : LOW'
            elif int(wbctxt) > 11000:
                stats[0] = 'Wbc : HIGH'
            else: stats[0] = 'Wbc : OK'
        else : stats[0] = 'Wbc : OK'

        if int(neuttxt) < 28:
            stats[1] = 'Neut : LOW'
        elif int(neuttxt) > 54:
            stats[1] = 'Neut : HIGH'
        else: stats[1] = 'Neut : OK'

        if int(lymphtxt) < 36:
            stats[2] = 'Lymph : LOW'
        elif int(lymphtxt) > 52:
            stats[2] = 'Lymph : HIGH'
        else: stats[2] = 'Lymph : OK'

        if float(rbctxt) < 4.5:
            stats[3] = 'RBC : LOW'
        elif float(rbctxt) > 6:
            stats[3] = 'RBC : HIGH'
        else: stats[3] = 'RBC : OK'

        if gendertxt == 'זכר':
            if int(hcttxt) < 37:
                stats[4] = 'Hct : LOW'
            elif int(hcttxt) > 54:
                stats[4] = 'Hct : HIGH'
            else: stats[4] = 'Hct : OK'
        elif gendertxt == 'נקבה':
            if int(hcttxt) < 33:
                stats[4] = 'Hct : LOW'
            elif int(hcttxt) > 43:
                stats[4] = 'Hct : HIGH'
            else: stats[4] = 'Hct : OK'
        else : stats[4] = 'Hct : OK'

        if int(ureatxt) < 17:
            stats[5] = 'Urea : LOW'
        elif int(ureatxt) > 43:
            stats[5] = 'Urea : HIGH'
        else: stats[5] = 'Urea : OK'

        if gendertxt == 'זכר':
            if int(agetxt) <= 17:
                if float(hbtxt) < 11.5:
                    stats[6] = 'Hb : LOW'
                elif float(hbtxt) > 18:
                    stats[6] = 'Hb : HIGH'
                else: stats[6] = 'Hb : OK'
            elif int(hbtxt) < 12:
                stats[6] = 'Hb : LOW'
            elif int(hbtxt) > 18:
                stats[6] = 'Hb : HIGH'
            else: stats[6] = 'Hb : OK'
        elif gendertxt == 'נקבה':
            if int(agetxt) <= 17:
                if float(hbtxt) < 11.5:
                    stats[6] = 'Hb : LOW'
                elif float(hbtxt) > 18:
                    stats[6] = 'Hb : HIGH'
                else: stats[6] = 'Hb : OK'
            elif int(hbtxt) < 12:
                stats[6] = 'Hb : LOW'
            elif int(hbtxt) > 16:
                stats[6] = 'Hb : HIGH'
            else: stats[6] = 'Hb : OK'
        else : stats[6] = 'Hb : OK'

        if int(agetxt) <= 2:
            if float(creatintxt) < 0.2:
                stats[7] = 'Creatinine : LOW'
            elif float(creatintxt) > 0.5:
                stats[7] = 'Creatinine : HIGH'
            else: stats[7] = 'Creatinine : OK'
        elif int(agetxt) <= 17 and int(agetxt) >= 3:
            if float(creatintxt) < 0.5:
                stats[7] = 'Creatinine : LOW'
            elif float(creatintxt) > 1:
                stats[7] = 'Creatinine : HIGH'
            else: stats[7] = 'Creatinine : OK'
        elif int(agetxt) <= 17 and int(agetxt) >= 3:
            if float(creatintxt) < 0.6:
                stats[7] = 'Creatinine : LOW'
            elif float(creatintxt) > 1:
                stats[7] = 'Creatinine : HIGH'
            else: stats[7] = 'Creatinine : OK'
        elif int(agetxt) >= 60:
            if float(creatintxt) < 0.6:
                stats[7] = 'Creatinine : LOW'
            elif float(creatintxt) > 1.2:
                stats[7] = 'Creatinine : HIGH'
            else: stats[7] = 'Creatinine : OK'
        else : stats[7] = 'Creatinine : OK'

        if int(irontxt) < 60:
            stats[8] = 'Iron : LOW'
        elif int(irontxt) > 160:
            stats[8] = 'Iron : HIGH'
        else: stats[8] = 'Iron : OK'

        if gendertxt == 'זכר':
            if int(hdltxt) < 29:
                stats[9] = 'Hdl : LOW'
            elif int(hdltxt) > 62:
                stats[9] = 'Hdl : HIGH'
            else: stats[9] = 'Hdl : OK'
        elif gendertxt == 'נקבה':
            if int(hdltxt) < 34:
                stats[9] = 'Hdl : LOW'
            elif int(hdltxt) > 82:
                stats[9] = 'Hdl : HIGH'
            else: stats[9] = 'Hdl : OK'
        else : stats[9] = 'Hdl : OK'

        if int(alkaphtxt) < 30:
            stats[10] = 'AlkalinePh. : LOW'
        elif int(alkaphtxt) > 120:
            stats[10] = 'AlkalinePh. : HIGH'
        else: stats[10] = 'AlkalinePh. : OK'

        for i in range(11):
            with open('result.txt', 'a') as f:
                f.writelines('\n'.join(stats[i-1]))
        j = 0
        if stats[3] == 'RBC : LOW' and stats[4] == 'Hct : LOW' and stats[6] == 'Hb : LOW':
            help[j] = 'Anemia : 2 pills B12 10mg per day during a month.'
            j+=1
        if stats[5] is not 'Urea : OK' :
            help[j] = 'Diet : Look for Nutrisionist'
            j+=1
        if stats[3] == 'RBC : LOW' or stats[4] == 'Hct : LOW' and stats[6] == 'Hb : LOW' and stats[8] == 'Iron : LOW':
            help[j] = 'Bleeding : Go to Hospital'
            j+=1
        if stats[9] == 'Hdl : LOW':
            help[j] = 'Hyperlipidemia, Heart disease and  Adult diabetes:  Arrange an appointment with a nutritionist, a 5 kg pill of Simovil per day for a week, coordinate an appointment with a nutritionist, adjust insulin for the patient'
            j+=1
        if stats[1] == 'Neut : LOW' and stats[2] == 'Lymph : HIGH' and stats[3] == 'RBC : HIGH':
            help[j] = 'Interference in the formation of blood / blood cells : Pill 10 kg of B12 per day for 1 month 5 kg ball of folic acid per day for 1 month'
            j+=1
        if stats[6] == 'Hb : LOW':
            help[j] = 'Hematological disorder, iron deficiency : Two 10-12-day B12 pills per month, an injection of a hormone to encourage red blood cell production'
            j+=1
        if stats[8] == 'Iron : HIGH':
            help[j] = 'Iron poisoning :  evacuate to the hospital'
            j+=1
        if stats[5] == 'Urea : HIGH':
            help[j] = 'Dehydration : complete rest lying down, returning fluids in drinking'
            j+=1
        if stats[5] is not 'Urea : OK' and stats[2] == 'Lymph : LOW' and fevertxt == 'כן':
            help[j] = 'Infection , Cancer : Antarctica - Dedicated Antibiotic E'
            j+=1
        if stats[10] == 'AlkalinePh. : LOW' :
            help[j] = 'Vitamin deficiency referral to blood test to identify missing vitamins'
            j+=1
        if stats[0] == 'Wbc : LOW' :
            help[j] = 'DViral disease to rest at home'
            j+=1
        if stats[10] == 'AlkalinePh. : HIGH' :
            help[j] = 'Biliary diseases, hyperthyroidism, use of various medications : referral to the family doctor for the purpose of checking for a match between the drugs Propylthiouracil to reduce thyroid activity, referral for surgical treatment'
            j+=1
        if stats[0] == 'Wbc : HIGH' :
            help[j] = 'Blood disease : A combination of cyclophospamide and corticocorids'
            j+=1
        if stats[5] == 'Urea : HIGH' and stats[7] == 'Urea : HIGH' :
            help[j] = 'Kidney disease : balances blood sugar levels'
            j+=1
        if stats[7] is not 'Creatinine : OK' :
            help[j] = 'Muscle diseases : two pellets 5 g of Altman s c3 turmeric per day for a month'
            j+=1
        if stats[3] == 'RBC : HIGH' :
            help[j] = 'Lung disease stop smoking / referral for an X-ray of the lungs'
            j+=1
        if stats[7] == 'Creatinine : HIGH' :
            help[j] = 'Increased consumption of meat to coordinate an appointment with a nutritionist'
            j+=1
        if stats[5] == 'Urea : LOW' and stats[5] == 'Urea : LOW' or pregnanttxt == 'כן':
            help[j] = 'Malnutrition to coordinate meeting with a nutritionist'
            j+=1
        
        for i in range(j+1):
            with open('result.txt', 'a') as f:
                f.writelines('\n'.join(help[i]))

        messages.success(request,'Txt OK')
        

