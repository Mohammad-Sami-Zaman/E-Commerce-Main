from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from productmanager.models import *

def signup(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        full_name = req.POST.get('full_name')
        role = req.POST.get('role')
        email = req.POST.get('email')
        password = req.POST.get('password')
        password2 = req.POST.get('password2')

        user_exist = CustomUserModel.objects.filter(username = username).exists()
        if user_exist:
            messages.warning(req, 'Username Exist')
        
        if password == password2:
            CustomUserModel.objects.create_user(
                username= username,
                full_name = full_name,
                role = role,
                email= email,
                password=password
            )
            messages.success(req, 'Account Created Successfully')
            return redirect('login')
        else:
            messages.warning(req,'Password Does Not Match')
            return redirect('signup')
    return render(req, 'signup.html')


def login_page(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password = password)
        if user:
            login(req, user)
            messages.success(req, 'Login Successfully')
            return redirect('home')
        else:
            messages.warning(req, 'Invalid Indicator')
            return redirect('login')

    return render(req, 'login.html')


@login_required
def logout_page(req):
    logout(req)
    messages.success(req, 'Log Out successfully')
    return redirect('login')


@login_required
def profile(req):
    
    return render(req, 'home.html')

@login_required
def product_catagory(req):
    if req.user.role == 'Admin':
        data = CategoryModel.objects.filter(user = req.user)

        context = {
            'data' : data
        }

        return render(req, 'product_catagory.html', context)
    else:
        messages.warning(req, 'You are not admin')
        return redirect('home')
    
@login_required
def catagory_add(req):
    if req.method == 'POST':
        category_name = req.POST.get('category_name')
        description = req.POST.get('description')

        CategoryModel.objects.create(
            user = req.user,
            category_name = category_name,
            description = description
        )
        return redirect('product_catagory')
    return render(req, 'catagory_add.html')

@login_required
def catagory_edit(req, c_id):
    cat_data = CategoryModel.objects.get(id = c_id)
    if req.method == 'POST':
        category_name = req.POST.get('category_name')
        description = req.POST.get('description')

        cat_data.category_name = category_name
        cat_data.description = description

        cat_data.save()
        
        return redirect('product_catagory')
    
    context = {
        'cat_data' : cat_data
    }
    return render(req, 'catagory_edit.html', context)

@login_required
def catagory_delete(req, c_id):
    CategoryModel.objects.get(id = c_id).delete()
    return redirect('product_catagory')





@login_required
def product_list(req):
    
        Products = ProductModel.objects.all()

        context = {
            'Products' : Products
        }

        return render(req, 'product_list.html', context)

@login_required
def product_add(req):
    
    pro_catagory = CategoryModel.objects.all()
    if req.user.role == 'Seller':
        if req.method == 'POST':
            product_name = req.POST.get('product_name')
            product_description = req.POST.get('product_description')
            product_image = req.FILES.get('product_image')
            price = req.POST.get('price')
            stock_quantity = req.POST.get('stock_quantity')
            category = req.POST.get('category_name')
            category_name = CategoryModel.objects.get(id  =  category)
            ProductModel.objects.create(
                seller = req.user,
                category = category_name,
                product_name = product_name,
                product_description = product_description,
                product_image = product_image,
                price = price,
                stock_quantity = stock_quantity
            )

            return redirect('product_list')

        context = {
            
            'pro_catagory' : pro_catagory
        }

        return render(req, 'product_add.html', context)

   

@login_required
def product_delete(req, p_id):
        
        ProductModel.objects.get(id = p_id).delete()

        return redirect('product_list')


@login_required
def product_edit(req, p_id):
    Products = ProductModel.objects.get(id = p_id)
    pro_catagory = CategoryModel.objects.all()
    if req.user.role == 'Seller':
        if req.method == 'POST':
            product_name = req.POST.get('product_name')
            product_description = req.POST.get('product_description')
            product_image = req.FILES.get('product_image')
            price = req.POST.get('price')
            stock_quantity = req.POST.get('stock_quantity')
            category = req.POST.get('category_name')
            category_name = CategoryModel.objects.get(id  =  category)


            
            
            Products.category = category_name
            Products.product_name = product_name
            Products.product_description = product_description
            if product_image:
                Products.product_image = product_image
            Products.price = price
            Products.stock_quantity = stock_quantity
            Products.save()

            return redirect('product_list')

        context = {
            
            'pro_catagory' : pro_catagory,
            'Product' : Products
        }

        return render(req, 'product_edit.html', context)
    

@login_required
def product_buy(req, p_id):
    if req.user.role == 'Customer':
        Products = ProductModel.objects.get(id = p_id)
    
    
        if req.method == 'POST':
            
            quantity = int(req.POST.get('quantity'))
            order_status = req.POST.get('order_status')
            total_price = Products.price * quantity

            
            
            OrderModel.objects.create(
                customer = req.user,
                product = Products,
                quantity = quantity,
                
                order_status = order_status,
                total_price = total_price,
                
            )

            return redirect('order_list')

        context = {
            
            
            'Product' : Products
        }

        return render(req, 'product_buy.html', context)

    

@login_required
def order_list(req):
    if req.user.role == 'Customer':
        Orders = OrderModel.objects.filter(customer = req.user)

        context = {
            'Orders' : Orders
        }

        return render(req, 'order_list.html', context)
    

@login_required
def customer_list(req):
    if req.user.role == 'Admin':
        Users = CustomUserModel.objects.filter(role = 'Customer')

        context = {
            'Users' : Users
        }

        return render(req, 'customer_list.html', context)
    

@login_required
def seller_list(req):
    if req.user.role == 'Admin':
        Users = CustomUserModel.objects.filter(role = 'Seller')

        context = {
            'Users' : Users
        }

        return render(req, 'seller_list.html', context)
    
@login_required
def seller_product_list(req):
    if req.user.role == 'Seller':
        Products = ProductModel.objects.filter(seller = req.user)

        context = {
            'Products' : Products
        }

        return render(req, 'seller_product_list.html', context)