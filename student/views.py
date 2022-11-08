from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
  response = requests.get('http://127.0.0.1:1025/student/')
  students = response.json()
  return render(request, "student/index.html", {'students': students['results']})

def new(request):
  response = requests.get('http://127.0.0.1:1025/subject/')
  subjects = response.json()
  # if request.user.is_authenticated:
  #   print("Logged in")
  # else:
  #   print("Not logged in")
  # teachers = Teacher.objects.all()
  return render(request, "student/new.html", {'subjects': subjects['results']})

def show(request, id):
  student = find_student(request, id)
  # student = Student.objects.get(id=id)
  return render(request, "student/show.html", {'student': student})

def edit(request, id):
  student = find_student(request, id)
  # student = Student.objects.get(id=id)
  return render(request, "student/edit.html", {'student': student})

def destroy(request, id):
  student = find_student(request, id)
  # student = Student.objects.get(id=id)
  student.delete()
  messages.success(request, 'Contact Deleted Successfully!')
  return redirect("index")

def find_student(request, id):
  student = Student.objects.get(id=id)
  return student

def create(request):
  if request.method == "POST":
    url = 'http://127.0.0.1:1025/student/'
    payload = request.POST
    response = requests.post(url, data = payload)
    breakpoint()
    if response.status_code == 200:
      return render(request, 'student/index.html')
    else:
      return render(request, 'student/new.html')


def update(request, id):
  student = find_student(request, id)
  # student = Student.objects.get(id=id)

  form = StudentForm(request.POST, instance = student)
  print("+++++++++++++++++++++++")
  print(student)
  print(form.is_valid())
  print(form)
  print("+++++++++++++++++++++++")
  if form.is_valid():
    form.save()
    return redirect("show")
  return render(request, 'student/edit.html', {'student': student})
