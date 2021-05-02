from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def home_view(request):
    #my_list = ['Ranveer','Ran','Ranvi','Ranve']
    #my_color = ['red','green','blue', 'sky blue']
    Employee = {'Ranveer','Ram'}
    Designation = {'IT','IT'}
    Salary = {'20000','20000'}
    #combined_list = zip(my_list, my_color)
    combined_list = zip(Employee,Designation,Salary)
    context = {
        'reuslt' : combined_list
#        'result' : my_list,
#        'result1' : combined_list,
#        'h1color' : 'red',
#        'h2color' : 'blue',
#        'h3color': 'yellow',
    }
    return render(request,'student_temp/home.html',context)



def about_view(request):
    if request.method == 'POST':
        name = request.POST['tb_name']
        gender = request.POST['tb_gender']
        email = request.POST['tb_email']
        age = request.POST['tb_age']
        dob = request.POST['td_dob']
        city = request.POST['drp_city']
        course = request.POST['cb_course']
        course1 = request.POST['cb_course1']
        address = request.POST['cb_address']
        password = request.POST['tb_password']
        mobile = request.POST['tb_mobile']
        submit = request.POST['tb-submit']
        context = {
            'name' : name,
            'gender': gender,
            'email': email,
            'age': age,
            'dob': dob,
            'city': city,
            'course': course,
            'course1': course1,
            'address': address,
            'password': password,
            'mobile': mobile,
            'submit': submit,           
        }
        return render(request,'student_temp/about.html',context)
    else:
        return render(request,'student_temp/about.html')

def sign_view(request):
    if request.method =='POST':
        name = request.POST['tb_user_name']
        password = request.POST['tb_password']
        if(name=='admin' and password=='admin'):
            return render(request,'student_temp/home.html')
        else:
            context = {
                'error' : 'Invalid id and password'
            }
            return render(request,'student_temp/sign.html',context)
    return render(request,"student_temp/sign.html")
    
def login1_view(request):
    if request.method =='POST':
        name = request.POST['tbname']
        email = request.POST['tbemail']
        context = {
            'name' : name,
            'email' : email,
        }
        return render(request,'student_temp/login.html',context)
    else:
        return render(request,'student_temp/login.html') 

