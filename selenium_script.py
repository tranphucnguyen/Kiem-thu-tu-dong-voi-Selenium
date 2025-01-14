from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = r"C:\Webdrive\chromedriver.exe"
login_page_path = r"file:///D:/python/login.html"  # Đảm bảo đường dẫn chính xác

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Danh sách các test case
test_cases = [
    {"email": "", "password": "", "expected_error": "Vui lòng nhập email và mật khẩu!"},
    {"email": "test", "password": "123", "expected_error": "Email không hợp lệ!"},
    {"email": "wrong@example.com", "password": "123", "expected_error": "Email hoặc mật khẩu không chính xác!"},
    {"email": "test@gmail.com", "password": "wrongpassword", "expected_error": "Email hoặc mật khẩu không chính xác!"},
    {"email": "test@gmail.com", "password": "123", "expected_error": "Email và mật khẩu đúng!"},
    {"email": "unknown@example.com", "password": "123", "expected_error": "Email hoặc mật khẩu không chính xác!"},  # Tài khoản không tồn tại
    {"email": "test@gmail.com", "password": "wrongpassword", "expected_error": "Email hoặc mật khẩu không chính xác!"},  # Thử với mật khẩu sai nhiều lần
]


try:
    for case in test_cases:
        print(f"Running test case: {case}")

        # Mở lại trang login
        driver.get(login_page_path)

        # Nhập thông tin email và mật khẩu
        driver.find_element(By.ID, "email").clear()  # Xóa dữ liệu cũ
        driver.find_element(By.ID, "email").send_keys(case["email"])
        driver.find_element(By.ID, "password").clear()  # Xóa dữ liệu cũ
        driver.find_element(By.ID, "password").send_keys(case["password"])
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(2)  # Đợi trang tải hoặc thông báo hiển thị

        try:
            # Lấy thông báo lỗi
            error_message = driver.find_element(By.ID, "errorMsg")
            print(f"Error message displayed: {error_message.text}")

            # Kiểm tra thông báo lỗi hiển thị
            assert error_message.is_displayed(), f"Không có thông báo lỗi: {case}"
            assert error_message.text == case["expected_error"], f"Lỗi sai nội dung: {case}"
            print(f"Test case {case} passed.")
        except Exception as case_error:
            print(f"Test case failed: {case}, Error: {case_error}")

except Exception as e:
    print(f"An error occurred during execution: {e}")

finally:
    # Đảm bảo luôn đóng trình duyệt
    driver.quit()
