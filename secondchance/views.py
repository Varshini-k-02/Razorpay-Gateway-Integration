from django.shortcuts import render
import razorpay

def home(request):
        return render(request,'index.html')


# def success(request):
#     return render(request, "success.html")
