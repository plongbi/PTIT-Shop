Frontend: HTML, CSS, JavaScript, Bootstrap
Backend: Django
Database: SQlite

##Cấu trúc dự án

PTIT-Shop/
│
├── app/                            # Ứng dụng chính của dự án
│   ├── migrations/                 # Các file migration của database
│   ├── static/                     # Static (CSS, JS, Images)
│   │   ├── app/
│   │   │   ├── css/                # CSS 
│   │   │   ├── images/             # Image 
│   │   │   └── js/                 # JavaScript 
│   │   └── assets/                 # Các tài nguyên khác
│   │
│   ├── templates/                  # HTML
│   │   └── app/
│   │       ├── base.html           # Cơ sở
│   │       ├── home.html           # Trang chủ
│   │       ├── detail.html         # Chi tiết sản phẩm
│   │       ├── cart.html           # Giỏ hàng
│   │       ├── checkout.html       # Thanh toán
│   │       ├── payment.html        # Xác nhận thanh toán
│   │       ├── login.html          # Đăng nhập
│   │       ├── register.html       # Đăng ký
│   │       ├── search.html         # Tìm kiếm
│   │       ├── category.html       # Danh mục sản phẩm
│   │       └── introduce.html      # Giới thiệu
│   │
│   ├── admin.py                    # Admin panel
│   ├── apps.py                     # App
│   ├── models.py                   # Models
│   ├── urls.py                     # URL 
│   ├── views.py                    # Views
│   └── tests.py                    # Tests
│
├── media/                          # Media 
│
├── webbanhang/                     # Cấu hình chính của dự án
│   ├── __init__.py
│   ├── asgi.py                     # ASGI config
│   ├── settings.py                 # Cài đặt dự án
│   ├── urls.py                     # URL chính
│   └── wsgi.py                     # WSGI config
│
├── db.sqlite3                      # SQLite database
├── manage.py                       # Quản lý dự án Django

##Các chức năng chính
1. **Hệ thống xác thực người dùng**
   - Đăng ký
   - Đăng nhập
   - Đăng xuất

2. **Quản lý sản phẩm**
   - Danh sách sản phẩm
   - Chi tiết sản phẩm với nhiều hình ảnh
   - Tìm kiếm sản phẩm
   - Phân loại sản phẩm theo danh mục

3. **Giỏ hàng và thanh toán**
   - Thêm sản phẩm vào giỏ hàng
   - Cập nhật số lượng
   - Xóa sản phẩm khỏi giỏ hàng
   - Quy trình thanh toán
   - Xác nhận thanh toán

4. **Quản lý đơn hàng**
   - Tạo đơn hàng
   - Quản lý trạng thái đơn hàng
