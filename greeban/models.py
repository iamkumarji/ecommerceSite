from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, default="")
    product_category = models.CharField(max_length=50, default="")
    product_description = models.CharField(max_length=5000, default="")
    product_price = models.IntegerField(default=0)
    product_listed_date = models.DateField()
    product_quantity = models.IntegerField(default=0)
    product_quantity_per_serving_gms = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='greeban/images', default="")
    product_prof_image = models.ImageField(upload_to='greeban/images', default="")
    product_cart_image = models.ImageField(upload_to='greeban/images', default="")

    '''def __str__(self):
        return self.product_name + str(self.id)'''

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_categories():
        return Product.objects.values_list('product_category', flat=True).distinct()

    @staticmethod
    def get_product_by_category(category):
        if category:
            return Product.objects.filter(product_category=category)
        else:
            return Product.objects.all()


class OTP(models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=12, unique=True)
    generated_OTP = models.IntegerField(default=000000)
    received_OTP = models.IntegerField(default=000000)

    def __str__(self):
        return self.mobile


class UserData(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True)
    mobile_no = models.IntegerField(default=000000)
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=255, default="")
    pin = models.IntegerField(default=000000)
    state = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


'''class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    mobile = models.ForeignKey(OTP, on_delete=models.CASCADE)
    itemsAndQuantity = PickledObjectField()
    price = PickledObjectField()
    total_amount = models.FloatField(default=0.0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.id'''

'''class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserData, models.CASCADE)


class CartItem(models.Model):
    cart_item_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, models.CASCADE)
    cart_id = models.ForeignKey(Cart, models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    discount = models.IntegerField(default=0)'''


class Order(models.Model):

    transaction_status_values = (
        ('Initiated', 'In progress'),
        ('created', 'Transaction Created'),
        ('Success', 'Transaction Completed'),
        ('failed', 'Transaction Failed')
    )

    order_id = models.IntegerField(primary_key=True, default=0)
    user_id = models.ForeignKey(UserData, on_delete=models.CASCADE, default=0)
    order_date = models.DateTimeField()
    total_amount = models.IntegerField(default=0)
    transaction_id = models.CharField(default='', max_length=100, unique=True)
    transaction_status = models.CharField(
        max_length=20,
        default='',
        choices=transaction_status_values
        )
    name = models.CharField(max_length=40, default="")
    contactNo = models.CharField(max_length=10, default="")
    emailId = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=40, default="")
    state = models.CharField(max_length=30, default="")
    pinCode = models.CharField(max_length=7, default="")


    def __str__(self):
        return str(self.order_id)


class OrderDetails(models.Model):
    order_details_id = models.IntegerField(primary_key=True, default=1)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, default=0)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.order_id)

class Promotions(models.Model):
    promocode_id = models.IntegerField(primary_key=True, default=0)
    promocode = models.CharField(max_length=20, default=0)
    discount_percent = models.IntegerField(default=0)
    times_used = models.IntegerField(default=1)
    influencer_email = models.CharField(max_length=50, default="")
    def __str__(self):
        return str(self.promocode)
