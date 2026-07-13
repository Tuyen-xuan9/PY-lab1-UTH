"""Bài 13: Chương trình quản lý sinh viên đơn giản dùng list."""

danh_sach_sinh_vien = []


def them_sinh_vien():
    print("=== Thêm sinh viên mới ===")
    mssv = input("Nhập MSSV: ")
    ho_ten = input("Nhập họ và tên: ")
    try:
        diem = float(input("Nhập điểm số: "))
        danh_sach_sinh_vien.append({"mssv": mssv, "ho_ten": ho_ten, "diem": diem})
        print("Thêm sinh viên thành công!")
    except ValueError:
        print("Điểm số phải là một số!")


def hien_thi_danh_sach():
    print("=== Danh sách sinh viên ===")
    if not danh_sach_sinh_vien:
        print("Danh sách trống!")
    else:
        for sv in danh_sach_sinh_vien:
            print(f"MSSV: {sv['mssv']}, Họ tên: {sv['ho_ten']}, Điểm: {sv['diem']}")


def hien_thi_sinh_vien_diem_cao():
    print("=== Danh sách sinh viên có điểm > 7 ===")
    sinh_vien_diem_cao = [sv for sv in danh_sach_sinh_vien if sv["diem"] > 7]
    if not sinh_vien_diem_cao:
        print("Không có sinh viên nào có điểm > 7!")
    else:
        for sv in sinh_vien_diem_cao:
            print(f"MSSV: {sv['mssv']}, Họ tên: {sv['ho_ten']}, Điểm: {sv['diem']}")


def tim_kiem_sinh_vien():
    print("=== Tìm kiếm sinh viên ===")
    mssv = input("Nhập MSSV cần tìm: ")
    ket_qua = next((sv for sv in danh_sach_sinh_vien if sv["mssv"] == mssv), None)
    if ket_qua:
        print(f"Tìm thấy: MSSV: {ket_qua['mssv']}, Họ tên: {ket_qua['ho_ten']}, Điểm: {ket_qua['diem']}")
    else:
        print("Không tìm thấy sinh viên!")


def cap_nhat_diem():
    print("=== Cập nhật điểm số của sinh viên ===")
    mssv = input("Nhập MSSV cần cập nhật điểm: ")
    for sv in danh_sach_sinh_vien:
        if sv["mssv"] == mssv:
            try:
                diem_moi = float(input("Nhập điểm mới: "))
                sv["diem"] = diem_moi
                print("Cập nhật điểm thành công!")
                return
            except ValueError:
                print("Điểm số phải là một số!")
                return
    print("Không tìm thấy sinh viên!")


def xoa_sinh_vien():
    print("=== Xóa sinh viên ===")
    mssv = input("Nhập MSSV cần xóa: ")
    for sv in danh_sach_sinh_vien:
        if sv["mssv"] == mssv:
            danh_sach_sinh_vien.remove(sv)
            print("Xóa sinh viên thành công!")
            return
    print("Không tìm thấy sinh viên!")


def menu():
    while True:
        print("\n=== Hệ thống quản lý sinh viên ===")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Hiển thị sinh viên có điểm > 7")
        print("4. Tìm kiếm sinh viên theo MSSV")
        print("5. Cập nhật điểm số sinh viên")
        print("6. Xóa sinh viên theo MSSV")
        print("7. Thoát chương trình")
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            them_sinh_vien()
        elif lua_chon == "2":
            hien_thi_danh_sach()
        elif lua_chon == "3":
            hien_thi_sinh_vien_diem_cao()
        elif lua_chon == "4":
            tim_kiem_sinh_vien()
        elif lua_chon == "5":
            cap_nhat_diem()
        elif lua_chon == "6":
            xoa_sinh_vien()
        elif lua_chon == "7":
            print("Goodbye!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")


def run():
    print("=== Bài 13: Quản lý sinh viên ===")
    menu()


if __name__ == "__main__":
    run()
