from django.shortcuts import render
from django.http import HttpResponse
from .models import HostelData3
from .models import HostelData2
from .models import HostelData1
from .models import Lists
import datetime
import re
from django.conf import settings
import os
from email.message import EmailMessage
import ssl
import smtplib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.core.files.storage import FileSystemStorage
from io import BytesIO

file_path = os.path.join(settings.BASE_DIR, 'Hostel_Addmission\\templates\\ext_file\\close.txt')
file_path2 = os.path.join(settings.BASE_DIR, 'Hostel_Addmission\\templates\\ext_file\\impdates.txt')
file_path3 = os.path.join(settings.BASE_DIR, 'Hostel_Addmission\\templates\\ext_file\\close2.txt')
file_path4 = os.path.join(settings.BASE_DIR, 'Hostel_Addmission\\templates\\ext_file\\close1.txt')
file_path5 = os.path.join(settings.BASE_DIR, 'Hostel_Addmission\\templates\\ext_file\\list.txt')

def home(request):
    return render(request , 'Home/index.html' )

def Hostellook(request):
    return render(request , 'Home/previewtab.html' )

def important_dates(request):
    with open(file_path2, 'r') as file:
        lines = file.readlines()
    print("lines", lines)
    p3 = lines[0]
    f3 = lines[1]
    ED = lines[2]
    SD = lines[3]
    acc = lines[13].strip()  
    if acc == "ON":
        return render(request, 'studates/dates.html', {'p3': p3, 'f3': f3 ,'ED': ED, 'SD': SD})
    else:
        return HttpResponse('Link Disabled For Now')


def important_dates2(request):
    with open(file_path2, 'r') as file:
        lines = file.readlines()
    p3 = lines[4]
    f3 = lines[5]
    ED = lines[6]
    SD = lines[7]
    acc = lines[14].strip()  
    if acc == "ON":
        return render(request, 'studates/date2.html', {'p3': p3, 'f3': f3 ,'ED': ED, 'SD': SD})
    else:
        return HttpResponse('Link Disabled For Now')

def important_dates1(request):
    with open(file_path2, 'r') as file:
        lines = file.readlines()
    p3 = lines[8]
    f3 = lines[9]
    ED = lines[10]
    SD = lines[11]
    acc = lines[15].strip()  
    if acc == "ON":
        return render(request, 'studates/dates1.html', {'p3': p3, 'f3': f3 ,'ED': ED, 'SD': SD})
    else:
        return HttpResponse('Link Disabled For Now')

def close_impdates3(request):
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
        if decide == 'OFF':
            with open(file_path2, 'r+') as file:
                lines = file.readlines()
                lines[13] = "OFF\n"
                file.seek(0)
                file.writelines(lines)
        if decide == 'ON':
            with open(file_path2, 'r+') as file:
                lines = file.readlines()
                lines[13] = "ON\n"
                file.seek(0)
                file.writelines(lines)
    return render(request , 'Admin_OP\closeimdates.html\cimp3.html')

def close_impdates2(request):
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
        if decide == 'OFF':
            with open(file_path2, 'r+') as file:
                lines = file.readlines()
                lines[14] = "OFF\n"
                file.seek(0)
                file.writelines(lines)
        if decide == 'ON':
            with open(file_path2, 'r+') as file:
                lines = file.readlines()
                lines[14] = "ON\n"
                file.seek(0)
                file.writelines(lines)
    return render(request , 'Admin_OP\closeimdates.html\cimp2.html')

def close_impdates1(request):
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
        if decide == 'OFF':
            with open(file_path2, 'r+') as file:
                lines = file.readlines()
                lines[15] = "OFF\n"
                file.seek(0)
                file.writelines(lines)
        if decide == 'ON':
            with open(file_path2, 'r+') as file:
                lines = file.readlines()
                lines[15] = "ON\n"
                file.seek(0)
                file.writelines(lines)
    return render(request , 'Admin_OP\closeimdates.html\cimp1.html')

def closeplist(request):
    decide = None
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
    if decide == 'ON':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[0] = 'ON\n'
            file.seek(0)
            file.writelines(lines)
    if decide == 'OFF':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[0] = 'OFF\n'
            file.seek(0)
            file.writelines(lines)
    return render(request , 'Admin_OP/closeimdates.html/plist3.html')    

def closeflist(request):
    decide = None
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
    if decide == 'ON':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[1] = 'ON\n'
            file.seek(0)
            file.writelines(lines)
    if decide == 'OFF':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[1] = 'OFF\n'
            file.seek(0)
            file.writelines(lines)
    return render(request , 'Admin_OP/closeimdates.html/flist3.html')    

def closeplist2(request):
    decide = None
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
    if decide == 'ON':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[2] = 'ON\n'
            file.seek(0)
            file.writelines(lines)
    if decide == 'OFF':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[2] = 'OFF\n'
            file.seek(0)
            file.writelines(lines)
    return render(request , 'Admin_OP/closeimdates.html/plist2.html')    

def closeflist2(request):
    decide = None
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
    if decide == 'ON':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[3] = 'ON\n'
            file.seek(0)
            file.writelines(lines)
    if decide == 'OFF':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[3] = 'OFF\n'
            file.seek(0)
            file.writelines(lines)
    return render(request , 'Admin_OP/closeimdates.html/flist2.html')    


def closeplist1(request):
    decide = None
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
    if decide == 'ON':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[4] = 'ON\n'
            file.seek(0)
            file.writelines(lines)
    if decide == 'OFF':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[4] = 'OFF\n'
            file.seek(0)
            file.writelines(lines)
    return render(request , 'Admin_OP/closeimdates.html/plist1.html')    

def closeflist1(request):
    decide = None
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
    if decide == 'ON':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[5] = 'ON'
            file.seek(0)
            file.writelines(lines)
    if decide == 'OFF':
        with open(file_path5 , 'r+') as file:
            lines = file.readlines()
            lines[5] = 'OF'
            file.seek(0)
            file.writelines(lines)
    return render(request, 'Admin_OP/closeimdates.html/flist1.html')

