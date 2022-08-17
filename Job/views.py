from django.shortcuts import render,redirect
from django.core import paginator
from .form import Applyform,JobForm
from .models import job
from django.urls import reverse



# Create your views here.
def job_list(request):
    job_list=job.objects.all()
    context={'jobs':job_list}
    return render(request,'job_list.html',context)

def job_detail(request, slug):
    job_detail=job.objects.get(slug=slug)

    if request.method=='POST':
        form = Applyform(request.POST , request.FILES)
        if form.is_valid():
            myform.Job = job_detail
            myform = form.save(commit=False)
            myform.save()
            print('DOne')

    else:
        form =Applyform
    
    context={'job':job_detail,'form':form}
    return render(request,'job_detail.html',context)
    
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('job_list'))

    else:
        form = JobForm()

    return render(request,'add_job.html',{'form':form})