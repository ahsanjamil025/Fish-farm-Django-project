
from django.db.models.fields import DecimalField
from django.db.models.fields.files import ImageField
from django.forms.forms import Form
from django.http.response import HttpResponse
from fishfarm.models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import smtplib, ssl
from email.mime.text import MIMEText
from .forms import *
from django.shortcuts import redirect, render
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


# Create your views here.
def index(request):
    p = Product.objects.all()
    add = Address.objects.all()
    extend={}
    if request.user.is_authenticated:
        extend = Customers.objects.get(user=request.user.id)

    return render(request,'index.html',{'product':p,'ad':add,'extend': extend})

@login_required(login_url="/users/login")
def eindex(request):
   
    max_val=Req_info.objects.latest('id')
    extend = Customers.objects.get(user=request.user.id)
    oders =Req_info.objects.all()
    pro = Product.objects.all()
    p=0
    d=0
    q=0
    for data in oders :
        if data.status=="Pending":
            p=p+1
        else:
            d=d+1
    for data in pro :
        q+=1
       


    return render(request,'ehome.html',{'oders': max_val,'pending': p,'deliver': d,'prot': q,'pro': pro,'extend': extend,})

def signin(request):
    if request.method=="POST":
        # Get the post parameters

        loginusername=request.POST['Username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            if user.groups.filter(name = "Employe").exists():
                return redirect("ehome")
            else:

                messages.success(request, "Successfully Logged In")
                return redirect("index")
        else:
           
            
            return redirect("signin")
    return render(request,'signin.html',)

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['Username']
        email=request.POST['Email']
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        pass1=request.POST['Password']
        pass2=request.POST['Confirm Password']

        # check for errorneous input
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('signup')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Fish Farm account has been successfully created")
        return redirect('signin')
    

    return render(request,'sign up.html')

def about(request):
    extend={}
    if request.user.is_authenticated:
        extend = Customers.objects.get(user=request.user.id)
    add = Address.objects.all()
    dataset = About_us.objects.all()
    datset = About_Info.objects.all()
    return render(request,'about.html',{'about':dataset,'info':datset,'ad':add,'extend': extend,})

def contact(request):
    extend={}
    if request.user.is_authenticated:
        extend = Customers.objects.get(user=request.user.id)
    add = Address.objects.all()
    if request.method == "POST":  
        name= request.POST['Name']
        no= request.POST['Mobile']
        email = request.POST['Email']
        mssg = request.POST['Message']
        print(name,no,email,mssg)
        ins=Feedback(name=name,Mobile=no,Feedback=mssg,Email=email)
        ins.save()

    return render(request,'contact.html',{'ad':add,'extend': extend,})



    
def feedback(request):
    extend = Customers.objects.get(user=request.user.id)
    dataset = Feedback.objects.all()
    return render(request,'feedback.html',{'feed':dataset,'extend': extend,})

def sell(request):
    extend = Customers.objects.get(user=request.user.id)
    dataset = OrdereProduct.objects.all()
    return render(request,'sell.html',{'sell':dataset,'extend': extend,})

def order(request):
    extend = Customers.objects.get(user=request.user.id)
    dataset = Req_info.objects.all()
    return render(request,'orders.html',{'order':dataset,'extend': extend,})


def edit(request , pk ):
    form1 = Req_info.objects.get(id=pk)
    item = form1.CustomerID

    name = form1.Name_Costomer
    email="empty"
    obj=User.objects.all()
    for val in obj:
        if val.username==name:
            email=val.email
            
            
    dataset = OrdereProduct.objects.all()   
    form = edit_form(instance=form1)

    if request.method == 'POST':
        form = edit_form(request.POST ,instance=form1)
        if form.is_valid:
            form.save()
            status = request.POST['status']
            if (status=='deliver' or status=='Deliver' or status=='deliverd' or status=='Deliverd') and (email !="empty"):
                sender = 'ahsanjamil025@gmail.com'
                receivers = [email]
                body_of_email = 'YOUR order has been recieve you will get soon!...\n Thanks for shoping'
                msg = MIMEText(body_of_email, 'html')
                msg['Subject'] = 'Oder recieved succesfully'
                msg['From'] = sender
                msg['To'] = ','.join(receivers)
                s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
                s.login(user = 'ahsanjamil025@gmail.com', password = 'jamil332')
                s.sendmail(sender, receivers, msg.as_string())
                s.quit()
                print("Email has been sent sucessfully!")

            redirect('order')
    
    return render(request,'manage.html',{'form1':form1,'id':pk,'Purchase':dataset,'email':email }) 

def promang(request , pk ):
    form1 = Product.objects.get(id=pk)

    
    form = edit_form1(instance=form1)

    if request.method == 'POST':
        form = edit_form1(request.POST ,instance=form1)
        if form.is_valid:
            form.save()
            messages.success(request, 'Updated')
            redirect('ehome')
    
    return render(request,'managep.html',{'form1':form1,}) 

def delete(request, pk):
    form= Feedback.objects.get(pk=pk)
    
    form.delete()
    return redirect('/components/') 

def Settings(request):
    add = Address.objects.all()
    form1 = User.objects.get(username=request.user)
    data = Customers.objects.get(user=request.user.id)
    form = Profile(instance=request.user)
    if request.method == 'POST':
        form = Profile(request.POST ,instance=request.user)
        if form.is_valid:
            form.save()    
    return render(request,'setting.html',{'ad':add,'form1':form1,'extend': data,})

def cSettings(request):
    add = Address.objects.all()
    
    
    extend = Customers.objects.get(user=request.user.id)
    extend1= Profileextend(request.POST, instance=extend)
    
    form = Profile(instance=request.user)
    if request.method == 'POST':
        form = Profileextend(request.POST,request.FILES, instance=extend)
        
        if form.is_valid:
            form.save()
        

        
    return render(request,'csetting.html',{'ad':add,'extend1': extend1,'extend': extend,})

def password(request):
    form1 = User.objects.get(username=request.user)
    data = Customers.objects.get(user=request.user.id)
    if request.method == "POST":
        password = request.POST['password']
        password1 = request.POST['password1']
        if password1== password:
            form1.set_password(password)
            form1.save()
    return render(request,'password.html',{'extend': data,})



def Logouts(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('signin')

#add to cart_view
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    total=0.00
    cart = Cart(request)
    
    ab=request.session['cart']
    print(ab)
    for key,value in ab.items():
        print(value['name'])
        total = float( float(value['price'])* float(value['quantity'])) + float(total)
    return render(request, 'cart.html',{'bill':total})


#....buy view
def store(request):
    total=0.00
    cart = Cart(request)
    
    ab=request.session['cart']
    #print(ab)
    for key,value in ab.items():
        print(value['name'])
        total = float( float(value['price'])* float(value['quantity'])) + float(total)

    #print(total) 
    address = request.POST['address']

    #print(request.user)
    instant=Req_info(CustomerID=value['userid'],Name_Costomer=request.user,Postal_Address=address,GrandTotal=total)
    instant.save()

    print(value['userid'])
    max_val=Req_info.objects.latest('id')
   # print(max_val)
    for key,value in ab.items():
        print(value['name'])
        
        
        OrdereProduct.objects.create(order=max_val,  CustomerID=value['userid'], Name_Costomer=request.user,  name=value['name'], quantity=value['quantity'], price=value['price'])
    
    cart.clear()
    

    return render(request, 'index.html', {'cart': cart})

@login_required(login_url="/users/login")
def deletecartitem(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect("cart_detail")

#....pdf

