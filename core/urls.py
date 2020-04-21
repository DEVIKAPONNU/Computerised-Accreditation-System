from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('teacherlogin/', auth_views.LoginView.as_view(template_name='teacher/teacherlogin.html'), name='teacherlogin'),
	path('courseAttended/',views.courseAttended, name='courseAttended'),
	path('teacherindex/',views.teacherindex, name='teacherindex'),
	path('qp/',views.qp, name='qp'),
	path('internals/',views.internals, name='internals'),
	path('studentlogin/',auth_views.LoginView.as_view(template_name="student/studentlogin.html"), name='studentlogin'),
	path('s1/',views.s1_view, name='s1_view'),
	path('s2/',views.s2_view, name='s2_view'),
	path('s3/',views.s3_view, name='s3_view'),
	path('s4/',views.s4_view, name='s4_view'),
	path('s5/',views.s5_view, name='s5_view'),
	path('s6/',views.s6_view, name='s6_view'),
	path('s7/',views.s7_view, name='s7_view'),
	path('s8/',views.s8_view, name='s8_view'),
	path('feedback/',views.feedback, name='feedback'),
	path('studentindex/',views.studentindex, name='studentindex'),
	path('labindex/',views.labindex, name='labindex'),
	path('lablogin/',auth_views.LoginView.as_view(template_name="lab/lablogin.html"), name='lablogin'),




]
