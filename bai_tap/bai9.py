"""Bài 9: Định dạng chuỗi - bỏ khoảng trắng thừa, viết hoa đầu mỗi từ."""


def dinh_dang_chuoi():
    chuoi_goc = input("Nhập vào một chuỗi bất kỳ: ")

    # Loại bỏ khoảng trắng thừa ở đầu và cuối
    chuoi_da_xu_ly = ' '.join(chuoi_goc.split())

    # Định dạng mỗi từ: chữ cái đầu in hoa, các chữ còn lại in thường
    chuoi_dinh_dang = ' '.join([tu.capitalize() for tu in chuoi_da_xu_ly.split()])

    print("Chuỗi sau khi định dạng:", chuoi_dinh_dang)


def run():
    print("=== Bài 9: Định dạng chuỗi ===")
    dinh_dang_chuoi()


if __name__ == "__main__":
    run()
