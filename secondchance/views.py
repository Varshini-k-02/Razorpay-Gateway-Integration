from django.shortcuts import render
import razorpay
from django.views.decorations.csrf import csrf_exempt

def home(request):
        order_amount = 50000
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}   
        # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)    
        return render(request,'index.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")
