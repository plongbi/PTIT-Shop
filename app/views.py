from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
import json,random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def product(request):
    return render(request, 'app/product.html')

def payment(request):
    user = request.user
    checkout_data = request.session.get('checkout_data')
    message = None

    if user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = 0

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        if request.user.is_authenticated:
            order.complete = True
            order.save()
            message = "Thanh toán thành công! Cảm ơn bạn đã mua hàng."
        else:
            message = "Vui lòng đăng nhập để hoàn tất thanh toán."
    
    return render(request, 'app/payment.html', {
        'checkout_data': checkout_data,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'message': message,
    })





def introduce(request):
    context = {}
    return render(request, 'app/introduce.html', context)

def detail(request, id):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    product = get_object_or_404(Product, id=id)
    categories = Category.objects.filter(is_sub=False)

    # ✅ Lấy các category của sản phẩm
    product_categories = product.category.all()

    # ✅ Lấy các sản phẩm liên quan từ các category đó
    related_products = Product.objects.filter(
        category__in=product_categories
    ).exclude(id=product.id).distinct()[:4]

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'categories': categories,
        'products': [product],  # dùng trong for loop
        'related_products': related_products,  # nếu bạn dùng để gợi ý
    }
    return render(request, 'app/detail.html', context)

def category(request):
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')
    category_obj = None
    products = []

    if active_category:
        category_obj = get_object_or_404(Category, slug=active_category)
        products = Product.objects.filter(category=category_obj)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'categories': categories,'products': products,'active_category': active_category,'category_obj': category_obj,'cartItems': cartItems}
    return render(request, 'app/category.html', context)

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')

    # Lấy tất cả sản phẩm và tính toán giảm giá ngẫu nhiên cho từng sản phẩm
    products = Product.objects.all()

    # Sắp xếp các sản phẩm theo thứ tự ngẫu nhiên
    products = list(products)  
    random.shuffle(products)  

    for product in products:
        product.discount_percent = random.randint(10, 70)  # Giảm giá ngẫu nhiên từ 10% đến 70%
        product.sale_price = int(product.price * (1 - product.discount_percent / 100))

    flash_sale_products = products[:6]  # Chọn 6 sản phẩm đầu tiên từ danh sách

    context = {
        'products': products,
        'flash_sale_products': flash_sale_products,
        'cartItems': cartItems,
        'categories': categories,
        'active_category': active_category,
    }
    return render(request, 'app/home.html', context)

def search(request):
    searched = ""
    keys = []
    if request.method == 'POST':
        # searched = request.POST['searched']
        # keys = Product.objects.filter(name__icontains=searched)
        searched = request.POST['searched'].strip().lower()  # Chuyển tất cả về chữ thường
        keys = Product.objects.filter(name__icontains=searched)  # Lọc sản phẩm với từ khóa không phân biệt hoa thường
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub =False)
    products = Product.objects.all()
    return render(request,'app/search.html',{'searched':searched,'keys':keys,'products': products,'cartItems':cartItems,'categories':categories})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context= {'form':form}
    return render(request,'app/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Tên người dùng hoặc mật khẩu không chính xác!')
    
    return render(request, 'app/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}  # Tránh lỗi khi truy cập các thuộc tính trong template
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub =False)
    context = {'items':items,'order':order,'cartItems':cartItems,'categories':categories}
    return render(request, 'app/cart.html', context)


def checkout(request):
    user = request.user
    items = []  # Danh sách sản phẩm nếu người dùng không đăng nhập
    order = None

    if user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=user, complete=False)
        items = order.orderitem_set.all()

    # Kiểm tra khi có request method là POST
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        number = request.POST.get('number')

        # Kiểm tra xem thông tin cá nhân có đầy đủ không
        if not (name and email and address and number):
            messages.error(request, "Vui lòng điền đầy đủ thông tin cá nhân.")
            return redirect('checkout')

        # Lưu thông tin vào session (để chuyển sang payment)
        request.session['checkout_data'] = {
            'name': name,
            'email': email,
            'address': address,
            'number': number,
        }

        # Chuyển sang trang payment
        return redirect('payment')

    return render(request, 'app/checkout.html', {
        'items': items,
        'order': order,
    })






def updateItem(request):
    data = json.loads(request.body)
    productId = data.get('productId')
    action = data.get('action')

    try:
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    # Trả về phản hồi JSON với thông tin mới
    response_data = {
        'cartItems': order.get_cart_items,
        'cartTotal': order.get_cart_total,
    }
    return JsonResponse(response_data)


