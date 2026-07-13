"""Bài 14: Từ điển Anh-Việt đơn giản dùng dictionary."""

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def load_data(file_path):
    dictionary = {}
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                english, vietnamese = line.split(':', 1)
                dictionary[english] = vietnamese
    return dictionary


def save_data(file_path, dictionary):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        for english, vietnamese in dictionary.items():
            file.write(f"{english}:{vietnamese}\n")


def add_word(dictionary):
    english = input("Nhập từ tiếng Anh: ").strip()
    if english in dictionary:
        print("Từ này đã tồn tại trong từ điển.")
    else:
        vietnamese = input("Nhập nghĩa tiếng Việt: ").strip()
        dictionary[english] = vietnamese
        print("Đã thêm từ thành công!")


def lookup_word(dictionary):
    english = input("Nhập từ tiếng Anh cần tra cứu: ").strip()
    if english in dictionary:
        print(f"Nghĩa của từ '{english}' là: {dictionary[english]}")
    else:
        print("Không tìm thấy từ này trong từ điển.")


def delete_word(dictionary):
    english = input("Nhập từ tiếng Anh cần xóa: ").strip()
    if english in dictionary:
        del dictionary[english]
        print("Đã xóa từ thành công!")
    else:
        print("Không tìm thấy từ này trong từ điển.")


def display_all_words(dictionary):
    if dictionary:
        print("Danh sách các từ trong từ điển:")
        for english, vietnamese in dictionary.items():
            print(f"{english}: {vietnamese}")
    else:
        print("Từ điển hiện đang trống.")


def main():
    file_path = os.path.join(DATA_DIR, "dictionary.txt")
    dictionary = load_data(file_path)

    while True:
        print("\n--- TỪ ĐIỂN ANH-VIỆT ---")
        print("1. Load data from file")
        print("2. Add a new word")
        print("3. Look up the meaning of a word")
        print("4. Delete a word from dictionary")
        print("5. Display all words in the dictionary")
        print("6. Exit")
        choice = input("Chọn một tùy chọn (1-6): ").strip()

        if choice == '1':
            dictionary = load_data(file_path)
            print("Dữ liệu đã được tải thành công!")
        elif choice == '2':
            add_word(dictionary)
        elif choice == '3':
            lookup_word(dictionary)
        elif choice == '4':
            delete_word(dictionary)
        elif choice == '5':
            display_all_words(dictionary)
        elif choice == '6':
            save_data(file_path, dictionary)
            print("Dữ liệu đã được lưu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


def run():
    print("=== Bài 14: Từ điển Anh-Việt ===")
    main()


if __name__ == "__main__":
    run()
