from django.shortcuts import render,redirect
from account.models import Accounts
from .models import Forgatetoken
from django.contrib.auth.models import User
import random
from django.contrib import messages

# Create your views here.
def forgatepage(request):
    if request.method =="POST":
        username = request.POST['userid']
        print(username)
        if User.objects.filter(username = username).exists():
            if Forgatetoken.objects.filter(username = username).exists():
                Forgatetoken.objects.filter(username = username).delete()
                otp = random.randint(1000,9999)
                print('OTP :',otp)
                querry = Accounts.objects.get(username = username)
                email = querry.email
                name = querry.name

                import smtplib, ssl
                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "noreplay.rechstore@gmail.com"  # Enter your address
                receiver_email = email  # Enter receiver address
                password = 9015749179
                message = """\
                Subject: RechSTORE

                """+"""
                Hello """+str(name)+"""
                        """+str(otp)+" is your OTP to resat password of your account, Please Don't share this with anyone."

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)


                x = Forgatetoken(username = username, otp = otp)
                x.save()
                return render(request,'forgate password/forgateotp.html',{'u':username})
            else:
                otp = random.randint(1000,9999)
                print('OTP :',otp)

                querry = Accounts.objects.get(username = username)
                email = querry.email
                name = querry.name

                import smtplib, ssl
                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "noreplay.rechstore@gmail.com"  # Enter your address
                receiver_email = email  # Enter receiver address
                password = 9015749179
                message = """\
                RechSTORE

                """+"""
                Hello """+str(name)+"""
                        """+str(otp)+" is your OTP to resat password of your account, Please Don't share this with anyone."

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)


                x = Forgatetoken(username = username, otp = otp)
                x.save()
                return render(request,'forgate password/forgateotp.html',{'u':username})
        else:
            return render(request,'forgate password/forgate.html',{'key_error':'Invalid UserName'})
    else:
        return render(request,'forgate password/forgate.html')

def forgateotppage(request):
    if request.method =="POST":
        username = request.POST['username']
        print('username is : ', username)
        if Forgatetoken.objects.filter(username = username).exists():
            querry = Forgatetoken.objects.get(username = username)

            otp = querry.otp
            print('Save OTP : ',otp)

            user_otp = request.POST['otp']
            print('User OTP is : ',user_otp)

            cont = querry.cont
            print(cont)

            while cont<=4:
                if int(user_otp) == int(otp) :
                    return render(request,'forgate password/setnewpassword.html',{'u':username})
                else:
                    print('Before : ',cont)
                    if cont <4:
                        ff = ' Attempt Left'
                        err2 = 5-cont
                        err = str(err2)+ff
                        print(err)
                    else:
                        err = 'Last Attempt'
                    cont = cont+1
                    Forgatetoken.objects.filter(username=username).update(cont = cont)
                    print('After : ',cont)
                    return render(request, 'forgate password/forgateotp.html',{'key_error':'Invalid OTP','u':username, 'err':err})
            else:
                Forgatetoken.objects.filter(username = username).delete()
                messages.info(request,'Sorry!, maximum try over')
                return redirect('login')

def newpassword(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['pass1']
        print(password)
        if User.objects.filter(username = username).exists():
            x = User.objects.get(username = username)
            x.set_password(password)
            x.save()
            Accounts.objects.filter(username = username).update(password = password)

            querry = Accounts.objects.get(username = username)
            name = querry.name
            email = querry.email
            passwordac = querry.password

            import smtplib, ssl
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "noreplay.rechstore@gmail.com"  # Enter your address
            receiver_email = email  # Enter receiver address
            password = 9015749179
            message = """\
            RechSTORE

            """+"""
            Hello """+str(name)+"""
                    """+"""Congratulations!!!, your password has be reset successfully, Please Note.
                                Username : """+str(username)+"""
                                Password : """+str(passwordac)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)


            messages.info(request,'Password resat succefully')
            return redirect('login')
