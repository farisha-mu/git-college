from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import course, teacher, student
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'home.html')


def login(request):

    if request.method == 'POST':
      username= request.POST['uname']
      password= request.POST['pwd']
      user=auth.authenticate(username=username,password=password)
      if user is not None:
          auth.login(request,user)
          if request.user.is_staff == True:
              return redirect('adminhome')
          else:
              return redirect('thome')
      else:
          messages.error(request,'invalid')
    return render(request,'login.html')      
    
def tregister(request):

    
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        mail = request.POST.get('email')
        mobile = request.POST.get('num')
        u_name = request.POST.get('uname')
        passwd = request.POST.get('pwd')
        cpasswd = request.POST.get('cpwd')
        img = request.FILES.get('img')
        select = request.POST['select']
        c_name = course.objects.get(id=select)

        if passwd == cpasswd:

            if User.objects.filter(username=u_name).exists():
                messages.warning(request,'Username already exists')
                return redirect('home')

            else:

                try:
                    user = User.objects.create_user(first_name=f_name, last_name=l_name,email=mail, password=passwd, username=u_name)

                    user.save()

                    data = User.objects.get(id=user.id)
                    faculty_data = teacher(phone=mobile,user=data,course_fk=c_name,image=img)

                    faculty_data.save()
                    messages.success(request,'Faculty added successfully')
                    return redirect('login')
                except:
                    messages.error(request,'Error , try again later')
                    return redirect('home')
        else:
            messages.error(request,'Passwords not matching')
            return redirect('addfacualty')
    c_data = course.objects.all()
    return render(request, 'teacherregister.html', {'c_data': c_data})







def addfacualtyadmin(request):
    
     if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        mail = request.POST.get('email')
        mobile = request.POST.get('num')
        u_name = request.POST.get('uname')
        passwd = request.POST.get('pwd')
        cpasswd = request.POST.get('cpwd')
        img = request.FILES.get('img')
        select = request.POST['select']
        c_name = course.objects.get(id=select)

        if passwd == cpasswd:

            if User.objects.filter(username=u_name).exists():
                messages.warning(request,'Username already exists')
                return redirect('home')

            else:

                try:
                    user = User.objects.create_user(first_name=f_name, last_name=l_name,email=mail, password=passwd, username=u_name)

                    user.save()

                    data = User.objects.get(id=user.id)
                    faculty_data = teacher(phnone=mobile,user=data,course_fk=c_name,image=img)

                    faculty_data.save()
                    messages.success(request,'Faculty added successfully')
                    return redirect('addfacualty')
                except:
                    messages.error(request,'Error , try again later')
                    return redirect('home')
        else:
            messages.error(request,'Passwords not matching')
            return redirect('addfacualty')
     c_data = course.objects.all()
     return render(request, 'addfacualty.html', {'c_data': c_data})



    











def showteacherdata(request):
    
    show=teacher.objects.all()
     
    return render(request,'teacherdata.html',{'c_data':show})






   
def adminhome(request):
    return render(request,'adminhome.html')



def thome(request):
    
    return render(request, 'teacherhome.html')

    


def Shome(request):
    return render(request,'studenthome.html')



def addcourse(request):
    if request.method == 'POST':
        coursename=request.POST['cname']
        course.objects.create(course_name=coursename)
        messages.info(request,'course added successfully')
        

    return render(request,'addcourse.html')

def addstudent(request):
    if request.method == 'POST':
        # Handle POST request
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        num = request.POST.get('num')
        email = request.POST.get('email')
        course_id = request.POST.get('select')
        img = request.FILES.get('img')

        course_instance = course.objects.get(pk=course_id)

        new_student = student(
            first_name=f_name,
            last_name=l_name,
            phone=num,
            email=email,
            course_fk=course_instance,
            image=img
        )
        new_student.save()

        c_data = course.objects.all()
        messages.info(request,'student added successfully')
        
        return render(request, 'addstudent.html', {'c_data': c_data})
    
    else:
        # Handle GET request
        c_data = course.objects.all()
        return render(request, 'addstudent.html', {'c_data': c_data})

def addfacualty(request):
    
    return render(request,'addfacualty.html')


def showstudentdata(request):
     show=student.objects.all()
     return render(request,'studentdata.html',{'c_data':show})




def student_update(request, student_id):
    student_instance = student.objects.get(pk=student_id)
    courses = course.objects.all()
    return render(request, 'student_update.html', {'student': student_instance, 'courses': courses})


