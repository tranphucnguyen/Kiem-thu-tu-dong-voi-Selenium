# Selenium Automation Script
## Giới thiệu
Mỗi sinh viên dùng câu nhắc sau để có bài tập riêng của mình tương tự mẫu này (Liên kết đến một trang bên ngoài.). Có thể chọn ngôn ngữ lập trình khác.
"Cho tôi một bài tập cho sinh viên học môn kiểm thử về kiểm thử tự động với selenium"
## Mô tả bài toán
Dự án này sử dụng **Selenium** để tự động hóa quá trình đăng nhập vào một trang web (login.html). Mục tiêu là kiểm tra tính năng đăng nhập bằng cách xử lý các trường hợp sau:

1. **Form đăng nhập**:
   - Người dùng nhập tài khoản và mật khẩu vào form đăng nhập
   ![image](https://github.com/user-attachments/assets/e1ca7ee6-ff0c-48de-bac2-12e37a0e25a2)
3. **Đăng nhập thành công**:
   - Người dùng nhập đúng email và mật khẩu hợp lệ, hệ thống chuyển hướng tới `success.html`.
   ![image](https://github.com/user-attachments/assets/49802591-4158-4e18-bce9-eac7f016d02e)
   ![image](https://github.com/user-attachments/assets/7274eb46-33d6-45bb-921b-991398f20241)
    
3. **Xử lý selenium**:
   ![image](https://github.com/user-attachments/assets/5befde2b-f8f4-45a9-896b-dd4ae702645f)
   ![image](https://github.com/user-attachments/assets/80d67268-335d-4dd2-b5ec-04974efdb25b)
   ![image](https://github.com/user-attachments/assets/2f8e73d5-b63b-4e65-b796-2115d9723b45)

## Kết quả thực nghiệm
![image](https://github.com/user-attachments/assets/afeac55c-7c94-4794-b8da-75f5740d05a5)

## Công nghệ sử dụng
- **Python 3.12**: Ngôn ngữ lập trình chính.
- **Selenium**: Thư viện tự động hóa trình duyệt.
- **ChromeDriver**: Công cụ điều khiển trình duyệt Google Chrome.
- **HTML**: Giao diện đơn giản để thực hiện bài toán.

## Cấu trúc dự án
```plaintext
D:/python/
│
├── login.html          # Trang đăng nhập
├── success.html        # Trang chuyển hướng khi đăng nhập thành công
├── selenium_script.py  # Mã nguồn chính cho tự động hóa
└── README.md           # Tài liệu mô tả bài toán
