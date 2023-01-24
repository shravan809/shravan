from django.shortcuts import render,HttpResponse
from .forms import *
from .models import *
# Create your views here.


# def signup(request):

#     form = SignUp
#     return render (request,"UserAccounts/signup.html",{'forms':form})

# from django.shortcuts import render

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            # email=form.cleaned_data['email']
            # first_name=form.cleaned_data['first_name']
            # last_name=form.cleaned_data['last_name']
            # mobile_number=form.cleaned_data['mobile_number']
            obj=form.save()
            return HttpResponse('Success')
            

    else:
        form = SignUp

    return  render (request,"UserAccounts/signup.html",{'forms':form})

def vender(request):
    if request.method == 'POST':
        form = VenderForm(request.POST)
        if form.is_valid():
            # email=form.cleaned_data['email']
            # first_name=form.cleaned_data['first_name']
            # last_name=form.cleaned_data['last_name']
            # mobile_number=form.cleaned_data['mobile_number']
            obj = form.save()
            return HttpResponse('Success')


    else:
        form = VenderForm

    return render(request, "UserAccounts/vender.html", {'forms': form})