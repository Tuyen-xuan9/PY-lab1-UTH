#!/usr/bin/env python3
"""
LAB 1: NGỮ NGHĨA CÚ PHÁP LẬP TRÌNH PYTHON
Chương trình menu chính để chạy 15 bài tập trong Lab 1.

Chạy: python main.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bai_tap import (
    bai1, bai2, bai3, bai4, bai5,
    bai6, bai7, bai8, bai9, bai10,
    bai11, bai12, bai13, bai14, bai15,
)


# ===== Màu sắc ANSI cho giao diện console =====
class Mau:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"


DANH_SACH_BAI = [
    ("1", "Tính lương nhân viên (giờ làm & thù lao)", bai1.run),
    ("2", "Tính tuổi từ ngày tháng năm sinh", bai2.run),
    ("3", "In dãy số bình phương tích lũy", bai3.run),
    ("4", "In bảng cửu chương", bai4.run),
    ("5", "Xử lý chuỗi từ (loại trùng, sắp xếp, viết hoa)", bai5.run),
    ("6", "Lọc số nhị phân 4 chữ số chia hết cho 5", bai6.run),
    ("7", "Tìm số chính phương có ít nhất 2 chữ số chẵn", bai7.run),
    ("8", "Đếm chữ hoa / chữ thường trong câu", bai8.run),
    ("9", "Định dạng chuỗi (viết hoa đầu từ)", bai9.run),
    ("10", "Loại bỏ bài hát trùng lặp (đọc/ghi file)", bai10.run),
    ("11", "Xử lý giao dịch ngân hàng (đọc/ghi file)", bai11.run),
    ("12", "Kiểm tra username & password hợp lệ", bai12.run),
    ("13", "Quản lý sinh viên (CRUD với list)", bai13.run),
    ("14", "Từ điển Anh - Việt (dictionary)", bai14.run),
    ("15", "Xử lý mảng 2 chiều (số nguyên tố, đường chéo, min/max)", bai15.run),
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def in_header():
    print(f"{Mau.CYAN}{Mau.BOLD}")
    print("╔" + "═" * 62 + "╗")
    print("║" + " LAB 1: NGỮ NGHĨA CÚ PHÁP LẬP TRÌNH PYTHON".center(62) + "║")
    print("╚" + "═" * 62 + "╝")
    print(Mau.RESET)


def in_menu():
    print(f"{Mau.YELLOW}{Mau.BOLD}DANH SÁCH BÀI TẬP:{Mau.RESET}\n")
    for ma, mo_ta, _ in DANH_SACH_BAI:
        so = f"{Mau.GREEN}{ma:>2}{Mau.RESET}"
        print(f"  [{so}] {mo_ta}")
    print()
    print(f"  [{Mau.MAGENTA}{Mau.BOLD} A{Mau.RESET}] Chạy TẤT CẢ các bài (lần lượt)")
    print(f"  [{Mau.RED}{Mau.BOLD} 0{Mau.RESET}] Thoát chương trình")
    print(f"\n{Mau.DIM}{'-' * 64}{Mau.RESET}")


def in_tieu_de_bai(ma, mo_ta):
    print(f"\n{Mau.BLUE}{Mau.BOLD}{'=' * 64}")
    print(f"  BÀI {ma}: {mo_ta}")
    print(f"{'=' * 64}{Mau.RESET}\n")


def cho_enter():
    input(f"\n{Mau.DIM}Nhấn Enter để quay lại menu...{Mau.RESET}")


def chay_bai(ma, mo_ta, ham_chay):
    clear_screen()
    in_tieu_de_bai(ma, mo_ta)
    try:
        ham_chay()
    except KeyboardInterrupt:
        print(f"\n{Mau.RED}Đã hủy bài tập.{Mau.RESET}")
    except Exception as e:
        print(f"\n{Mau.RED}Có lỗi xảy ra: {e}{Mau.RESET}")
    cho_enter()


def chay_tat_ca():
    for ma, mo_ta, ham_chay in DANH_SACH_BAI:
        chay_bai(ma, mo_ta, ham_chay)


def main():
    tra_cuu = {ma: (mo_ta, ham) for ma, mo_ta, ham in DANH_SACH_BAI}

    while True:
        clear_screen()
        in_header()
        in_menu()
        lua_chon = input(f"{Mau.WHITE}{Mau.BOLD}Nhập lựa chọn của bạn: {Mau.RESET}").strip().upper()

        if lua_chon == "0":
            print(f"\n{Mau.GREEN}Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!{Mau.RESET}\n")
            break
        elif lua_chon == "A":
            chay_tat_ca()
        elif lua_chon in tra_cuu:
            mo_ta, ham_chay = tra_cuu[lua_chon]
            chay_bai(lua_chon, mo_ta, ham_chay)
        else:
            print(f"{Mau.RED}Lựa chọn không hợp lệ! Vui lòng thử lại.{Mau.RESET}")
            input("Nhấn Enter để tiếp tục...")


if __name__ == "__main__":
    main()
