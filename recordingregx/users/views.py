from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail
from django.conf import settings
msg_en = '''
Thank you for the Registration.
The Administrator will be automatically notified and review your application.

Best Regards
Your ScoreBook Administration
'''

msg_de = '''
Vielen Dank für die Registrierung.
Der Administraton wird automatisch benachrichtigt.
Sie werden benachrichtigt wenn Ihr Profil aktiviert wird.

Ihre Anmeldedaten:
user    : {uname}
email   : {email}
password: *******


Mit freundlichen Grüßen
ScoreBook Administration
info@bohrlab.de
'''
msg_admin = '''
New Registration

Ihre Anmeldedaten:
user    : {uname}
email   : {email}

'''
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
            
            username = form.cleaned_data.get('username')
            if (settings.EMAIL_USE_EMAIL):
                email = form.cleaned_data.get('email')
                #notification for new user
                send_mail(subject = 'ScoreBook',
                message= msg_de.format(uname=username, email=email), 
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email])
                #notification for admin
                send_mail(subject='New Registration',
                message = msg_de.format(uname=username, email=email), 
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['alexej1412@gmail.com'])

            messages.success(request,f'Account created for {username} ! Youre registration will be reviewed ! ')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f'Your Accout has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': user_form,
        'p_form': profile_form
    }
    return render(request, 'users/profile.html', context)