"""Bài 11: Đọc file nhật ký giao dịch ngân hàng, tính số dư thực tế."""

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def xu_ly_giao_dich(ten_file_giao_dich, ten_file_so_du):
    try:
        # Mở file giao dịch để đọc
        with open(ten_file_giao_dich, 'r', encoding='utf-8') as file_giao_dich:
            giao_dich = file_giao_dich.readlines()

        so_du = 0

        for dong in giao_dich:
            dong = dong.strip()  # Loại bỏ khoảng trắng thừa
            if dong.startswith("D"):
                so_tien = int(dong.split()[1])
                so_du += so_tien  # Cộng vào số dư
            elif dong.startswith("W"):
                so_tien = int(dong.split()[1])
                phi = so_tien * 0.001  # Tính phí rút tiền (0.1%)
                so_du -= (so_tien + phi)  # Trừ số tiền và phí khỏi số dư

        # Ghi kết quả vào file số dư
        with open(ten_file_so_du, 'w', encoding='utf-8') as file_so_du:
            file_so_du.write(f"Số dư hiện tại: {int(so_du)} VNĐ\n")

        print("Đã xử lý giao dịch và ghi kết quả vào file thành công.")
    except FileNotFoundError:
        print("Không tìm thấy file giao dịch. Vui lòng kiểm tra lại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


def dam_bao_file_mau(ten_file_giao_dich):
    """Nếu file giao dịch mẫu chưa tồn tại, tạo file mẫu để demo."""
    if not os.path.exists(ten_file_giao_dich):
        os.makedirs(os.path.dirname(ten_file_giao_dich), exist_ok=True)
        with open(ten_file_giao_dich, 'w', encoding='utf-8') as f:
            f.write("Name: Tuyen\nD 500000\nW 150000\nW 50000\nW 132000\nD 110000\n")


def run():
    print("=== Bài 11: Xử lý giao dịch ngân hàng ===")
    ten_file_giao_dich = os.path.join(DATA_DIR, "Transaction.txt")
    ten_file_so_du = os.path.join(DATA_DIR, "BalanceInquiry.txt")

    dam_bao_file_mau(ten_file_giao_dich)
    xu_ly_giao_dich(ten_file_giao_dich, ten_file_so_du)


if __name__ == "__main__":
    run()
