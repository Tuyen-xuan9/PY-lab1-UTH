"""Bài 10: Loại bỏ các bài hát trùng lặp trong danh sách nghe nhạc."""

import os

# Thư mục chứa dữ liệu (input/output) nằm cùng cấp với thư mục bai_tap
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def remove_duplicate_songs(input_file, output_file):
    """
    Đọc danh sách bài hát từ file input, loại bỏ bài hát trùng lặp và ghi vào file output.
    """
    try:
        # Đọc file và loại bỏ trùng lặp
        with open(input_file, 'r', encoding='utf-8') as f:
            songs = f.readlines()

        # Loại bỏ khoảng trắng thừa và trùng lặp (giữ thứ tự xuất hiện đầu tiên)
        unique_songs = list(dict.fromkeys(song.strip() for song in songs if song.strip()))

        # Ghi danh sách không trùng lặp vào file mới
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(unique_songs))

        print(f"Đã xử lý xong! Danh sách bài hát không trùng lặp được lưu tại: {output_file}")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {input_file}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


def dam_bao_file_mau(input_file):
    """Nếu file input mẫu chưa tồn tại, tạo file mẫu để demo (giống dữ liệu gốc trong lab)."""
    if not os.path.exists(input_file):
        os.makedirs(os.path.dirname(input_file), exist_ok=True)
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("Go Go\nMic Drop\nDNA\nFire\nGo Go\nDNA\n")


def run():
    print("=== Bài 10: Loại bỏ bài hát trùng lặp ===")
    input_file = os.path.join(DATA_DIR, 'danhsach_baihat.txt')
    output_file = os.path.join(DATA_DIR, 'danhsach_khongtrunglap.txt')

    dam_bao_file_mau(input_file)
    remove_duplicate_songs(input_file, output_file)


if __name__ == "__main__":
    run()
