# Selenium Automation Script
## Giới thiệu
Mỗi sinh viên dùng câu nhắc sau để có bài tập riêng của mình tương tự mẫu này (Liên kết đến một trang bên ngoài.). Có thể chọn ngôn ngữ lập trình khác.
"Cho tôi một bài tập cho sinh viên học môn kiểm thử về kiểm thử tự động với selenium"
## Mô tả bài toán
Dự án này sử dụng **Selenium** để tự động hóa quá trình đăng nhập vào một trang web (login.html). Mục tiêu là kiểm tra tính năng đăng nhập bằng cách xử lý các trường hợp sau:
## 2.Các bài kiểm thử: 
- Kiểm thử không nhập email và password
- Kiểm thử nhập sai email
- Kiểm thử nhập sai password
- Kiểm thử nhập sai email và password
- Kiểm thử nhập đúng email và password
- Kiểm thử với tài khoản không tồn tại
- Kiểm thử với  mật khẩu sai nhiều lần
1. **Form đăng nhập**:
   - Người dùng nhập tài khoản và mật khẩu vào form đăng nhập
   ![image](https://github.com/user-attachments/assets/8ba70dd0-731a-4d12-bba7-3b73a74bce43)
   ![image](https://github.com/user-attachments/assets/6db74c11-3de1-470c-bb08-3d9768dc0318)

3. **Đăng nhập thành công**:
   - Người dùng nhập đúng email và mật khẩu hợp lệ, hệ thống chuyển hướng tới `success.html`.
   ![image](https://github.com/user-attachments/assets/49802591-4158-4e18-bce9-eac7f016d02e)
   ![image](https://github.com/user-attachments/assets/7274eb46-33d6-45bb-921b-991398f20241)
    
3. **Xử lý selenium**:
   ![image](https://github.com/user-attachments/assets/ac60429e-68a3-4b47-bda2-730b247a6cbb)


## Kết quả thực nghiệm
![Uploading image.png…]()



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
## Đường dẫn Chatgpt
https://chatgpt.com/share/67868065-593c-8006-83ca-531a740079f8
