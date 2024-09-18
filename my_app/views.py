from django.shortcuts import render, redirect
from .models import Verification

from django.db import connection
from django.http import HttpResponse

from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def Homepage(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def principal(request):
    return render(request,'principalmessage.html')
def feed(request):
    return render(request,'feed.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')
def shedule(request):
    return render(request,'shedule.html')
def about(request):
    return render(request,'about.html')
def about(request):
    return render(request,'about.html')
def search(request):
    return render(request,'search.html')
def course_1(request):
    return render(request,'shipsimulatorrolebasedcourse1.html')
def course_2(request):
    return render(request,'shipsimulatorcourse2.html')
def course_3(request):
    return render(request,'shipmastercourse3.html')
def course_4(request):
    return render(request,'bridgewatchkeepingcourse4.html')
def course_5(request):
    return render(request,'bridgewatchkeepingratingscourse5.html')
def course_6(request):
    return render(request,'shiptransfercourse6.html')
def course_7(request):
    return render(request,'largevesselcourse7.html')
def course_8(request):
    return render(request,'framopumpcourse8.html')
def course_9(request):
    return render(request,'electricalcourse9.html')
def course_10(request):
    return render(request,'bwtscourse10.html')
def course_11(request):
    return render(request,'marinecourse11.html')
def course_12(request):
    return render(request,'pneumaticscourse12.html')
def course_13(request):
    return render(request,'safetycourse13.html')
def shedule(request):
    return render(request,'shedule.html')
def adminpage(request):
    return render(request, 'adminlogin.html')

   


def LoginPage(request):
    context={
        "error":""
    }
    if request.method == "POST":
        print(request.POST)
        user=authenticate(username = request.POST['username'], password = request.POST['password'])
        print(user)

        if user is not None:
            login(request, user)
            return render(request, 'dashboard/index.html')
        else:
            context={
                "error":"*Invalid Username OR Password"
            }
            return render(request, 'adminlogin.html', context)
    return render(request,'adminlogin.html')    

def logoutuser(request):
    logout(request)
    return redirect('./adminpage')

def student_profile(request):
    if not request.user.is_authenticated:
        return redirect('./adminpage')  # Redirect to the login page if user is not authenticated

    students = Verification.objects.all()
    return render(request, 'dashboard/register1.html', {'students': students})
# views.py

def search_certificate(request):
    if request.method == 'POST':
      #  certificateStripes=request.POST.get('certificateStripes')
        certificateCourse = request.POST.get('certificateCourse')
        certificateNo = request.POST.get('certificateNo')
        lastName = request.POST.get('lastName')

        # Assuming you have a model called Verification1 corresponding to your table
        # Adjust the model name according to your Django project's models
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM my_app_verification WHERE certificateCourse = %s AND certificateNo = %s AND lastName = %s  ", [certificateCourse+'/', certificateNo, lastName])
            row = cursor.fetchone()
        
        if row is not None:
            context = {
                'courseName': row[0],  # Assuming the course name is in the second column
                'certificateStripes': row[9],  # Assuming certificate stripes are in the third column
                'certificateCourse': row[10],  # Assuming certificate course is in the fourth column
                'certificateNo': row[11],  # Assuming certificate number is in the fifth column
                'participantName': row[5],  # Assuming participant name is in the sixth column
                'passportNo': row[7],  # Assuming passport number is in the seventh column
                'courseDate1': row[3],  # Assuming course date1 is in the eighth column
                'courseDate2': row[4],  # Assuming course date2 is in the ninth column
                'issueDate': row[12],  # Assuming issue date is in the tenth column
            }
            return render(request, 'certificate.html', context)
        else:
            error_message = "Incorrect Certificate Number or Lastname OR Certificate data is yet to be uploaded into the database"
            return render(request, 'error.html', {'error_message': error_message})
    else:
        return render(request, 'search.html')
