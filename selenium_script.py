from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Nhập đường dẫn tới ChromeDriver và file login.html
chrome_driver_path = r"C:\Webdrive\chromedriver.exe"
login_page_path = r"file:///D:/python/login.html"  # Đảm bảo đường dẫn chính xác
success_page_path = r"file:///D:/python/success.html"  # Đảm bảo đường dẫn chính xác

# Nhập tên đăng nhập và mật khẩu từ người dùng
email_input = input("Nhập email: ")
password_input = input("Nhập mật khẩu: ")

# Khởi tạo Service cho ChromeDriver
service = Service(chrome_driver_path)

# Khởi tạo WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Mở trang login
    driver.get(login_page_path)

    # Kiểm tra nếu không nhập email hoặc mật khẩu
    if not email_input or not password_input:
        print("Email hoặc mật khẩu không được bỏ trống!")
    else:
        # Nhập email và mật khẩu vào các trường
        driver.find_element(By.ID, "email").send_keys(email_input)
        driver.find_element(By.ID, "password").send_keys(password_input)

        # Nhấn nút Đăng nhập
        driver.find_element(By.ID, "loginBtn").click()

        # Chờ một chút để trang web có thể xử lý
        time.sleep(2)

        # Kiểm tra nếu trang chuyển hướng thành công
        if driver.current_url == success_page_path:
            print("Đăng nhập thành công và chuyển đến success.html!")

        # Kiểm tra nếu có thông báo lỗi
        else:
            try:
                error_message = driver.find_element(By.ID, "errorMsg")
                if error_message.is_displayed():
                    print("Lỗi: " + error_message.text)
                else:
                    print("Không có thông báo lỗi.")
            except:
                print("Không tìm thấy thông báo lỗi.")

    # Kiểm tra trường hợp email sai
    driver.get(login_page_path)  # Quay lại trang login
    driver.find_element(By.ID, "email").send_keys("wrong@example.com")
    driver.find_element(By.ID, "password").send_keys(password_input)
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(2)

    # Kiểm tra nếu có thông báo lỗi khi nhập sai email
    if driver.current_url == login_page_path:
        try:
            error_message = driver.find_element(By.ID, "errorMsg")
            if error_message.is_displayed():
                print("Thông báo lỗi với email sai: " + error_message.text)
            else:
                print("Không có thông báo lỗi với email sai.")
        except:
            print("Không có thông báo lỗi với email sai.")

    # Kiểm tra trường hợp mật khẩu sai
    driver.get(login_page_path)  # Quay lại trang login
    driver.find_element(By.ID, "email").send_keys(email_input)
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(2)

    # Kiểm tra nếu có thông báo lỗi khi nhập sai mật khẩu
    if driver.current_url == login_page_path:
        try:
            error_message = driver.find_element(By.ID, "errorMsg")
            if error_message.is_displayed():
                print("Thông báo lỗi với mật khẩu sai: " + error_message.text)
            else:
                print("Không có thông báo lỗi với mật khẩu sai.")
        except:
            print("Không có thông báo lỗi với mật khẩu sai.")

    # Kiểm tra trường hợp cả email và mật khẩu đều sai
    driver.get(login_page_path)  # Quay lại trang login
    driver.find_element(By.ID, "email").send_keys("wrong@example.com")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(2)

    # Kiểm tra nếu có thông báo lỗi khi nhập cả email và mật khẩu sai
    if driver.current_url == login_page_path:
        try:
            error_message = driver.find_element(By.ID, "errorMsg")
            if error_message.is_displayed():
                print("Thông báo lỗi với cả email và mật khẩu sai: " + error_message.text)
            else:
                print("Không có thông báo lỗi với cả email và mật khẩu sai.")
        except:
            print("Không có thông báo lỗi với cả email và mật khẩu sai.")

finally:
    driver.quit()
