from django.db import models
import django.utils.timezone
from customers.models import Customer
from products.models import Product


import random
import string

def generate_order_id():
    """Generate a random order ID consisting of letters and numbers."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=10))  # generates a 10-character order ID



class Sale(models.Model):
    date_added = models.DateTimeField(default=django.utils.timezone.now)
    customer = models.ForeignKey(
        Customer, models.DO_NOTHING, db_column='customer')
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax_percentage = models.FloatField(default=0)
    amount_payed = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    order_id = models.CharField(max_length=15, unique=True, blank=True, null=True)
    

    class Meta:
        db_table = 'Sales'

    def __str__(self) -> str:
        return "Sale ID: " + str(self.id) + " | Grand Total: " + str(self.grand_total) + " | Datetime: " + str(self.date_added)

    def sum_items(self):
        details = SaleDetail.objects.filter(sale=self.id)
        return sum([d.quantity for d in details])
    
    def save(self, *args, **kwargs):
        # Ensure order_id is set if not already set
        if not self.order_id:
            self.order_id = generate_order_id()
        super(Sale, self).save(*args, **kwargs)


class SaleDetail(models.Model):
    sale = models.ForeignKey(
        Sale, models.DO_NOTHING, db_column='sale')
    product = models.ForeignKey(
        Product, models.DO_NOTHING, db_column='product')
    price = models.FloatField()
    quantity = models.IntegerField()
    total_detail = models.FloatField()

    class Meta:
        db_table = 'SaleDetails'

    def __str__(self) -> str:
        return "Detail ID: " + str(self.id) + " Sale ID: " + str(self.sale.id) + " Quantity: " + str(self.quantity)