def plistshow(request):
    with open(file_path5 , 'r') as file:
        lines = file.readlines()
    if lines[0] == 'ON\n':
        data = Lists.objects.all()
        return render(request , 'studates/lists_show.html',{'data':data})
    else:
        return HttpResponse(' Link Disabled By Admin ')
def flistshow(request):
    with open(file_path5 , 'r') as file:
        lines = file.readlines()
    if lines[1] == 'ON\n':
        data = Lists.objects.all()
        return render(request , 'studates/list_show2.html',{'data':data})
    else:
        return HttpResponse(' Link Disabled By Admin ')

def plistshow22(request):
    with open(file_path5 , 'r') as file:
        lines = file.readlines()
    if lines[2] == 'ON\n':
        data = Lists.objects.all()
        return render(request , 'studates/listyear2.html',{'data':data})
    else:
        return HttpResponse(' Link Disabled By Admin ')
    
def flistshow22(request):
    with open(file_path5 , 'r') as file:
        lines = file.readlines()
    if lines[3] == 'ON\n':
        data = Lists.objects.all()
        return render(request , 'studates/listyears2.html',{'data':data})
    else:
        return HttpResponse(' Link Disabled By Admin ')
    
def plistshow11(request):
    with open(file_path5 , 'r') as file:
        lines = file.readlines()
    if lines[4] == 'ON\n':
        data = Lists.objects.all()
        return render(request , 'studates/listyear1.html',{'data':data})
    else:
        return HttpResponse(' Link Disabled By Admin ')
def flistshow11(request):
    with open(file_path5 , 'r') as file:
        lines = file.readlines()
    if lines[5] == 'ON':
        data = Lists.objects.all()
        return render(request , 'studates/listyears1.html',{'data':data})
    else:
        return HttpResponse(' Link Disabled By Admin ')


    
def plistUP(request):
    s = Lists.objects.get(k=101010)
    if request.method == 'POST':
        p3 = request.FILES.get('p3')
        if p3:
            s.p3 = p3
        s.save()            
    return render(request , 'Admin_OP/lists/plist.html')


def plistUP2(request):
    s = Lists.objects.get(k=101010)
    if request.method == 'POST':
        p2 = request.FILES.get('p2')
        if p2:
            s.p2 = p2
        s.save()            
    return render(request , 'Admin_OP/lists/plist2.html')


def plistUP1(request):
    s = Lists.objects.get(k=101010)
    if request.method == 'POST':
        p1 = request.FILES.get('p1')
        if p1:
            s.p1 = p1
        s.save()            
    return render(request , 'Admin_OP/lists/plist1.html')


def flistUP(request):
    s = Lists.objects.get(k=101010)
    if request.method == 'POST':
        f3 = request.FILES.get('f3')
        if f3:
            s.f3 = f3 
        s.save()      
    return render(request , 'Admin_OP/lists/flist.html')

def flistUP2(request):
    s = Lists.objects.get(k=101010)
    if request.method == 'POST':
        f2 = request.FILES.get('f2')
        if f2:
            s.f2 = f2
        s.save()      
    return render(request , 'Admin_OP/lists/flist2.html')

def flistUP1(request):
    s = Lists.objects.get(k=101010)
    if request.method == 'POST':
        f1 = request.FILES.get('f1')
        if f1:
            s.f1 = f1  
        s.save()      
    return render(request , 'Admin_OP/lists/flist1.html')

def up_date(request):
    if request.method == 'POST':
        p3 = str(request.POST['p3'])
        f3 = str(request.POST['f3'])
        ED = str(request.POST['ED'])
        SD = str(request.POST['SD'])
        with open(file_path2, 'r+') as file:
            lines = file.readlines()
            lines[0] = p3+"\n"
            lines[1] = f3+"\n"
            lines[2] = ED+"\n"
            lines[3] = SD+"\n"
            file.seek(0)
            file.writelines(lines)
    return render(request,'Admin_OP/dateChange/date.html')

def up_date2(request):
    SD = 0
    if request.method == 'POST':
        p3 = str(request.POST['p3'])
        f3 = str(request.POST['f3'])
        ED = str(request.POST['ED'])
        SD = str(request.POST['SD'])
        with open(file_path2, 'r+') as file:
            lines = file.readlines()
            lines[4] = p3+"\n"
            lines[5] = f3+"\n"
            lines[6] = ED+"\n"
            lines[7] = SD+"\n"
            file.seek(0)
            file.writelines(lines)
    return render(request,'Admin_OP/dateChange/date2.html')

def up_date1(request):
    if request.method == 'POST':
        p3 = str(request.POST['p3'])
        f3 = str(request.POST['f3'])
        ED = str(request.POST['ED'])
        SD = str(request.POST['SD'])
        print(SD)
        with open(file_path2, 'r+') as file:
            lines = file.readlines()
            lines[8] = p3+"\n"
            lines[9] = f3+"\n"
            lines[10] = ED+"\n"
            lines[11] = SD+"\n"
            file.seek(0)
            file.writelines(lines)
    return render(request,'Admin_OP/dateChange/date1.html')

