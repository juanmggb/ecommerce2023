from django.shortcuts import render, HttpResponse

# Create your views here.
def register(request):

    return render(request, "account/registration/register.html")