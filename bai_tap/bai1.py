"""Bài 1: Tính số tiền thực lĩnh của nhân viên dựa trên số giờ làm và thù lao/giờ."""


def tinh_luong(gio_lam, thu_lao):
    gio_tieu_chuan = 40
    tien_thuc_linh = 0

    # Tính số tiền thực lĩnh
    if gio_lam <= gio_tieu_chuan:
        # Nếu số giờ làm không vượt chuẩn
        tien_thuc_linh = gio_lam * thu_lao
    else:
        # Nếu số giờ làm vượt chuẩn
        gio_vuot_chuan = gio_lam - gio_tieu_chuan
        tien_thuc_linh = (gio_tieu_chuan * thu_lao) + (gio_vuot_chuan * thu_lao * 1.5)

    return tien_thuc_linh


def run():
    print("=== Bài 1: Tính lương nhân viên ===")
    gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
    thu_lao = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

    tien_thuc_linh = tinh_luong(gio_lam, thu_lao)
    print(f"Số tiền thực lĩnh của nhân viên là: {tien_thuc_linh:.2f}")


if __name__ == "__main__":
    run()