def edit_student(request, student_id):
    student_instance = get_object_or_404(student, pk=student_id)
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        num = request.POST.get('num')
        email = request.POST.get('email')
        course_id = request.POST.get('select')
        img = request.FILES.get('img')

        course_instance = course.objects.get(pk=course_id)

        student_instance.first_name = f_name
        student_instance.last_name = l_name
        student_instance.phone = num
        student_instance.email = email
        student_instance.course_fk = course_instance
        if img:
            student_instance.image = img
        
        student_instance.save()
        return HttpResponse("Student deleted successfully!")

       
    else:
        courses = course.objects.all()
        return render(request, 'editstudent.html', {'student': student_instance, 'courses': courses})
    


def delete_student(request, student_id):
    student_instance = get_object_or_404(student, pk=student_id)
    if request.method == 'POST':
        student_instance.delete()
        return redirect('showstudentdata')


    return render(request, 'studentdelete.html', {'student': student_instance})    
    


def edit_faculty_admin(request, faculty_admin_id):
    faculty_admin_instance = get_object_or_404(teacher, pk=faculty_admin_id)
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        mail = request.POST.get('email')
        mobile = request.POST.get('num')
        u_name = request.POST.get('uname')
        passwd = request.POST.get('pwd')
        cpasswd = request.POST.get('cpwd')
        img = request.FILES.get('img')
        select = request.POST['select']
        c_name = course.objects.get(id=select)

        if passwd == cpasswd:
            try:
                # Update User data
                user = User.objects.get(id=faculty_admin_instance.user.id)
                user.first_name = f_name
                user.last_name = l_name
                user.email = mail
                user.username = u_name
                if passwd:
                    user.set_password(passwd)
                user.save()

                # Update Teacher data
                faculty_admin_instance.phnone = mobile
                faculty_admin_instance.course_fk = c_name
                if img:
                    faculty_admin_instance.image = img
                faculty_admin_instance.save()

                messages.success(request, 'Faculty/admin updated successfully')
                return redirect('adminhome')
            except:
                messages.error(request, 'Error, try again later')
                return redirect('home')
        else:
            messages.error(request, 'Passwords not matching')
            return redirect('addfacualty')  # Redirect to the form page if passwords don't match

    c_data = course.objects.all()
    return render(request, 'teacheradmin_update.html', {'faculty_admin': faculty_admin_instance, 'c_data': c_data})  


def delete_faculty_admin(request, faculty_admin_id):
    faculty_admin = get_object_or_404(teacher, pk=faculty_admin_id)

    if request.method == 'POST':
        faculty_admin.delete()
        messages.success(request, 'Faculty/Admin deleted successfully')
        return redirect('showteacherdata')

    return render(request, 'teacherdelete.html', {'faculty_admin': faculty_admin})


@login_required
def view_teacher_profile(request):
    # Get the currently logged-in user
    user = request.user

    try:
        # Retrieve the teacher object associated with the user
        teacher_profile = teacher.objects.get(user=user)
    except teacher.DoesNotExist:
        # Handle the case where the teacher object does not exist
        messages.error(request, 'Teacher profile does not exist.')
        return redirect('home')

    # Render the template with the teacher object
    return render(request, 'profile.html', {'teacher_profile': teacher_profile})

@login_required
def edit_teacher_profile(request):
    # Get the teacher profile associated with the current user

    teacher_profile, created = teacher.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Update the teacher profile with the POST data
        teacher_profile.image = request.FILES.get('image')
        teacher_profile.course_fk = request.POST.get('course_fk')
        teacher_profile.phnone = request.POST.get('phone_number')
        teacher_profile.save()  # Save the updated profile
        messages.success(request, 'Profile updated successfully.')
        return redirect('view_teacher_profile')
    
    # If it's a GET request, display the form with current profile data
    return render(request, 'edit_profile.html', {'teacher_profile': teacher_profile})


def delete_teacher_profile(request):
    # Get the teacher profile associated with the current user
    teacher_profile = get_object_or_404(teacher, user=request.user)

    if request.method == 'POST':
        # Delete the teacher profile
        teacher_profile.delete()

        # Optionally, you can also delete the associated user if needed
        # request.user.delete()

        messages.success(request, 'Profile deleted successfully.')
        return redirect('home')  # Redirect to the home page or any other relevant page after deletion
    else:
        # If it's not a POST request, handle it accordingly (e.g., show an error message)
        messages.error(request, 'Invalid request method.')
        return redirect('home') # Redirect to the home page or any other re