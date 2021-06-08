from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def createPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_user_exits =get_user_model().objects.filter(username=username).exists()

        if is_user_exits ==False:
            'that means the user is not in database u free to create '
            user = get_user_model().objects.create_user(username=username,email=email,password=password)
            messages.success(request,'Your Account Has been Created Check Your email for more info')
            # now let send the mail to the user
            # send message to the user
            send_mail(
            'Subject here',
            f"Hi {username}, you just created an account on Rapheal's portal",
            settings.EMAIL_HOST_USER,
            [f'{email}',],
            fail_silently=False,
            )

            # send message to the  odmin
            send_mail(
            'Subject here',
            f"Hi Raphael,  {username} just created an account or login on your portal",
            settings.EMAIL_HOST_USER,#hey this is the sender and can be reset in the settings.py
            [settings.EMAIL_HOST_USER,],
            fail_silently=False,
            )
            return redirect('/')
        else:
            messages.success(request,'Username exits Already')


    return render(request,'index.html')

def loginPage(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)

        isUser = authenticate(username=username,password=password)
        if isUser != None:
            messages.success(request,'You have been logged In ')
        else:
            messages.success(request,'Bad  Credentials')



    return render(request,'index.html')

