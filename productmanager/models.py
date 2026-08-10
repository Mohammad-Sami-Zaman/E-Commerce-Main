from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# full_name, username, email, password, role (Admin / Seller / Customer)
class CustomUserModel(AbstractUser):
    role_type = [
        ('Admin' , 'Admin'),
        ('Seller' , 'Seller'),
        ('Customer' , 'Customer'),     
    ]
    
    full_name = models.CharField(max_length= 100, null= True)
    role = models.CharField(choices=role_type, null= True)

    def __str__(self):
        return f'{self.username} --- {self.role}'
    
# category_name, description, created_at
class CategoryModel(models.Model):

    user = models.ForeignKey(CustomUserModel, on_delete= models.CASCADE, null=True)
    category_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.category_name} --- {self.created_at}'
    

# seller (ForeignKey to CustomUserModel), category (ForeignKey to CategoryModel), product_name,
# product_description, product_image, price, stock_quantity, created_at 

class ProductModel(models.Model):

    seller = models.ForeignKey(CustomUserModel, on_delete= models.CASCADE, null=True)
    category = models.ForeignKey(CategoryModel, on_delete= models.CASCADE, null=True)
    product_name = models.CharField(max_length=100, null=True)
    product_description = models.TextField(null=True)
    product_image = models.ImageField(upload_to='products/', null=True)
    price = models.PositiveIntegerField(null=True)
    stock_quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name} --- {self.category}'

    


# customer (ForeignKey to CustomUserModel), product (ForeignKey to ProductModel), quantity,
# total_price, order_status (Pending / Confirmed / Cancelled), ordered_at 

class OrderModel(models.Model):
    order_type = [
        ('Pending' , 'Pending'),
        ('Confirmed' , 'Confirmed'),
        ('Cancelled' , 'Cancelled'),     
    ]


    customer = models.ForeignKey(CustomUserModel, on_delete= models.CASCADE, null=True)
    product = models.ForeignKey(ProductModel, on_delete= models.CASCADE, null=True)
    total_price = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    order_status = models.CharField(choices=order_type, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} --- {self.order_status}'
