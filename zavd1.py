def analyze_log_file(log_file_path):
    codes = {}

    try:
        with open(log_file_path, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) > 8:
                    code_str = parts[8]
                    if code_str.isdigit():
                        code = int(code_str)
                        if code in codes:
                            codes[code] += 1
                        else:
                            codes[code] = 1
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except IOError:
        print("Помилка: не вдалося прочитати файл.")

    return codes


log_path = "apache_logs.txt"
result = analyze_log_file(log_path)
print("Результати аналізу лог-файлу:")
print(result)
