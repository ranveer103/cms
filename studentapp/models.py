from django.db import models

#  class StudentPersonalInfo(models.Model):
#     name =  models.CharField(max_length = 100, blank=True)
#     course = models.CharField(max_length = 50)
#     session = models.IntegerField()
#     father_name = models.CharField(max_length = 100,null=True)
#     date = models.DateField(null=True)
#     def __str__(self):
#         return self.father_name

# class StudentMarks(models.Model):
#     rollno =  models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50, unique=True)
#     marks = models.IntegerField(null=True)
#     course = models.CharField(max_length=100, default='python')
#     def __str__(self):
#         return self.name


#     class Meta:
#         db_table = 'marks_tbl'

# class EmployeeDetails(models.Model):
#     name = models.CharField(max_length= 100)
#     desigantion = models.CharField(max_length= 100)

#     def __str__(self):
#         return self.name
#     class Meta:
#         db_table = 'emp_details'
#         verbose_name_plural = 'Employee Details'

# class EmployeeSalary(models.Model):
#     emp_id = models.ForeignKey(EmployeeDetails,on_delete=models.CASCADE, primary_key=True)
#     salary = models.IntegerField()

#     def __str__(self):
#         return self.emp_id.name+' ' +self.emp_id.desigantion
#     class Meta:
#         db_table = 'emp_salary'
#         verbose_name_plural = 'Employee Salary'


class Department(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class TeamLead(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.name 

class Employee(models.Model):
    name = models.CharField(max_length=100)
    desigation = models.CharField(max_length=100)
    department = models.ForeignKey(Department,null=True, on_delete=models.CASCADE)
    teamlead = models.ForeignKey(TeamLead,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name  


 


