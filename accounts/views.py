from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from .form import Sighnupform
from .models import Profile
# Create your views here.

def sighnup(request):
    if request.method=='POST':
        form=Sighnupform(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data['username']
            password =form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form=Sighnupform()
    return render(request,'registration/signup.html', {'form':form} )



def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})



def profile_edit(request):
    pass