def First_year(request):
    
    with open(file_path3 , 'r') as file:
        current_value = file.read()
        print(current_value,type(current_value))
    if current_value == 'ON':
        if request.method == "POST":

            name = request.POST['name']
            Bdate = request.POST['DOB']
            cast = request.POST['cast']
            nationality = request.POST['nation']
            Bgroup = request.POST['Bgroup']
            number = request.POST['Number']
            address = request.POST['add']
            email = request.POST['email']
            branch = request.POST['Branch']
            obtain1 = int(request.POST['Obtained1']) 
            total1 = int(request.POST['Total1'])     

            if total1 <= 0 :
                return HttpResponse("Total marks should be greater than 0.")
            
            obtain = obtain1
            total = total1

            per = (obtain / total) * 100

            fname = request.POST['fname']
            fphone = request.POST['fPhone']
            faddress = request.POST['fAddress']

            Signature = request.FILES.get('Signature')
            fSignature = request.FILES.get('fSignature')
            marksheet2 = request.FILES.get('Marksheet2')
            allotment = request.FILES.get('Allotment')
            domacile = request.FILES.get('Domacile')
            addmission = request.FILES.get('Addmission')
            registration = request.FILES.get('Registration')

            try:
                Bdate = datetime.datetime.strptime(Bdate, '%Y-%m-%d').date()
            except ValueError:
                return HttpResponse("Invalid birthdate format.")

            if not re.fullmatch("[7-9][0-9]{9}",number):
                return HttpResponse("Invalid phone number format.")

            if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                return HttpResponse("Invalid email format.")

            if not re.fullmatch("[7-9][0-9]{9}",number):
                return HttpResponse("Invalid father's phone number format.")
            
            data = HostelData1.objects.all()
            for i in data:
                if i.Email == email or i.phone1 == number:
                    return HttpResponse("This student already exists!")
            count = 1
            for i in data:
                 count += 1

            h = HostelData1()
            h.fno1 = "2310" + str(count)
            h.name = name
            h.DOB = Bdate
            h.cast = cast
            h.nationality = nationality 
            h.BGroup = Bgroup
            h.phone1 = number
            h.Address1 = address
            h.Email = email
            h.Branch = branch
            h.percentage = per

            h.Father_name = fname
            h.phone2 = fphone
            h.Address2 = faddress

            if Signature:
                h.student_signature = Signature
            if fSignature:
                h.father_signature = fSignature
            if marksheet2:
                h.marksheet = marksheet2
            if allotment:
                h.Allotment = allotment
            if domacile:
                h.Domacile = domacile
            if addmission:
                h.Addmission = addmission
            if registration:
                h.Registration = registration
            
            request.session['fno1'] = h.fno1
            h.save()
            em = EmailMessage()
            email_receiver=h.Email  
            email_sender="satwikbot3@gmail.com"
            email_password="uzuzkugblnquthir"
            subject = " Government Polytechnic Nagpur "
            body = f" {h.name} Your Application Submitted Succesfully Your Application ID {h.fno1} "
            em['FROM']=email_sender
            em['To']=email_receiver
            em['Subject']=subject
            em.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver,em.as_string())
            return render(request , '1year/index.html' , {'msg':' Successfully '})

        return render(request , '1year/index.html')
    else:
        return HttpResponse(' Form Disabled For Now ')

def Second_year(request):
    with open(file_path4 , 'r') as file:
        current_value = file.read()
        print(current_value,type(current_value))
    if current_value == 'ON':
        if request.method == "POST":
            name = request.POST['name']
            Bdate = request.POST['DOB']
            cast = request.POST['cast']
            nationality = request.POST['nation']
            Bgroup = request.POST['Bgroup']
            number = request.POST['Number']
            address = request.POST['add']
            email = request.POST['email']
            branch = request.POST['Branch']
            backlog = request.POST['Backlog']
            noBack = request.POST['noBack']
            obtain1 = int(request.POST['Obtained1']) 
            total1 = int(request.POST['Total1'])      
            obtain2 = int(request.POST['Obtained2']) 
            total2 = int(request.POST['Total2'])      

            if total1 <= 0 or total2 <= 0:
                return HttpResponse("Total marks should be greater than 0.")
            
            obtain = obtain1 + obtain2
            total = total1 + total2

            if total <= 0:
                return HttpResponse("Total marks should be greater than 0.")
            per = (obtain / total) * 100

            fname = request.POST['fname']
            fphone = request.POST['fPhone']
            faddress = request.POST['fAddress']

            Signature = request.FILES.get('Signature')
            fSignature = request.FILES.get('fSignature')
            Marksheet1 = request.FILES.get('Marksheet1')
            marksheet2 = request.FILES.get('Marksheet2')
            allotment = request.FILES.get('Allotment')
            domacile = request.FILES.get('Domacile')
            addmission = request.FILES.get('Addmission')
            registration = request.FILES.get('Registration')

            try:
                Bdate = datetime.datetime.strptime(Bdate, '%Y-%m-%d').date()
            except ValueError:
                return HttpResponse("Invalid birthdate format.")

            if not re.fullmatch("[7-9][0-9]{9}",number):
                return HttpResponse("Invalid phone number format.")

            if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                return HttpResponse("Invalid email format.")

            if not re.fullmatch("[7-9][0-9]{9}",number):
                return HttpResponse("Invalid father's phone number format.")
            
            data = HostelData2.objects.all()
            for i in data:
                if i.Email == email or i.phone1 == number:
                    return HttpResponse("This student already exists!")
            count = 1
            for i in data:
                 count += 1

            h = HostelData2()
            h.fno2 = '2320'+str(count)
            h.name = name
            h.DOB = Bdate
            h.cast = cast
            h.nationality = nationality 
            h.BGroup = Bgroup
            h.phone1 = number
            h.Address1 = address
            h.Email = email
            h.Branch = branch
            h.Backlog = backlog
            h.Nu_Backlog = noBack
            h.percentage = per

            h.Father_name = fname
            h.phone2 = fphone
            h.Address2 = faddress

            if Signature:
                h.student_signature = Signature
            if fSignature:
                h.father_signature = fSignature
            if Marksheet1:
                h.marksheet1 = Marksheet1
            if marksheet2:
                h.marksheet2 = marksheet2
            if allotment:
                h.Allotment = allotment
            if domacile:
                h.Domacile = domacile
            if addmission:
                h.Addmission = addmission
            if registration:
                h.Registration = registration

            request.session['fno2'] = h.fno2
            h.save()
            em = EmailMessage()
            email_receiver=h.Email  
            email_sender="satwikbot3@gmail.com"
            email_password="uzuzkugblnquthir"
            subject = " Government Polytechnic Nagpur "
            body = f" {h.name} Your Application Submitted Succesfully Your Application ID {h.fno2} "
            em['FROM']=email_sender
            em['To']=email_receiver
            em['Subject']=subject
            em.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver,em.as_string())
            return render(request , '2year/index.html' , {'msg':' Successfully '})

        return render(request , '2year/index.html')
    else:
        return HttpResponse('Form Disabled For Now')

