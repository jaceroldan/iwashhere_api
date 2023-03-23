from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import CustomerSerializer, OrderSerializer

from api.models import Customer, Order

class CustomerViewSet(viewsets.ModelViewSet):
    """
    /api/customers/
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """
    /api/orders/
    """

    queryset = Order.objects.all() 
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
