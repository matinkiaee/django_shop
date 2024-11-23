from django.db import models
from shop.models import Product
from account.models import ShopUser



# Create your models here.

class Order(models.Model):
    buyer = models.ForeignKey(ShopUser, related_name='orders', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11,verbose_name="تلفن")
    address = models.CharField(max_length=250,verbose_name="ادرس")
    postal_code = models.CharField(max_length=10,verbose_name="کد پستی")
    province = models.CharField(max_length=50, verbose_name="استان")
    city = models.CharField(max_length=50,verbose_name="شهر")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False,verbose_name="پرداخت")

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'


    def __str__(self):
        return f"order {self.id}"


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())






class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0,verbose_name="قیمت")
    quantity = models.PositiveIntegerField(default=1,verbose_name="تعداد")


    class Meta:
        verbose_name = 'آیتم سفارش'
        verbose_name_plural = 'آیتم های سفارش'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


    
    