def Second_year_mining(request):
    with open(file_path4 , 'r') as file:
        current_value = file.read()
    if current_value == 'ON':
        if request.method == "POST":
            name = request.POST['name']
            Bdate = request.POST['DOB']
            cast = request.POST['cast']
            nationality = request.POST['nation']
            Bgroup = request.POST['Bgroup']
            number = request.POST['Number']
            address = request.POST['add']
            email = request.POST['email']
            branch = request.POST['Branch']
            backlog = request.POST['Backlog']
            noBack = request.POST['noBack']
            obtain1 = int(request.POST['Obtained1']) 
            total1 = int(request.POST['Total1'])       

            if total1 <= 0:
                return HttpResponse("Total marks should be greater than 0.")
           
            per = (obtain1 / total1) * 100

            fname = request.POST['fname']
            fphone = request.POST['fPhone']
            faddress = request.POST['fAddress']

            Signature = request.FILES.get('Signature')
            fSignature = request.FILES.get('fSignature')
            Marksheet1 = request.FILES.get('Marksheet1')
            allotment = request.FILES.get('Allotment')
            domacile = request.FILES.get('Domacile')
            addmission = request.FILES.get('Addmission')
            registration = request.FILES.get('Registration')

            try:
                Bdate = datetime.datetime.strptime(Bdate, '%Y-%m-%d').date()
            except ValueError:
                return HttpResponse("Invalid birthdate format.")

            if not re.fullmatch("[7-9][0-9]{9}",number):
                return HttpResponse("Invalid phone number format.")

            if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                return HttpResponse("Invalid email format.")

            if not re.fullmatch("[7-9][0-9]{9}",number):
                return HttpResponse("Invalid father's phone number format.")

            data = HostelData2.objects.all()
            for i in data:
                if i.Email == email or i.phone1 == number:
                    return HttpResponse("This student already exists!")
            count = 1
            for i in data:
                 count += 1

            h = HostelData2()
            h.fno2 = '2320'+str(count)
            h.name = name
            h.DOB = Bdate
            h.cast = cast
            h.nationality = nationality 
            h.BGroup = Bgroup
            h.phone1 = number
            h.Address1 = address
            h.Email = email
            h.Branch = branch
            h.Backlog = backlog
            h.Nu_Backlog = noBack
            h.percentage = per

            h.Father_name = fname
            h.phone2 = fphone
            h.Address2 = faddress

            if Signature:
                h.student_signature = Signature
            if fSignature:
                h.father_signature = fSignature
            if Marksheet1:
                h.marksheet1 = Marksheet1
            if allotment:
                h.Allotment = allotment
            if domacile:
                h.Domacile = domacile
            if addmission:
                h.Addmission = addmission
            if registration:
                h.Registration = registration

            h.save()
            em = EmailMessage()
            email_receiver=h.Email  
            email_sender="satwikbot3@gmail.com"
            email_password="uzuzkugblnquthir"
            subject = " Government Polytechnic Nagpur "
            body = f" {h.name} Your Application Submitted Succesfully Your Application ID {h.fno2} "
            em['FROM']=email_sender
            em['To']=email_receiver
            em['Subject']=subject
            em.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver,em.as_string())
            return render(request , 'mining/year2.html' , {'msg':' Successfully '})

        return render(request , 'mining/year2.html')
    else:
        return HttpResponse('Form Disabled For Now')

