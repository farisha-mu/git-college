from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('tregister',views.tregister,name='tregister'),
    path('addfacualtyadmin',views.addfacualtyadmin,name='addfacualtyadmin'),
   
    path('adminhome',views.adminhome,name='adminhome'),
    path('thome',views.thome,name='thome'),
    path('shome',views.Shome,name='shome'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addfacualty',views.addfacualty,name='addfacualty'),
    path('showstudentdata',views.showstudentdata,name='showstudentdata'),
    path('showteacherdata',views.showteacherdata,name='showteacherdata'),
    path('student_update/<int:student_id>/', views.student_update, name='student_update'),
   path('student_update/<int:student_id>', views.edit_student, name='student_edit'),
   path('student_delete/<int:student_id>/', views.delete_student, name='student_delete'),
   path('edit_faculty_admin/<int:faculty_admin_id>/', views.edit_faculty_admin, name='edit_faculty_admin'),
   path('delete_faculty_admin/<int:faculty_admin_id>/', views.delete_faculty_admin, name='delete_faculty_admin'),
  path('view_profile/', views.view_teacher_profile, name='view_profile'),
  path('profile/edit/',views. edit_teacher_profile, name='edit_teacher_profile'),
   path('profile/delete/', views.delete_teacher_profile, name='delete_teacher_profile'),
    
]