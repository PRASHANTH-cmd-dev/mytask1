from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Customer
from django.db.models import Q



# Create your views here.

def prashanth(request):
    template=loader.get_template("homepage.html")
    return HttpResponse(template.render({},request))

def index(request):
    return render(request,"index.html")

def addrecordpage(request):
    return render(request,"addrecord.html")

def addrecorddb(request):
    if request.method == "POST":
        ct=request.POST.get("customer_id")
        nm=request.POST.get("name")
        em=request.POST.get("email")
        ph=request.POST.get("phone")
        ad=request.POST.get("address")
        qt = int(request.POST.get("quantity"))
        pr = float(request.POST.get("price"))
        
        total = qt*pr
        
        
        c1=Customer(
            customer_id=ct,
            name=nm,email=em,
            phone=ph,address=ad,
            quantity=qt,
            price=pr,
            total_amount=total)
        c1.save()
        
        return HttpResponse("""
                 <h2 style="color:green;">Record updated successfully!</h2>
                 <a href='/prashanth/'><button>Go to homepage</button></a>
                 """)
    
    
def displayrecordpage(request):
    mycustomer=Customer.objects.all()
    mycontext={'file':mycustomer}
    return render(request,"displayrecord.html",mycontext)

def onlyrecords(request):
    file = Customer.objects.all()
    return render(request, "onlyrecords.html", {"file": file})

    
    
def updaterecordpage(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, "updaterecord.html",{"customer":customer})

def updaterecorddb(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == "POST":
        
        customer.name = request.POST.get("name")
        customer.email = request.POST.get("email")
        customer.phone = request.POST.get("phone")
        customer.address = request.POST.get("address")
        customer.quantity = int(request.POST.get("quantity"))
        customer.price = float(request.POST.get("price"))
        customer.total_amount = customer.quantity * customer.price  # recalc
        customer.save()
        
        

        return HttpResponse("""
                 <h2 style="color:green;">Record updated successfully!</h2>
                 <a href='/prashanth/'><button>Go to homepage</button></a>
                 """)


    return HttpResponse("Invalid request method")
    



def deleterecordpage(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, "deleterecord.html", {"customer": customer})

def deleterecorddb(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return HttpResponse("""
                 <h2 style="color:green;">Record Deleted Succesfully!</h2>
                 <a href='/prashanth/'><button>Go to homepage</button></a>
                 """)


def searchrecordpage(request):
    query = request.GET.get("q")
    results = Customer.objects.all()
    if query:
        if query.isdigit():  
            
            results = Customer.objects.filter(customer_id=int(query))
            
    
                
            
        else:
    
            results = results.filter(
                Q(name__icontains=query) |
                Q(email__icontains=query) |
                Q(phone__icontains=query) 
                
            )
            
            
                 
                
        
    return render(request, "searchrecord.html", {"results": results, "query": query})
    