def Third_year(request):
        with open(file_path , 'r') as file:
            current_value = file.read()
        if current_value == 'ON':
            fno3 = request.session.get('fno3')
            if fno3 :
                data = HostelData3.objects.get(fno3=fno3)
                if request.method == "POST":

                    name = request.POST['name']
                    Bdate = request.POST['DOB']
                    cast = request.POST['cast']
                    nationality = request.POST['nation']
                    Bgroup = request.POST['Bgroup']
                    number = request.POST['Number']
                    address = request.POST['add']
                    email = request.POST['email']
                    branch = request.POST['Branch']
                    backlog = request.POST['Backlog']
                                           
                    fname = request.POST['fname']
                    fphone = request.POST['fPhone']
                    faddress = request.POST['fAddress']

                    Signature = request.FILES.get('Signature')
                    fSignature = request.FILES.get('fSignature')
                    Marksheet1 = request.FILES.get('Marksheet1')
                    marksheet2 = request.FILES.get('Marksheet2')
                    allotment = request.FILES.get('Allotment')
                    domacile = request.FILES.get('Domacile')
                    addmission = request.FILES.get('Addmission')
                    registration = request.FILES.get('Registration')

                    try:
                        Bdate = datetime.datetime.strptime(Bdate, '%Y-%m-%d').date()
                    except ValueError:
                        return HttpResponse("Invalid birthdate format.")


                    if not re.fullmatch("[7-9][0-9]{9}",number):
                        return HttpResponse("Invalid phone number format.")

                    if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                        return HttpResponse("Invalid email format.")

                    if not re.fullmatch("[7-9][0-9]{9}",number):
                        return HttpResponse("Invalid father's phone number format.")
                    
                    data = HostelData3.objects.all()
                    for i in data:
                        if i.Email == email or i.phone1 == number:
                            return HttpResponse("This student already exists!")
                
                    data.fno3 = fno3
                    data.name = name
                    data.DOB = Bdate
                    data.cast = cast
                    data.nationality = nationality 
                    data.BGroup = Bgroup
                    data.phone1 = number
                    data.Address1 = address
                    data.Email = email
                    data.Branch = branch
                    data.Backlog = backlog
                    data.Father_name = fname
                    data.phone2 = fphone
                    data.Address2 = faddress

                    if Signature:
                        data.student_signature = Signature
                    if fSignature:
                        data.father_signature = fSignature
                    if Marksheet1:
                        data.marksheet1 = Marksheet1
                    if marksheet2:
                        data.marksheet2 = marksheet2
                    if allotment:
                        data.Allotment = allotment
                    if domacile:
                        data.Domacile = domacile
                    if addmission:
                        data.Addmission = addmission
                    if registration:
                        data.Registration = registration

                    request.session['fno3'] = data.fno3
                    data.save()
                return render(request , '3year/index2.html' , {'data':data})
        else:
            return HttpResponse('Form Disabled For Now')
    # ####################################################

        if current_value == 'ON':
            if request.method == "POST":

                name = request.POST['name']
                Bdate = request.POST['DOB']
                cast = request.POST['cast']
                nationality = request.POST['nation']
                Bgroup = request.POST['Bgroup']
                number = request.POST['Number']
                address = request.POST['add']
                email = request.POST['email']
                branch = request.POST['Branch']
                backlog = request.POST['Backlog']
                noBack = request.POST['noBack']
                obtain1 = int(request.POST['Obtained1'])
                total1 = int(request.POST['Total1'])
                obtain2 = int(request.POST['Obtained2'])
                total2 = int(request.POST['Total2'])
                    

                if total1 <= 0 or total2 <= 0:
                    return HttpResponse("Total marks should be greater than 0.")
                
                obtain = obtain1 + obtain2
                total = total1 + total2

                if total <= 0:
                    return HttpResponse("Total marks should be greater than 0.")
                per = (obtain / total) * 100

                fname = request.POST['fname']
                fphone = request.POST['fPhone']
                faddress = request.POST['fAddress']

                Signature = request.FILES.get('Signature')
                fSignature = request.FILES.get('fSignature')
                Marksheet1 = request.FILES.get('Marksheet1')
                marksheet2 = request.FILES.get('Marksheet2')
                allotment = request.FILES.get('Allotment')
                domacile = request.FILES.get('Domacile')
                addmission = request.FILES.get('Addmission')
                registration = request.FILES.get('Registration')

                try:
                    Bdate = datetime.datetime.strptime(Bdate, '%Y-%m-%d').date()
                except ValueError:
                    return HttpResponse("Invalid birthdate format.")


                if not re.fullmatch("[7-9][0-9]{9}",number):
                    return HttpResponse("Invalid phone number format.")

                if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                    return HttpResponse("Invalid email format.")

                if not re.fullmatch("[7-9][0-9]{9}",number):
                    return HttpResponse("Invalid father's phone number format.")

                data = HostelData3.objects.all()
                for i in data:
                    if i.Email == email or i.phone1 == number:
                        return HttpResponse("This student already exists!")
                count = 1
                for i in data:
                    count += 1

                h = HostelData3()
                h.fno3 = '2330'+str(count)
                h.name = name
                h.DOB = Bdate
                h.cast = cast
                h.nationality = nationality 
                h.BGroup = Bgroup
                h.phone1 = number
                h.Address1 = address
                h.Email = email
                h.Branch = branch
                h.percentage = per
                h.Backlog = backlog
                h.Nu_Backlog = noBack
                h.Father_name = fname
                h.phone2 = fphone
                h.Address2 = faddress

                if Signature:
                    h.student_signature = Signature
                if fSignature:
                    h.father_signature = fSignature
                if Marksheet1:
                    h.marksheet1 = Marksheet1
                if marksheet2:
                    h.marksheet2 = marksheet2
                if allotment:
                    h.Allotment = allotment
                if domacile:
                    h.Domacile = domacile
                if addmission:
                    h.Addmission = addmission
                if registration:
                    h.Registration = registration

                request.session['fno3'] = h.fno3
                h.save()
                em = EmailMessage()
                email_receiver=h.Email  
                email_sender="satwikbot3@gmail.com"
                email_password="uzuzkugblnquthir"
                subject = " Government Polytechnic Nagpur "
                body = f" {h.name} Your Application Submitted Succesfully Your Application ID {h.fno3} "
                em['FROM']=email_sender
                em['To']=email_receiver
                em['Subject']=subject
                em.set_content(body)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                    smtp.login(email_sender,email_password)
                    smtp.sendmail(email_sender,email_receiver,em.as_string())

                return render(request , '3year/index.html' , {'msg':' Successfully'})

            return render(request , '3year/index.html')
        else:
                return HttpResponse('Form Disabled For Now')

