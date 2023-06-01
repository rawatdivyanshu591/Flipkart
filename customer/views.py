from django.shortcuts import render

#Create your Views here.
from rest_framework import status
from rest_framework.views import APIview
from rest_framework.response import response
from customer.serializers import*

#Create your Views here.
class GetCustomerView(APIview):
    def get(self,request):
        instance=Customers.objects.all()
        serializer=GetCustomerserializer(instance,many=True)
        return response(serializer.data)
    
    def post(self,request):
        parasm = request.data
        print("data",parasm)
        serializers=GetCustomerserializer(data=parasm)
        serializers.valid(raise_expectation=True)
        serializers.save()
        return response({"message":"Save succesfully"})
    
class CustomeradressSerializer(APIview):
        def get(self,request):
             instance=Customers.objects.all()
             serializer=CustomeradressSerializer(instance,many=True)
             return response(serializer.data)
    
class CustomerDetailAddressView(APIview):
    def get(self,request,pk):
         instance=Customers.objects.filter(id=pk)
         serializer=CustomerDetailAddressSerializer(instance,many=True)
         return response(serializer.data)
         

