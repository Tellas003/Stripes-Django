"""
URL configuration for stripes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from my_app import views

urlpatterns = [
    path('secret/', admin.site.urls),
    path('myapp', include('my_app.urls')),
path('',views.Homepage, name='home'),

    path('about',views.about),
path('contact',views.contact),
path('gallery',views.gallery),
path('principalmessage',views.principal, name='princiaplmessage'),
path('feedback',views.feed,name='feedback'),
path('course_1',views.course_1, name='course_1'),
path('course_2',views.course_2, name='course_2'),
path('course_3',views.course_3, name='course_3'),
path('course_4',views.course_4, name='course_4'),
path('course_5',views.course_5, name='course_5'),
path('course_6',views.course_6, name='course_6'),
path('course_7',views.course_7, name='course_7'),
path('course_8',views.course_8, name='course_8'),
path('course_9',views.course_9, name='course_9'),
path('course_10',views.course_10, name='course_10'),
path('course_11',views.course_11, name='course_11'),
path('course_12',views.course_12, name='course_12'),
path('course_13',views.course_13, name='course_13'),
path('Course_Shedule',views.shedule, name='shedule'),
path('search', views.search, name='search'),

 
path('certificate', views.search_certificate, name='certificate'),

]

'''path('dashboard', views.LoginPage, name='dashboard'),
path('logout/',views.logoutuser),
path('adminpage',views.adminpage),
path('student_profile/', views.student_profile, name='student_profile'),'''