def Third_yearmining(request):
        with open(file_path , 'r') as file:
            current_value = file.read()
        if current_value == 'ON':
            if request.method == "POST":

                name = request.POST['name']
                Bdate = request.POST['DOB']
                cast = request.POST['cast']
                nationality = request.POST['nation']
                Bgroup = request.POST['Bgroup']
                number = request.POST['Number']
                address = request.POST['add']
                email = request.POST['email']
                branch = request.POST['Branch']
                backlog = request.POST['Backlog']
                NumberBack = request.POST['noBack']
                obtain1 = int(request.POST['Obtained1'])
                total1 = int(request.POST['Total1'])
                    

                if total1 <= 0 :
                    return HttpResponse("Total marks should be greater than 0.")
                
                per = (obtain1 / total1) * 100

                fname = request.POST['fname']
                fphone = request.POST['fPhone']
                faddress = request.POST['fAddress']

                Signature = request.FILES.get('Signature')
                fSignature = request.FILES.get('fSignature')
                Marksheet1 = request.FILES.get('Marksheet1')
                allotment = request.FILES.get('Allotment')
                domacile = request.FILES.get('Domacile')
                addmission = request.FILES.get('Addmission')
                registration = request.FILES.get('Registration')

                try:
                    Bdate = datetime.datetime.strptime(Bdate, '%Y-%m-%d').date()
                except ValueError:
                    return HttpResponse("Invalid birthdate format.")


                if not re.fullmatch("[7-9][0-9]{9}",number):
                    return HttpResponse("Invalid phone number format.")

                if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                    return HttpResponse("Invalid email format.")

                if not re.fullmatch("[7-9][0-9]{9}",number):
                    return HttpResponse("Invalid father's phone number format.")

                data = HostelData3.objects.all()
                for i in data:
                    if i.Email == email or i.phone1 == number:
                        return HttpResponse("This student already exists!")
                count = 1
                for i in data:
                    count += 1

                h = HostelData3()
                h.fno3 = '2330'+str(count)
                h.name = name
                h.DOB = Bdate
                h.cast = cast
                h.nationality = nationality 
                h.BGroup = Bgroup
                h.phone1 = number
                h.Address1 = address
                h.Email = email
                h.Branch = branch
                h.percentage = per
                h.Backlog = backlog
                h.Nu_Backlog = NumberBack
                h.Father_name = fname
                h.phone2 = fphone
                h.Address2 = faddress

                if Signature:
                    h.student_signature = Signature
                if fSignature:
                    h.father_signature = fSignature
                if Marksheet1:
                    h.marksheet1 = Marksheet1
                if allotment:
                    h.Allotment = allotment
                if domacile:
                    h.Domacile = domacile
                if addmission:
                    h.Addmission = addmission
                if registration:
                    h.Registration = registration

                request.session['fno3'] = h.fno3
                h.save()
                em = EmailMessage()
                email_receiver=h.Email  
                email_sender="satwikbot3@gmail.com"
                email_password="uzuzkugblnquthir"
                subject = " Government Polytechnic Nagpur "
                body = f" {h.name} Your Application Submitted Succesfully Your Application ID {h.fno3} "
                em['FROM']=email_sender
                em['To']=email_receiver
                em['Subject']=subject
                em.set_content(body)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                    smtp.login(email_sender,email_password)
                    smtp.sendmail(email_sender,email_receiver,em.as_string())

                return render(request , 'mining/year3.html' , {'msg':' Successfully '})
            return render(request , 'mining/year3.html')
        else:
                return HttpResponse('Form Disabled For Now')

def admin_log(request):
    msg = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if(username == 'gpnagpurHostel' and password == 'gpnagpur123'):
            msg = "Successfull"
            request.session['username'] = username
            request.session['password'] = password
            return render(request , 'Admin_OP/index.html')
        else:
            msg="Invalid Username or Password!"

    username = request.session.get('username')
    password = request.session.get('password')
    if username and password:
        return render(request , 'Admin_OP/index.html')
    return render(request , 'Admin_OP/login.html' ,{'msg':msg})

def close_Forms(request):
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
        if decide == 'OFF':
            with open(file_path, 'w') as file:
                file.write('OFF')
        if decide == 'ON':
            with open(file_path, 'w') as file:
                file.write('ON')
    return render(request , 'Admin_OP/closeform.html')

def close_Forms1(request):
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
        if decide == 'OFF':
            with open(file_path3, 'w') as file:
                file.write('OFF')
        if decide == 'ON':
            with open(file_path3, 'w') as file:
                file.write('ON')
    return render(request , 'Admin_OP/closeform1.html')

def close_Forms2(request):
    if request.method=="POST":
        decide  = str(request.POST['student_access'])
        if decide == 'OFF':
            with open(file_path4, 'w') as file:
                file.write('OFF')
        if decide == 'ON':
            with open(file_path4, 'w') as file:
                file.write('ON')
    return render(request , 'Admin_OP/closeform2.html')


def logout(request):
    request.session['username'] = None
    request.session['password'] = None
    return render(request , 'Admin_OP/login.html')

def Year3_report(request):
    data = HostelData3.objects.all()
    if request.method == 'POST':
        tseets = int(request.POST['Tseats'])
        OPENseets = int(request.POST['OPENseats'])
        OBCseets = int(request.POST['OBCseats'])
        SCseets = int(request.POST['SCseats'])
        STseets = int(request.POST['STseats'])
        NTseets = int(request.POST['NTseats'])
        SBCseets = int(request.POST['SBCseats'])
        sumseats = OPENseets+OBCseets+SCseets+STseets+NTseets+SBCseets
        if tseets != sumseats:
            return HttpResponse("Invalid Seats")
        backlog_YES_students = data.filter(Backlog='YES')
        backlog_NO_students = data.filter(Backlog='NO')
        available_seats = {
            'OBC': OBCseets,
            'SC': SCseets,
            'ST': STseets,
            'NT': NTseets,
            'SBC':SBCseets
        }
        Backlog_NO_students = sorted(backlog_NO_students ,key=lambda x:(-x.percentage))
        Backlog_Yes_students = sorted(backlog_YES_students ,key=lambda x:( x.Nu_Backlog , -x.percentage))
        openstudents = []
        count = 1
        open_student_seat = {}
        for i in range(OPENseets):
            student = Backlog_NO_students[i]
            seat = student.cast+'-'+'Alloted'
            open_student_seat[student.name] = seat
            openstudents.append(student.name)
            count += 1
        
        Allocated_students = []
        student_seat = {}
        for student in Backlog_NO_students:
            if student.name in openstudents:
                pass
            else:
                student_category = student.cast
                if available_seats.get(student_category,0) > 0:
                    seat = student.cast+'-'+'0'+str(available_seats[student_category])
                    student_seat[student.name] = seat
                    Allocated_students.append(student.name)
                    available_seats[student_category] -= 1
        return render(request , 'Admin_OP/Provisional/third_year.html',{
            'BACKLOG_YES':Backlog_Yes_students , 
            'BACKLOG_NO':Backlog_NO_students ,
            'Allocated_students':Allocated_students,
            'student_seat':student_seat,
            'openstudents':openstudents,
            'open_student_seat':open_student_seat
        })
    return render(request , 'Admin_OP/reports/year3.html',{'data':data} )

