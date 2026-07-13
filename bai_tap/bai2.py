"""Bài 2: Nhập ngày tháng năm sinh, tính tuổi hiện tại."""

import datetime


def ngay_thang_nam_sinh():
    while True:
        try:
            ngay = int(input("Nhập ngày sinh (1-31): "))
            thang = int(input("Nhập tháng sinh (1-12): "))
            nam = int(input("Nhập năm sinh: "))
            ngay_sinh = datetime.datetime(nam, thang, ngay)
            return ngay_sinh
        except ValueError:
            print("Ngày tháng năm không hợp lệ. Vui lòng nhập lại!")


def tinh_tuoi(ngay_sinh):
    # Lấy ngày hiện tại
    ngay_hien_tai = datetime.datetime.now()
    # Tính tuổi
    tuoi = ngay_hien_tai.year - ngay_sinh.year - (
        (ngay_hien_tai.month, ngay_hien_tai.day) < (ngay_sinh.month, ngay_sinh.day)
    )
    return tuoi


def run():
    print("=== Bài 2: Tính tuổi từ ngày tháng năm sinh ===")
    print("Nhập ngày tháng năm sinh của bạn")
    ngay_sinh = ngay_thang_nam_sinh()

    print(f"Tuổi của bạn là: {tinh_tuoi(ngay_sinh)}")


if __name__ == "__main__":
    run()
