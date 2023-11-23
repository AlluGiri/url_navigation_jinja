from django.shortcuts import render

# Create your views here.
def sweety(request):
    return render(request,'sandhya.html')

def sandhya(request):
    return render(request,'sweety.html')

# def myself(request):
#     return render(request,'Allu.html')