def Year2_report(request):
    data = HostelData2.objects.all()
    if request.method == 'POST':

        tseets = int(request.POST['Tseats'])
        OPENseets = int(request.POST['OPENseats'])
        OBCseets = int(request.POST['OBCseats'])
        SCseets = int(request.POST['SCseats'])
        STseets = int(request.POST['STseats'])
        NTseets = int(request.POST['NTseats'])
        SBCseets = int(request.POST['SBCseats'])
        sumseats = OPENseets+OBCseets+SCseets+STseets+NTseets+SBCseets
        if tseets != sumseats:
            return HttpResponse("Invalid Seats")
        backlog_YES_students = data.filter(Backlog='YES')
        backlog_NO_students = data.filter(Backlog='NO')
        available_seats = {
            'OBC': OBCseets,
            'SC': SCseets,
            'ST': STseets,
            'NT': NTseets,
            'SBC':SBCseets
        }
        Backlog_NO_students = sorted(backlog_NO_students ,key=lambda x:(-x.percentage))
        Backlog_Yes_students = sorted(backlog_YES_students ,key=lambda x:( x.Nu_Backlog , -x.percentage))
        openstudents = []
        count = 1
        open_student_seat = {}
        for i in range(OPENseets):
            student = Backlog_NO_students[i]
            seat = student.cast+'-'+'Alloted'
            open_student_seat[student.name] = seat
            openstudents.append(student.name)
            count += 1
        
        Allocated_students = []
        student_seat = {}
        for student in Backlog_NO_students:
            if student.name in openstudents:
                pass
            else:
                student_category = student.cast
                if available_seats.get(student_category,0) > 0:
                    seat = student.cast+'-'+'0'+str(available_seats[student_category])
                    student_seat[student.name] = seat
                    Allocated_students.append(student.name)
                    available_seats[student_category] -= 1
        return render(request , 'Admin_OP/Provisional/third_year.html',{
            'BACKLOG_YES':Backlog_Yes_students , 
            'BACKLOG_NO':Backlog_NO_students ,
            'Allocated_students':Allocated_students,
            'student_seat':student_seat,
            'openstudents':openstudents,
            'open_student_seat':open_student_seat
        })
    return render(request , 'Admin_OP/reports/year2.html',{'data':data} )


def Year1_report(request):
    data = HostelData1.objects.all()
    if request.method == 'POST':
        tseets = int(request.POST['Tseats'])
        OPENseets = int(request.POST['OPENseats'])
        OBCseets = int(request.POST['OBCseats'])
        SCseets = int(request.POST['SCseats'])
        STseets = int(request.POST['STseats'])
        NTseets = int(request.POST['NTseats'])
        SBCseets = int(request.POST['SBCseats'])
        sumseats = OPENseets+OBCseets+SCseets+STseets+NTseets+SBCseets
        if tseets != sumseats:
            return HttpResponse("Invalid Seats")
        backlog_YES_students = data.filter(Backlog='YES')
        backlog_NO_students = data.filter(Backlog='NO')
        available_seats = {
            'OBC': OBCseets,
            'SC': SCseets,
            'ST': STseets,
            'NT': NTseets,
            'SBC':SBCseets
        }
        Backlog_NO_students = sorted(backlog_NO_students ,key=lambda x:(-x.percentage))
        Backlog_Yes_students = sorted(backlog_YES_students ,key=lambda x:( x.Nu_Backlog , -x.percentage))
        openstudents = []
        count = 1
        open_student_seat = {}
        for i in range(OPENseets):
            student = Backlog_NO_students[i]
            seat = student.cast+'-'+'Alloted'
            open_student_seat[student.name] = seat
            openstudents.append(student.name)
            count += 1
        
        Allocated_students = []
        student_seat = {}
        for student in Backlog_NO_students:
            if student.name in openstudents:
                pass
            else:
                student_category = student.cast
                if available_seats.get(student_category,0) > 0:
                    seat = student.cast+'-'+'0'+str(available_seats[student_category])
                    student_seat[student.name] = seat
                    Allocated_students.append(student.name)
                    available_seats[student_category] -= 1
        return render(request , 'Admin_OP/Provisional/third_year.html',{
            'BACKLOG_YES':Backlog_Yes_students , 
            'BACKLOG_NO':Backlog_NO_students ,
            'Allocated_students':Allocated_students,
            'student_seat':student_seat,
            'openstudents':openstudents,
            'open_student_seat':open_student_seat
        })
    return render(request , 'Admin_OP/reports/year1.html',{'data':data})


def Provisional_list3(request):
    data = HostelData3.objects.all()
    data = sorted(data ,key=lambda x:(-x.percentage))
    return render(request , 'Admin_OP/Provisional1/third_year.html',{'data':data} )

def Provisional_list2(request):
    data = HostelData2.objects.all()
    data = sorted(data ,key=lambda x:(-x.percentage))
    return render(request , 'Admin_OP/Provisional1/second_year.html',{'data':data} )


def Provisional_list1(request):
    data = HostelData1.objects.all()
    data = sorted(data ,key=lambda x:(-x.percentage))
    return render(request , 'Admin_OP/Provisional1/first_year.html',{'data':data} )


def Search3(request):
    data1 = HostelData3.objects.all()

    data = sorted(data1 ,key=lambda x:(-x.percentage))
    name = ""
    if request.method == "POST":
        name = str(request.POST["search"])
    for i in data:
        if i.name == name or str(i.fno3) == name:
            i1 = i
            return render(request ,'Admin_OP/reports/search3.html' ,{'s':i1})
    return render(request , 'Admin_OP/search.html')


