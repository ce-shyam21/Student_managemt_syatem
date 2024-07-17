from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from .models import Student
from .forms import StudentForm

def index(request):
    SearchStudent = request.GET.get('SearchStudent')
    if SearchStudent:
        students = Student.objects.filter(student_number__icontains=SearchStudent)
    else:
        students = Student.objects.all()
    return render(request, 'students/index.html',	{'SearchStudent':SearchStudent, 'students': students})


# def index(request):
#   return render(request, 'students/index.html', {
#     'students': Student.objects.all()
#   })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))
# ... other view functions ...

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads.
        if form.is_valid():
            form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': form
    })

def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)  # Include request.FILES to handle file uploads.
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })

# ... other view functions ...

def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))
