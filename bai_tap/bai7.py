"""Bài 7: Tìm số chính phương trong [100, 2000] có ít nhất 2 chữ số chẵn."""


def la_so_chinh_phuong(so):
    can_bac_hai = int(so ** 0.5)
    return can_bac_hai * can_bac_hai == so


def dem_chu_so_chan(so):
    dem = 0
    for chu_so in str(so):
        if int(chu_so) % 2 == 0:  # Kiểm tra nếu chữ số là số chẵn
            dem += 1
    return dem


def run():
    print("=== Bài 7: Số chính phương có ít nhất 2 chữ số chẵn ===")
    danh_sach_so = []

    # Duyệt qua các số trong đoạn từ 100 đến 2000
    for so in range(100, 2001):
        if la_so_chinh_phuong(so) and dem_chu_so_chan(so) >= 2:
            danh_sach_so.append(str(so))

    print(",".join(danh_sach_so))


if __name__ == "__main__":
    run()
