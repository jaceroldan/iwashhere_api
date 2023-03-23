from django.contrib.auth.models import User

from rest_framework import serializers

from api.models import Customer, Order


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'contact_number',
            'date_created'
        )


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = (
            'date_created',
            'customer',
            'weight',
            'remarks',
            'service_cost',
            'detergent_cost',
            'fabcon_cost',
            'bleach_cost',
            'plastic_cost',
            'payment_method',
            'payment_made',
            'date_required',
            'date_claimed'
        )
