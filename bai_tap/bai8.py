"""Bài 8: Đếm số chữ hoa và chữ thường trong câu."""


def la_chu_hoa(ky_tu):
    return ky_tu.isalpha() and ky_tu.upper() == ky_tu


def la_chu_thuong(ky_tu):
    return ky_tu.isalpha() and ky_tu.lower() == ky_tu


def run():
    print("=== Bài 8: Đếm chữ hoa, chữ thường ===")
    cau = input("Hãy nhập một câu bất kỳ: ")

    # Sử dụng list comprehension để đếm chữ hoa và chữ thường
    chu_hoa = sum(1 for ky_tu in cau if la_chu_hoa(ky_tu))
    chu_thuong = sum(1 for ky_tu in cau if la_chu_thuong(ky_tu))

    print(f"Số lượng chữ hoa: {chu_hoa}")
    print(f"Số lượng chữ thường: {chu_thuong}")


if __name__ == "__main__":
    run()
