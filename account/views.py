from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Accounts
from .models import Token
from django.contrib import messages

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username =  request.POST['usrnam']
            password = request.POST['pass']
            from django.contrib import auth
            login_user = auth.authenticate(username = username, password = password)
            if login_user is None:
                messages.info(request,'User Id and Password incorect')
                return redirect('login')
            else:
                auth.login(request, login_user)
                return redirect('home')
        else:
            return render(request,'login/login.html')

            # that ok--------------------------------------------------------------------------------------------

def validation(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        username = request.POST['username']
        password = request.POST['pass']
        password1 = request.POST['pass1']

        if password == password1:
            if User.objects.filter(username = username).exists():
                return render(request,'register/register.html',{'error_key1':'User id is already taken, Please choose another username'})
            else:
                if Token.objects.filter(username = username).exists():
                    tok = Token.objects.get(username = username)
                    tok2 = tok.token
                    tok3 = 'You have alyeardy registered, Please Verify your account.Your tokken Number is '
                    tok4 = tok3 + str(tok2)
                    return render(request,'register/register.html',{'error_key2':tok4})
                else:
                    cont = 0
                    while cont == 0:
                        import random
                        random_number = random.randint(1000000000000,9999999999999)
                        print(random_number)
                        hex_number = hex(random_number).upper()
                        token_number = hex_number[2:-1]
                        if Token.objects.filter(token = hex_number).exists():
                            cont = 0
                        else:
                            print(token_number)
                            print('length : ', len(token_number))
                            cont = 1

                    otp = random.randint(1000,9999)
                    print('OTP :',otp)

                    x = Token(username = username, token = token_number, otp = otp, name = name, email = email, phone = mobile, password = password)
                    x.save()

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
                            """+str(otp)+" is your OTP to verify your account in RechSTORE, Your Token number is : "+str(token_number)+",use if fail to verify. Please Don't share this with anyone."

                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)




                    # b = str(mobile)
                    # lis = []
                    # x = b[0:2]
                    # y = b[2:-2]
                    # z = b[-2:]
                    # for i in range(0,len(y)):
                    #   lis.append('X')
                    # y = "".join(lis)
                    # m=x+y+z
                    # print(m)

                    # import requests
                    #
                    # url = "https://www.fast2sms.com/dev/bulk"
                    #
                    # payload = "sender_id=FSTSMS&language=english&route=qt&numbers=mobile&message=23641&variables={#AA#}|{#CC#}&variables_values=3659|56DF54GHTV"
                    # headers = {
                    #     'authorization': "spNM1K5g03ZCIwld264OuPzTVfykiDqRxaAtcnGF7jhmJLUbvElKSIazLx5ckbqdtQ1JmF8n0hYPC9sX",
                    #     'cache-control': "no-cache",
                    #     'content-type': "application/x-www-form-urlencoded"
                    #     }
                    #
                    # response = requests.request("POST", url, data=payload, headers=headers)
                    #
                    # print(response.text)
                    return render(request, 'register/confirm.html',{'u':username})
        else:
            return render(request,'register/register.html',{'error_key2':'Password cannot be match.'})

def register(request):

    if request.method =="POST":

        # name = request.POST['name']
        # email = request.POST['email']
        # mobile = request.POST['mobile']
        username = request.POST['username']
        # password = request.POST['pass']
        # password1 = request.POST['pass1']


        if User.objects.filter(username = username).exists():
            return render(request,'register/register.html',{'error_key1':'User id is already taken, Please choose another username'})
        else:
            user_otp = request.POST['otp']
            print('User OTP is : ',user_otp)

            querry_otp = Token.objects.get(username=username)

            otp = querry_otp.otp
            name = querry_otp.name
            username =querry_otp.username
            email = querry_otp.email
            mobile = querry_otp.phone
            passwordac = querry_otp.password

            cont = querry_otp.cont


            while cont<=4:
                if int(user_otp) == int(otp) :
                    x = User.objects.create_user(first_name = name, email= email, username= username, password = passwordac)
                    y = Accounts(name = name, email= email, username= username, password = passwordac, phone = mobile)
                    x.save()
                    y.save()
                    Token.objects.filter(username = username).delete()

                    tk = Accounts.objects.get(username = username)

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
                            """+"""Congratulations!!!, your account create successfully, Please Note.
                                        Username : """+str(username)+"""
                                        Password : """+str(tk.password)
                    print("pas : ",tk.password)

                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)



                    return redirect('login')
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
                    Token.objects.filter(username=username).update(cont = cont)
                    print('After : ',cont)
                    return render(request, 'register/confirm.html',{'key_error':'Invalid OTP','u':username, 'err':err})
            else:
                Token.objects.filter(username = username).delete()
                return render(request,'register/register.html',{'error_key2':'Sorry!, You maximum try is over, Please register again.'})
    else:
        return render(request,'register/register.html')

def activating_user(request):
    return render(request,'register/token.html')

def validate_token(request):
    token = request.POST['token']
    if Token.objects.filter(token = token).exists():
        querry = Token.objects.get(token = token)
        username = querry.username
        name = querry.name
        email = querry.email

        import random
        otp = random.randint(1000,9999)
        print('OTP :',otp)

        Token.objects.filter(username=username).update(otp = otp)

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
                """+str(otp)+" is your OTP to activate your account, Remamber you have only 4 Attempt to varify, if fails then you need to re-register. Please Don't share this with anyone."

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


        return render(request, 'register/confirm.html',{'u':username})
    else:
        return render(request,'register/token.html',{'key_error':'Please Enter Correct Token Number'})
