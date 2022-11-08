from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

def index(request):
  # if request.user.is_anonymous:
  #   return redirect('/login')
  return render(request, 'index.html')

def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    desc = request.POST.get('desc')

    contact = Contact(name=name, email=email, contact=contact, desc=desc, date=datetime.today())
    contact.save()
    messages.success(request, 'Contact create Successfully!')
  else:
    messages.warning(request, 'Contact Model WIP!')
  return render(request, 'contact.html')

def home(request):
  return render(request, 'index.html')
