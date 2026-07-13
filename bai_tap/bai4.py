"""Bài 4: In bảng cửu chương từ 2 đến 9."""


def in_bang_cuu_chuong():
    for x in range(2, 10):
        for t in range(2, 10):
            # In ra kết quả của phép nhân
            print(f"{x} x {t} = {x * t}", end="\t")
        # Xuống dòng sau mỗi lần in hết 1 dòng
        print()


def run():
    print("=== Bài 4: Bảng cửu chương ===")
    in_bang_cuu_chuong()


if __name__ == "__main__":
    run()
