from exp.models import Expenditure
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, UserManager
# Create your views here.
def dashboard(request):
    user=request.user
    uid=user.id
    data=Expenditure.objects.filter(User_id=uid)
    total=0
    for i in data:
        total+=i.amount
    return render(request,'dashboard.html',{'datalist':data,'total':total})

def addevent(request):
    return render(request,'addevent.html')

def addnewevent(request):
    print("inside")
    if(request.method=='POST'):
        print("inside post")
        date = request.POST['date1']
        par=request.POST['par']
        amount=request.POST['amount']
        mode =request.POST['mode']
        uid=request.POST['uid']
        event = Expenditure(date=date,amount=amount,particular = par,mode_of_payment=mode,User_id=uid)
        event.save()
        return redirect('dashboard')
    else:
        return redirect('dashboard')