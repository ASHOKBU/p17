from django.shortcuts import render
from myapp import forms

# Create your views here.
from myapp.utilities import store_image
def builtin(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)
        if form.is_valid():
            first_name= form.cleaned_data.get('first_name')
            last_name= form.cleaned_data.get('last_name')
            email= form.cleaned_data.get('email')
            phno= form.cleaned_data.get('phno')
            pwd= form.cleaned_data.get('pwd')
            birthday= form.cleaned_data.get('birthday')
            birthmonth= form.cleaned_data.get('birthmonth')
            birthyear= form.cleaned_data.get('birthyear')
            gender= form.cleaned_data.get('gender')
            language= form.cleaned_data.get('language')
            data=form.cleaned_data
            return render(request,"displaydata.html",context=data)
    form=forms.SampleForm()
    return render(request,'builtinform.html',{'form':form})
