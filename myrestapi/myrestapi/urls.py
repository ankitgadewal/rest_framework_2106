from django.contrib import admin
from django.urls import include, path
from restapp import views
import rest_framework

urlpatterns = [
    path('', views.QuickLinks.as_view(), name='QuickLinks'),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'), name='auth'),
    path('students/', views.StudentsView.as_view(), name='students'),
    path('students/<str:student_name>/', views.StudentDetailView.as_view(), name='single-student'),
    path('allsubjects/', views.AllSubjectView.as_view(), name='allsubjects'),
    path('attendance/', views.AttendanceView.as_view(), name='attendance'),
    path('bookdistribution/', views.BookDistributionView.as_view(), name='bookdistribution'),
    path('class/', views.ClassView.as_view(), name='class'),
    path('classsubjects/', views.ClassSubjectsView.as_view(), name='classsubjects'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('registration/', views.RegisterUserView.as_view(), name='registration'),
    path('allregistrations', views.AllRegistrationsView.as_view(), name='allregistrations'),
    path('allregistrations/<str:username>', views.SingleRegistrationView.as_view(), name='singleuser'),
    path('teachers/', views.TeachersView.as_view(), name='teachers'),
    path('teachers/<str:teacher_name>/', views.SingleTeacherView.as_view(), name='single-teacher'),
    path('teachersubjects/', views.TeacherSubjectView.as_view(), name='teachersubjects'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
