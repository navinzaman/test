from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from FinalProjectApp.models import StudentInfo, FacultyComment, CourseData, Enrollment
from django.db.models import Count, Avg
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

#CSRP - cross site request forgery 

@login_required
def home(request):
    context = {'name': 'Gemma Wood'}
    return render(request, 'FinalProjApp/home.html', context)

@login_required
def studentdetails(request):
    student_list = StudentInfo.objects.all()
    paginator = Paginator(student_list, 10)  
    page = request.GET.get('page')
    students = paginator.get_page(page)
    context = {'students': students}
    return render(request, 'FinalProjApp/studentdetails.html', context)


@login_required 
def coursedetails(request):
    course_list = CourseData.objects.all()
    paginator = Paginator(course_list, 10) 
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    context = {'courses': courses}
    return render(request, 'FinalProjApp/coursedetails.html', context)


@login_required
def studentenrollment(request):
    students = StudentInfo.objects.all()
    courses = CourseData.objects.all()
    enrolldata = Enrollment.objects.all()
    student_id = request.GET.get('student_dropdown', students.first().studentid)
    enrolled_courses = Enrollment.objects.filter(student=student_id)
    context = {'students': students, 'courses': courses, 'enrolldata': enrolldata, 'enrolled_courses': enrolled_courses, 'selected_student_id': student_id, }
    
    
    return render(request, 'FinalProjApp/studentenrollment.html', context)




def save(request):
    if 'student' in request.GET and 'course' in request.GET:
        student1 = request.GET.get('student')
        course1 = request.GET.get('course')
       
    
        enrolled_count = Enrollment.objects.filter(student=student1).count()
        if enrolled_count >= 3:
            return HttpResponse('Error: You have already enrolled in the maximum number of courses.')
        
        
        enrollment_count = Enrollment.objects.filter(student=student1, course=course1).count()
        if enrollment_count < 10000:
            enrollment = Enrollment(student=student1, course=course1)
            enrollment.save()
            return HttpResponse('Success')
    
    return HttpResponse('Error')
    
    
    
    
    
    
@login_required
def dashboard(request):
    total_students = StudentInfo.objects.count()
    avg_gpa = StudentInfo.objects.aggregate(Avg('gpa'))
    year_counts = StudentInfo.objects.values('studentyear').annotate(count=Count('studentyear'))
    course_count = CourseData.objects.count()

    context = {
        'total_students': total_students,
        'avg_gpa': avg_gpa['gpa__avg'],
        'year_counts': year_counts,
        'course_count': course_count,
    }
    return render(request, 'FinalProjApp/dashboard.html', context)


@login_required
def commentpage(request):
    return render(request, 'FinalProjApp/comment.html')

def savecomment(request):
    if ('useremail' in request.GET and 'usercomment' in request.GET):
        femail = request.GET.get('useremail')
        fcomment = request.GET.get('usercomment')
        data = FacultyComment(facultyemail = femail, facultycomment = fcomment)
        data.save()
    return HttpResponse('Success')
