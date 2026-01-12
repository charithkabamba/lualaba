from django.shortcuts import render

# Create your views here.
def esg(request):
    return render(request, 'esg/esg.html')

def safety(request):
    return render(request, 'esg/safety.html')
