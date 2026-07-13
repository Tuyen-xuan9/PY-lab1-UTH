"""Bài 5: Loại bỏ từ trùng lặp, sắp xếp, viết hoa từ bắt đầu bằng a/A."""


def xu_ly_chuoi():
    chuoi_nhap = input("Nhập một chuỗi có khoảng cách: ")

    # Tách chuỗi thành danh sách các từ và loại bỏ các từ trùng lặp
    danh_sach_tu = list(set(chuoi_nhap.split()))

    # Sắp xếp danh sách từ theo thứ tự bảng chữ cái
    danh_sach_tu.sort()
    for idx in range(len(danh_sach_tu)):
        # Nếu từ bắt đầu bằng chữ "A" hoặc "a", chuyển thành chữ in hoa
        if danh_sach_tu[idx][0].lower() == "a":
            danh_sach_tu[idx] = danh_sach_tu[idx].upper()

    print("Danh sách từ sau khi xử lý:")
    for tu in danh_sach_tu:
        print(tu)


def run():
    print("=== Bài 5: Xử lý chuỗi từ ===")
    xu_ly_chuoi()


if __name__ == "__main__":
    run()