def Search2(request):
    data1 = HostelData2.objects.all()

    data = sorted(data1 ,key=lambda x:(-x.percentage))
    name = ""
    if request.method == "POST":
        name = str(request.POST["search"])
    for i in data:
        if i.name == name or str(i.fno2) == name:
            i1 = i
            return render(request ,'Admin_OP/reports/search2.html' ,{'s':i1})
    return render(request , 'Admin_OP/search2.html')


def Search1(request):
    data1 = HostelData1.objects.all()

    data = sorted(data1 ,key=lambda x:(-x.percentage))
    name = ""
    if request.method == "POST":
        name = str(request.POST["search"])
    for i in data:
        if i.name == name or str(i.fno1) == name:
            i1 = i
            return render(request ,'Admin_OP/reports/search1.html' ,{'s':i1})
    return render(request , 'Admin_OP/search1.html')


def admin_Preview3(request, fno3):
    s = HostelData3.objects.get(fno3=fno3)
    if request.method == "POST":
        remark = request.POST["remark"]
        s.remark = remark
        s.save()
    return render(request, 'Admin_OP/form_Preview/formview.html', {'s': s})


def admin_Preview2(request, fno2):
    s = HostelData2.objects.get(fno2=fno2)
    if request.method == "POST":
        remark = request.POST["remark"]
        s.remark = remark
        s.save()
    return render(request, 'Admin_OP/form_Preview/formview2.html', {'s': s})


def admin_Preview1(request, fno1):
    s = HostelData1.objects.get(fno1=fno1)
    if request.method == "POST":
        remark = request.POST["remark"]
        s.remark = remark
        s.save()
    return render(request, 'Admin_OP/form_Preview/formview1.html', {'s': s})


def student_Preview(request):
        fno3 = request.session.get('fno3')
        if fno3:
            s = HostelData3.objects.get(fno3=fno3)
            return render(request, '3year\studentview.html', {'s': s})
        else:
            return HttpResponse(" You Haven't Fill Form Yet ")    

def student_Preview2(request):
        fno2 = request.session.get('fno2')
        if fno2:
            s = HostelData2.objects.get(fno2=fno2)
            return render(request, '2year\studentview.html', {'s': s})
        else:
            return HttpResponse(" You Haven't Fill Form Yet ")
   
def student_Preview1(request):
        fno1 = request.session.get('fno1')
        if fno1:
            s = HostelData1.objects.get(fno1=fno1)
            return render(request, '1year\studentview.html', {'s': s})
        else:
            return HttpResponse(" You Haven't Fill Form Yet ")


def printform(request, fno3):
    s = HostelData3.objects.get(fno3=fno3)
    data = {
        'id': s.fno3,
        'Name': s.name,
        'Email': s.Email,
        'Branch':s.Branch,
        'DOB':s.DOB,
        'Caste':s.cast,
        'Nationality':s.nationality,
        'Blood Group':s.BGroup,
        'Phone No ':s.phone1,
        'Address': s.Address1,
        'Percentage':s.percentage,
        'Backlogs':s.Nu_Backlog,
        'Parents Name':s.Father_name,
        'Parents Phone':s.phone2,
        'parents Address':s.Address2
    }

    h1 = "Government Polytechnic Nagpur"
    h2 = "An Autonomous Institute of Government of Maharashtra"
    h3 = "Hostel Admission Form"

    pdf_filename = f"{s.fno3}_student_form.pdf"
    buffer = BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)  
    c.drawString(100, 770, h1)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, h2)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 730, h3)

    y = 700  

    for key, value in data.items():
        c.setFont("Helvetica", 12)  
        c.drawString(100, y, f'{key}: {value}')
        y -= 20

    c.showPage()
    c.save()

    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
    return response

def printform2(request, fno2):
    s = HostelData2.objects.get(fno2=fno2)
    data = {
        'id': s.fno2,
        'Name': s.name,
        'Email': s.Email,
        'Branch':s.Branch,
        'DOB':s.DOB,
        'Caste':s.cast,
        'Nationality':s.nationality,
        'Blood Group':s.BGroup,
        'Phone No ':s.phone1,
        'Address': s.Address1,
        'Percentage':s.percentage,
        'Backlogs':s.Nu_Backlog,
        'Parents Name':s.Father_name,
        'Parents Phone':s.phone2,
        'parents Address':s.Address2
    }

    h1 = "Government Polytechnic Nagpur"
    h2 = "An Autonomous Institute of Government of Maharashtra"
    h3 = "Hostel Admission Form"

    pdf_filename = f"{s.fno2}_student_form.pdf"
    buffer = BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)  
    c.drawString(100, 770, h1)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, h2)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 730, h3)

    y = 700  

    for key, value in data.items():
        c.setFont("Helvetica", 12)  
        c.drawString(100, y, f'{key}: {value}')
        y -= 20

    c.showPage()
    c.save()

    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
    return response

def printform1(request, fno1):
    s = HostelData1.objects.get(fno1=fno1)
    data = {
        'id': s.fno1,
        'Name': s.name,
        'Email': s.Email,
        'Branch':s.Branch,
        'DOB':s.DOB,
        'Caste':s.cast,
        'Nationality':s.nationality,
        'Blood Group':s.BGroup,
        'Phone No ':s.phone1,
        'Address': s.Address1,
        'Percentage':s.percentage,
        'Parents Name':s.Father_name,
        'Parents Phone':s.phone2,
        'parents Address':s.Address2
    }

    h1 = "Government Polytechnic Nagpur"
    h2 = "An Autonomous Institute of Government of Maharashtra"
    h3 = "Hostel Admission Form"

    pdf_filename = f"{s.fno1}_student_form.pdf"
    buffer = BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)  
    c.drawString(100, 770, h1)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, h2)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 730, h3)

    y = 700  

    for key, value in data.items():
        c.setFont("Helvetica", 12)  
        c.drawString(100, y, f'{key}: {value}')
        y -= 20

    c.showPage()
    c.save()

    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
    return response