from django.contrib import admin

# Register your models here.
from productmanager.models import *

admin.site.register(CustomUserModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)