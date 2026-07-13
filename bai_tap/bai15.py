"""Bài 15: Xử lý mảng 2 chiều - tổng số nguyên tố, tổng đường chéo, vị trí min/max."""

import math


def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def tong_so_nguyen_to(matrix):
    tong = 0
    for hang in matrix:
        for phan_tu in hang:
            if la_so_nguyen_to(phan_tu):
                tong += phan_tu
    return tong


def tong_duong_cheo_chinh(matrix):
    n = len(matrix)
    tong = 0
    for i in range(n):
        tong += matrix[i][i]
    return tong


def tim_vi_tri_min_max(matrix):
    min_val = float('inf')
    max_val = float('-inf')
    vi_tri_min = (-1, -1)
    vi_tri_max = (-1, -1)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                vi_tri_min = (i, j)
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                vi_tri_max = (i, j)

    return vi_tri_min, vi_tri_max


def run():
    print("=== Bài 15: Xử lý mảng 2 chiều ===")
    so_hang = int(input("Nhập số hàng của mảng: "))
    so_cot = int(input("Nhập số cột của mảng: "))

    matrix = []
    print("Nhập các phần tử của mảng:")
    for i in range(so_hang):
        hang = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
        matrix.append(hang)

    # Tính tổng các số nguyên tố
    tong_nt = tong_so_nguyen_to(matrix)
    print(f"Tổng các số nguyên tố trong mảng: {tong_nt}")

    # Tính tổng đường chéo chính nếu là ma trận vuông
    if so_hang == so_cot:
        tong_cheo = tong_duong_cheo_chinh(matrix)
        print(f"Tổng đường chéo chính: {tong_cheo}")
    else:
        print("Không thể tính tổng đường chéo chính vì mảng không phải là ma trận vuông.")

    # Tìm vị trí của phần tử nhỏ nhất và lớn nhất
    vi_tri_min, vi_tri_max = tim_vi_tri_min_max(matrix)
    print(f"Vị trí phần tử nhỏ nhất: {vi_tri_min}")
    print(f"Vị trí phần tử lớn nhất: {vi_tri_max}")


if __name__ == "__main__":
    run()
