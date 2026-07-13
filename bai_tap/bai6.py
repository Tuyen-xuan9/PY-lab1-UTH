"""Bài 6: Lọc các số nhị phân 4 chữ số chia hết cho 5."""


def chia_het_cho_5(so_nhi_phan):
    # Chuyển đổi số nhị phân sang số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    # Kiểm tra chia hết cho 5
    return so_thap_phan % 5 == 0


def run():
    print("=== Bài 6: Lọc số nhị phân chia hết cho 5 ===")
    chuoi_nhi_phan = input("Nhập các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")

    # Tách chuỗi thành danh sách các số nhị phân
    danh_sach_nhi_phan = chuoi_nhi_phan.split(',')

    # Lọc ra các số nhị phân chia hết cho 5
    ket_qua = [so for so in danh_sach_nhi_phan if chia_het_cho_5(so)]

    print("Các số nhị phân chia hết cho 5 là:", ','.join(ket_qua))


if __name__ == "__main__":
    run()