def login_view(request):
    login_form = LoginForm()
    if(request.method=='POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            uname = login_form.cleaned_data['user_name']
            pwd = login_form.cleaned_data['user_pass']
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('../emps')

            else:
                context = {
                    'login_form' : login_form,
                    'error_msg' : 'Invalid id and password'
                        }
                return render(request,'student_temp/login.html',context)
                
    context = {
        'login_form' : login_form
    }
    return render(request,'student_temp/login.html',context)   
    
def signup_view(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user_name = signup_form.cleaned_data['username']
            first_name = signup_form.cleaned_data['first_name']
            last_name = signup_form.cleaned_data['last_name']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            password = make_password(password)
            user = User.objects.create_user(username= user_name,
                                            first_name= first_name,
                                            last_name = last_name,
                                            email= email,
                                            password = password
                                            )
            user.save()
            login(request, user)
            return redirect('../emps')


            
            # dob = signup_form.cleaned_data['dob']
            # age = signup_form.cleaned_data['age']
            # gender = signup_form.cleaned_data['gender']
            # city = signup_form.cleaned_data['city']
            # course1 = signup_form.cleaned_data['course1']
            # course2 = signup_form.cleaned_data['course2']
            # context={
            # 'name' : name,
            # 'email' : email,
            # 'password' : password,
            # 'dob' : dob,
            # 'age' : age,
            # 'gender' : gender,
            # 'city' : city,
            # 'course1' : course1,
            # 'course2' : course2,
            # }
            # return render(request,'student_temp/register-sucess.html', context)
        # else:
        #     context = {
        #         'sign_up':signup_form
        #         }
        #     return render(request,'student_temp/signup.html', context)
    else:
        signup_form = SignupForm()
        context = {
            'sign_up':signup_form
        }
        return render(request,'student_temp/signup.html',context)

# def signup_view(request):
#     if request.method == 'POST':
#         signup_form = SignupForm(request.POST)
#         if signup_form.is_valid():
#             name = signup_form.cleaned_data['name']
#             email = signup_form.cleaned_data['email']
#             password = signup_form.cleaned_data['password']
#             dob = signup_form.cleaned_data['dob']
#             age = signup_form.cleaned_data['age']
#             gender = signup_form.cleaned_data['gender']
#             city = signup_form.cleaned_data['city']
#             course1 = signup_form.cleaned_data['course1']
#             course2 = signup_form.cleaned_data['course2']
#             context={
#             'name' : name,
#             'email' : email,
#             'password' : password,
#             'dob' : dob,
#             'age' : age,
#             'gender' : gender,
#             'city' : city,
#             'course1' : course1,
#             'course2' : course2,
#             }
#             return render(request,'student_temp/register-sucess.html', context)
#         else:
#             context = {
#                 'sign_up':signup_form
#                 }
#             return render(request,'student_temp/signup.html', context)
#     else:
#         signup_form = SignupForm()
#         context = {
#             'sign_up':signup_form
#         }
#         return render(request,'student_temp/signup.html', context)
    
# def orm_practice(request):
#     #qs = EmployeeDetails.objects.all()
#     qs = EmployeeDetails.objects.filter(id_lt=10)

#    # for obj in qs:
#    #     print("name>>>>",obj.name)
#     #    print("designation>>>>", obj.designation)
#     #    print("*******************************************")
#     print("query",qs.query)
#     context = {
#         'qs' : qs
#     }

#     return render(request,'student_temp/allemp.html',context)

def display_employee(request):
    dep_qs = Department.objects.all() 
    # if(request.method == 'POST'):
    #     dep_id = request.POST.get('drp_department')
        #dep_obj = Department.objects.get(id=dep_id)
        #emps = Employee.objects.filter(department__id=dep_id, teamlead_name="Toyeeba")
    emps = Employee.objects.filter(department__id=1)
    #emps = Employee.objects.all()
    context = {
        'emps' : emps,
        'departments' : dep_qs
    }
    return render(request,'student_temp/emps.html',context)
    
    # context = {
    #     'departments' : dep_qs
    # }
    # return render(request,'student_temp/emps.html',context)

def add_dep(request):
    if(request.method == 'POST'):
        dname = request.POST.get('tb_dname')
        loc = request.POST.get('tb_location')
        #print('Department name>>>>', dname)
        #print('Department location>>>>', loc)
        obj = Department()
        obj.name = dname
        obj.location = loc
        obj.save()
        context = {
            'result_message' : 'Your department sucessfully added'
        }
        return render(request,'student_temp/add_department.html',context)
    return render(request,'student_temp/add_department.html')
          

def add_team(request):
    if(request.method=='POST'):
        tname = request.POST.get('tb_tname')
        phone = request.POST.get('tb_phone_no')
        obj = TeamLead()
        obj.name = tname # name is a same of variable
        obj.phone_no = phone #phone_no is a same of variable
        obj.save()
        context = {
            'result_message' : 'Your teamlead sucessfully added'
        }
        return render(request,'student_temp/add_teamlead.html',context)
    return render(request,'student_temp/add_teamlead.html')
          
def add_emp(request):
    dep_qs = Department.objects.all()
    team_tq = TeamLead.objects.all()
    if(request.method=='POST'):
        ename = request.POST.get('tb_name')
        designation = request.POST.get('tb_designation')
        dep_id = request.POST.get('drp_department')
        team_id = request.POST.get('drp_team')
        dep_obj = Department.objects.get(id = dep_id)
        team_obj = TeamLead.objects.get(id = team_id)

        obj_emp = Employee()
        obj_emp.name = ename
        obj_emp.designation = designation
        obj_emp.department = dep_obj
        obj_emp.teamlead = team_obj
        obj_emp.save()
        context = {
            'dep_qs' : dep_qs,
            'team_tq' : team_tq,
            'result' : 'Record inserted'
        }
        return render(request,'student_temp/add_employee.html', context)

    context = {
        'dep_qs' : dep_qs,
        'team_tq' : team_tq,
    }
    return render(request,'student_temp/add_employee.html', context)

def del_view(request):
    emp_id = request.GET.get('empid')
    emp_obj = Employee.objects.get(id=emp_id)
    emp_obj.delete()
    
    dep_qs = Department.objects.all()
    emps = Employee.objects.filter(department__id=1)
    context = {
        'emps' : emps,
        'deparments' : dep_qs
    }
    return render(request,'student_temp/emps.html',context)


def more_details_view(request):
    emp_id = request.GET.get('id')
    emp_obj = Employee.objects.get(id=emp_id)
    context = {
    'emp' : emp_obj,
    }
    return render(request,'student_temp/details.html',context)

def update_view(request):
    emp_id = request.GET.get('i')
    emp_obj = Employee.objects.get(id=emp_id)
    context = {
    'emp' : emp_obj,
    }
    return render(request,'student_temp/update.html',context)

def logout_view(request):
    logout(request)
    return redirect('../login')
    








