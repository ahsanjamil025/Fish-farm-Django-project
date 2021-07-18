from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Customers(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=200, null=True)
    Address = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="download (1).png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

#product by cart

    



class log_in(models.Model):
    username = models.CharField(max_length=35)
    password = models.CharField(max_length=35)
    email = models.CharField(max_length=50)
    identification = models.CharField(max_length=10)
    def __str__(self):
      return str(self.id)

class EmployeeBasicInfo(models.Model):
    names  = models.CharField(max_length=30) 
    last_name  = models.CharField(max_length=35)
    father_name  = models.CharField(max_length=35)
    date_of_birth = models.DateTimeField()
    sex = models.CharField(max_length=30) 
    married = models.CharField(max_length=30) 
    cnic = models.CharField(max_length=13,unique=True,blank=True)
    def __str__(self):
      return str(self.names)

class  EmployeeContactDetail(models.Model):
    employee_id =models.ForeignKey(EmployeeBasicInfo,on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    addres = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=30)
    phone_no_2 = models.CharField(max_length=30)
    landline = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class EmployeeSkill(models.Model):
    employee_id =models.ForeignKey(EmployeeBasicInfo,on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    other = models.CharField(max_length=100)    


class EmployeeQualification(models.Model):

    employee_id =models.ForeignKey(EmployeeBasicInfo,on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    other = models.CharField(max_length=100)


class Sell(models.Model):

    #Customer_id =models.ForeignKey(Customer,on_delete=models.CASCADE)
    employee_id =models.ForeignKey(EmployeeBasicInfo,on_delete=models.CASCADE)
    quantity = models.IntegerField() 
    price = models.DecimalField(max_digits=8, decimal_places=3)
    total = models.DecimalField(max_digits=8, decimal_places=3)
    entrytime = models.DateTimeField()

class About_us(models.Model):
    person_name = models.CharField(max_length=100) 
    Designation = models.CharField(max_length=100) 
    Person_image = models.ImageField(upload_to='images/')


class Feedback(models.Model):
    name = models.CharField(max_length=100) 
    
    Mobile = models.CharField(max_length=100) 
    Email = models.EmailField(max_length=100) 
    
    Feedback = models.CharField(max_length=1000) 

class Fish(models.Model):
    product_name = models.CharField(max_length=100) 
    price = models.CharField(max_length=100) 
    Product_image = models.ImageField(upload_to='images/')

class Product(models.Model):
    name = models.CharField(max_length=100) 
    price = models.CharField(max_length=100)
    Quantity = models.IntegerField(null=True)

    image = models.ImageField(upload_to='images/')


class Pagez(models.Model):
    page_name = models.CharField(max_length=100) 
    page_link = models.CharField(max_length=500)

class Address(models.Model):
    name = models.CharField(max_length=100) 
    Company_name = models.CharField(max_length=100)
    Street_address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100)

class About_Info(models.Model):
    basic_info = models.CharField(max_length=200) 
    detail_info = models.CharField(max_length=500)

class Req_info(models.Model):
    status=models.CharField(max_length=255, default='Pending')
    CustomerID = models.IntegerField( null=True)
    Name_Costomer=models.CharField(max_length=255, null=True)
    Postal_Address=models.CharField(max_length=500, null=True)
    GrandTotal=models.FloatField(  null=True,default='0.00' )

class OrdereProduct(models.Model):
    order = models.ForeignKey(Req_info, on_delete=models.CASCADE)
    CustomerID = models.IntegerField( null=True)
    Name_Costomer=models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity= models.FloatField()

    def __str__(self):
        return str(self.order)