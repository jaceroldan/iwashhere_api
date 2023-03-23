from decimal import Decimal

from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Order(models.Model):
    UNPAID = 0
    CASH = 1
    GCASH = 2
    PAYMENT_METHOD_CHOICES = (
        (UNPAID, 'Unpaid'),
        (CASH, 'Cash'),
        (GCASH, 'GCash'),
    )

    date_created = models.DateTimeField()
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='orders')
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    remarks = models.TextField()
    service_cost = models.DecimalField(max_digits=8, decimal_places=2)
    detergent_cost = models.DecimalField(max_digits=8, decimal_places=2)
    fabcon_cost = models.DecimalField(max_digits=8, decimal_places=2)
    bleach_cost = models.DecimalField(max_digits=8, decimal_places=2)
    plastic_cost = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHOD_CHOICES, default=CASH)
    payment_made = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal(0.0))
    date_required = models.DateTimeField(null=True, blank=True)
    date_claimed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer}: {self.date_created}'

    @property
    def total_cost(self) -> Decimal:
        return (
            self.service_cost
            + self.detergent_cost
            + self.fabcon_cost
            + self.bleach_cost
            + self.plastic_cost
        )

    @property
    def payment_method_display(self) -> str:
        return self.get_payment_method_display()

    @property
    def payment_status(self) -> str:
        return (
            'Paid' if self.payment_made >= self.total_cost else 'Unpaid'
            + f' {self.payment_method_display}')
