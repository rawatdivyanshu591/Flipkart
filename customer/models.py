from django.db import models

#Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=15,null=True,blank=True)
    last_name = models.CharField(max_length=15,null=True,blank=True)
    mobile_no = models.IntegerField(max_length=15,null=True,blank=True)
    address_name = models.CharField(max_length=15,null=True,blank=True)
    age = models.IntegerField(max_length=15,null=True,blank=True)
    country_name = models.CharField(max_length=15,null=True,blank=True)
    city_name = models.CharField(max_length=15,null=True,blank=True)
    dob = models.DateField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.first_name
class CustomerAddress(models.Model):
    customer=models.ForeignKey (Customers,on_delete=models.CASCADE,null=True,related_name="customer_addresses")
    street_name=models.CharField( max_length=15,null=True,blank=True)
    city_name=models.CharField (max_length=15,null=True,blank=True)
    state_name=models.CharField (max_length=15,null=True,blank=True)
    country_name=models.CharField (max_length=15,null=True,blank=True)
    pincode=models.IntegerField (max_length=15,null=True,blank=True)


    def __str__(self):
        return str(self.street_name)
    
class CustomerAdhar(models.Model):
        customer=models.OneToOneField(Customers,on_delete=models.CASCADE)
        adhar_no=models.IntegerField(null=True,blank=True)
        adhar_name=models.CharField(max_length=15,null=True,blank=True)
        adhar_adress=models.CharField(max_length=15,null=True,blank=True)
        
        def __str__(self):
            return str(self.adhar_name)


