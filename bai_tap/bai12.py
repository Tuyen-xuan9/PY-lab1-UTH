"""Bài 12: Kiểm tra tính hợp lệ của username và password."""


def kiem_tra_username(username):
    # Username phải có đúng 6 ký tự và chỉ chứa chữ thường hoặc số
    return len(username) == 6 and username.isalnum() and username.islower()


def kiem_tra_password(password):
    # Password phải có độ dài từ 6 đến 12 ký tự
    if not (6 <= len(password) <= 12):
        return False
    # Kiểm tra các thành phần cần thiết trong password
    co_chu_thuong = any(c.islower() for c in password)
    co_chu_hoa = any(c.isupper() for c in password)
    co_so = any(c.isdigit() for c in password)
    co_ky_tu_dac_biet = any(c in "!@#$%^&*" for c in password)
    # Password hợp lệ nếu có đủ các thành phần trên
    return co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet


def run():
    print("=== Bài 12: Kiểm tra username & password ===")
    print("Chào mừng bạn đến với hệ thống đăng ký!")
    username = input("Nhập username (6 ký tự, chỉ gồm chữ thường và số): ")
    password = input("Nhập password (6-12 ký tự, bao gồm chữ thường, chữ hoa, số, ký tự đặc biệt): ")

    # Kiểm tra tính hợp lệ của username và password
    if not kiem_tra_username(username):
        print("Username không hợp lệ! Vui lòng thử lại.")
    elif not kiem_tra_password(password):
        print("Password không hợp lệ! Vui lòng thử lại.")
    else:
        print("Đăng ký thành công! Chào mừng,", username)


if __name__ == "__main__":
    run()
