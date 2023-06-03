from rest_framework import serializers
from customer.models import*

class GetCustomerserializer(serializers.ModalSerializer):
    class Meta:
        model = Customers
        fields="__all__"


class CustomerAddressSerializer(serializers.ModalSerializer):
    class Meta:
        model = CustomerAddress
        fields="__all__"


class CustomerDetailAddressSerializer(serializers.ModelSerializer):
    related_name=CustomerAddressSerializer
    class Meta:
        model = Customers
        feilds = ('first_name,last_name,mobile_no,address_name,age,country_name,city_name,dob')