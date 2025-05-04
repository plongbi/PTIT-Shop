**Backend**: Django, Python
**Database**: SQLite
**Frontend**: HTML, CSS, JavaScript, Bootstrap


## Cấu trúc dự án

```
PTIT-Shop/
│
├── app/                            # Ứng dụng chính của dự án
│   ├── migrations/                 # Các file migration của database
│   ├── static/                     # Static files (CSS, JS, Images)
│   │   ├── app/
│   │   │   ├── css/                # CSS files
│   │   │   ├── images/             # Image files
│   │   │   └── js/                 # JavaScript files
│   │   └── assets/                 # Các tài nguyên khác
│   │
│   ├── templates/                  # Template HTML files
│   │   └── app/
│   │       ├── base.html           # Template cơ sở
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
│   ├── admin.py                    # Cấu hình admin panel
│   ├── apps.py                     # Cấu hình app
│   ├── models.py                   # Định nghĩa models
│   ├── urls.py                     # URL routing của app
│   ├── views.py                    # Logic xử lý views
│   └── tests.py                    # Unit tests
│
├── media/                          # Media files uploaded
│
├── webbanhang/                     # Cấu hình chính của dự án
│   ├── __init__.py
│   ├── asgi.py                     # ASGI config
│   ├── settings.py                 # Cài đặt dự án
│   ├── urls.py                     # URL routing chính
│   └── wsgi.py                     # WSGI config
│
├── db.sqlite3                      # SQLite database
├── manage.py                       # Quản lý dự án Django
├── requirements.txt                # Các thư viện cần thiết
└── README.md                       # Thông tin dự án
```

## Các chức năng chính

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
