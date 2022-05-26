from distutils.command.build_scripts import first_line_re
import imp
from django.shortcuts import render
from .forms_register import RegistrationForm
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
  #  response = HttpResponse()
    #response.writelines('Xin chào')
   # response.write('Homes')
   # return response
   return render(request,'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error(request):
  return render(request, 'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})
  