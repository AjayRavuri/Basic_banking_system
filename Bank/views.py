from django.shortcuts import render,redirect
from Bank.models import Customer,Transaction
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
def viewcustomers(request):
    customers=Customer.objects.all()
    return render(request,'view_customers.html',{'customers':customers})
def customerdetails(request,name):
    cusdet=Customer.objects.filter(cname=name)
    return render(request,'customer_details.html',{'cusdet':cusdet})
def transfermoney(request):
    customers=Customer.objects.all()
    if request.method=='POST':
        sender=request.POST['sender']
        sender_acc_no=request.POST['sender_acc_no']
        receiver=request.POST['receiver']
        receiver_acc_no=request.POST['receiver_acc_no']
        amount=request.POST['amount']

        data = request.POST
        sen = data.get('sender')
        rec = data.get('receiver')

        sen = Customer.objects.get(cname=(sen))
        rec = Customer.objects.get(cname=(rec))
        sender_acc = sen.accno
        receiver_acc = rec.accno

        if sender==receiver:
            messages.info(request,'Transaction can not possible between same users.')
            return redirect('/transfermoney')
        elif int(amount)<=0:
            messages.info(request,'Amount can not be zero or negative.')
            return redirect('/transfermoney')
        elif (sender_acc_no!=sender_acc) or (receiver_acc_no!=receiver_acc):
            messages.info(request,"Incorrect Account number.")
            return redirect('/transfermoney')
        elif float(amount)>sen.cbal:
            messages.info(request,"Sender's account balance is insufficient")
            return redirect('/transfermoney')
        else:
            sen.cbal = sen.cbal-float(amount)
            rec.cbal = rec.cbal+float(amount)
            sen.save()
            rec.save()
            transaction=Transaction.objects.get_or_create(sname=sender,saccno=sender_acc_no,rname=receiver,raccno=receiver_acc_no,amnt=amount)
            return redirect('/transsuccess')
    else:
        return render(request,'transfer_money.html',{'customers':customers})
def transsuccess(request):
    return render(request,'trans_success.html')
def transactionhistory(request):
    transactions=Transaction.objects.all()
    return render(request,'transaction_history.html',{'transactions':transactions})
