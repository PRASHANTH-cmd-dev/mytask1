from django.db import models

# Create your models here.

class Customer(models.Model):          
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, editable=False, default=0.00)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    