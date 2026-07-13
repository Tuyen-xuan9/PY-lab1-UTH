"""Bài 3: In ra dãy các số bình phương tích lũy từ 1 đến 9."""


def in_day_so():
    day_so = []
    # Vòng lặp từ 1 đến 9
    for v in range(1, 10):
        day_so.append(v * v)
        # In danh sách hiện tại
        print(day_so)


def run():
    print("=== Bài 3: In dãy số bình phương ===")
    in_day_so()


if __name__ == "__main__":
    run()
