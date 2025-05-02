import hashlib

def generate_file_hashes(*file_paths):
    result = {}

    for path in file_paths:
        try:
            with open(path, 'rb') as file:
                file_content = file.read()
                hash_value = hashlib.sha256(file_content).hexdigest()
                result[path] = hash_value
        except FileNotFoundError:
            print(f"Помилка: файл {path} не знайдено.")
        except IOError:
            print(f"Помилка: не вдалося прочитати файл {path}.")

    return result


hashes = generate_file_hashes("file1.txt", "file2.txt")
print("Хеші файлів:")
for path, hash_code in hashes.items():
    print(path, "=>", hash_code)
