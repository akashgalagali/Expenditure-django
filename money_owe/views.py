from django.contrib.auth.models import User
from money_owe.models import Owe
from django.shortcuts import redirect, render

# Create your views here.
def oweDashboard(request):
    user=request.user
    uid=user.id
    data=Owe.objects.filter(lender=uid)|Owe.objects.filter(borrower=uid)
    total=0
    for i in data:
        total+=i.amount
    return render(request,'oweDashboard.html',{'datalist':data,'total':total})

def oweMoney(request):
    users=User.objects.all()    
    return render(request,'addOwe.html',{'users':users})

def oweNewMoney(request):
    if(request.method=='POST'):
        user=request.user
        date=request.POST['date1']
        amount=request.POST['amount']
        role=request.POST['role']
        person=request.POST['person']
        friend=User.objects.filter(pk=person)
        if(role=='lender'):
            lender=user
            borrower=friend[0]
        else:
            borrower=user
            lender=friend[0]
        mode=request.POST['mode']
        event = Owe(date=date,amount=amount,lender=lender,mode_of_payment=mode,borrower=borrower,user_id=user)
        event.save()
        return redirect('oweDashboard')
    return redirect('oweDashboard')


def oweDelete(request,id):
   owe = Owe.objects.get(pk = id)
   owe.delete()
   return redirect('oweDashboard')
