from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .models import Users
# Create your views here.
from .models import *
from datetime import date,datetime
def index(request):
    return render(request,'publiclogin.html')

def publiclogin(request):
    if request.method== 'POST':
        card_number=request.POST ['cardnumber']
        psw=request.POST ['Password']

        if customers.objects.filter(cardnumber=card_number,password=psw).exists():
            #auth.login(request, user)
            user = customers.objects.get(cardnumber=card_number)
            products=product.objects.all()
            now = date.today()
            print(now)
            tran=transaction.objects.filter(customername=str(card_number))
            now=datetime.now()
            now=now.strftime('%Y-%m-%d')
            return render(request,'purchase.html',{'now':now,'user':user,'products':products,'tran':tran})
        else:
            messages.info(request,'invalid credentials')
            return render(request,'publiclogin.html')  
    else:
        return render(request,'publiclogin.html')    

def publicregister(request):

    if request.method == 'POST':
        fir_pass=request.POST['Password']
        sec_pass=request.POST['Password-repeat']
        if fir_pass==sec_pass:
            for publicitr in customers.objects.all():
                if publicitr.name==request.POST['Name']:
                    messages.info(request,'Name,taken')
                    return render(request,'publicregister.html')
                elif publicitr.Mail==request.POST['Mailid']:
                    messages.info(request,'email taken')
                    return render(request,'publicregister.html')
            print("uploading...")
            public=customers()
            public.name = request.POST['Name']
            public.dob = request.POST['Date_of_birth']
            public.aadhaarnumber = request.POST['Aadhar_number']
            public.gender = request.POST['Gender']
            public.cardtype = request.POST['Card_type']
            public.phone = request.POST['Phone']
            public.cardnumber = request.POST['Card_number']
            public.Mail = request.POST['Mailid']
            public.password = request.POST['Password']
            public.members = request.POST['family']
            public.save()
            return redirect('publiclogin')
        else:
            messages.info(request,'passwordnotmatch')
            return render(request,'publicregister.html')
    else: 
        return render(request,'publicregister.html')  


def mail(request):
    if request.method == 'POST':    
        list=[]
    
        # dd/mm/YY
        
        
        for obj in publicregister.objects.filter(customername=customername,cardnumber=cardnumber):
            customers=customers.objects.filter(cardnumber=obj.cardnumber).first()
            list.append(customers.Mail)
        for i in list:
            print(list)
        send_mail(
        'Vibo Login Details',
        'Your Registration Was Successfull',
        'rationcardpayment@gmail.com',
        list)
        return redirect('publiclogin')


        
def finalpurchase(request):
    if request.method== 'POST':
        print("transaction")
        namef=request.POST['customername']
        tranf=request.POST['trancid']
        datef=request.POST['finaldate']
        timef=request.POST['finaltime']
        moneyf=request.POST['finalamount']
        tranobj=transaction(name=namef,transactionid=tranf,date=datef, time=timef, amount= moneyf)
        tranobj.save()
        return redirect('/')
    else:
        money=request.session['money']
        date=request.session['slot1']
        time=request.session['slot2']
        return render(request,"publicpayment.html",{'money':money,'date':date,'time':time})
        return redirect('/')

def publicpurchase(request):
    if request.method== 'POST':
        print("transaction")
        namef=request.POST['customername']
        tranf=request.POST['trancid']
        datef=request.POST['finaldate']
        timef=request.POST['finaltime']
        moneyf=request.POST['finalamount']
        cardnof=request.POST['cardno']
        tranobj=transaction(name=namef,transactionid=tranf,date=datef, time=timef, amount= moneyf,customername=cardnof)
        tranobj.save()
        return redirect('publiclogin')
    else:
        return render(request,"purchase.html")
        return redirect(request,"publiclogin5.html")
        
        
def publiclogout(request):
    auth.logout(request) 
    return('/')  


def adminlogin(request):
    if request.method== 'POST':
        User_Id = request.POST['User_Id']
        Password = request.POST['Password']

        user = auth.authenticate(User_Id=User_Id,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messagess.info(request,'invalid credentials')
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')    

def adminregister(request):

    if request.method == 'POST':
        User_Id = request.POST['User_Id']
        password = request.POST['password']
        fir_pass=request.POST['createpassword']
        sec_pass=request.POST['confrimpasswod']
        if fir_pass==sec_pass:
            for adminitr in Admin.objects.all():
                if admin.Name==request.POST['Name']:
                    messages.info(request,'Name,taken')
                    return render(request,'adminregister.html')
                if adminitr.email==request.POST['MailId']:
                    messages.info(request,'email taken')
                    return render (request,adminregistration.html)
                admin=Admin()
                admin.Name = request.POST['Name']
                admin.Aadhaar_number = request.POST['Aadhar_number']
                admin.gender = request.POST['gender']
        
                admin.Phone = request.POST['Phone']
            
                admin.email = request.POST['email']
                admin.Password = request.POST['Password']
                admin.save()
                return render(request,'adminregister.html')
        else:
            return render(request,'adminregister.html')
    else: 
        return render(request,'adminregister.html')  



def adminlogout(request):
    auth.logout(request)
    return redirect('/')  


def publicpayment(request):
    if request.method == 'POST':
        totalamount = request.POST ['Amount']
        return render(request,'publicpayment.html',{"totalamount":totalamount}) 
       



    

     



