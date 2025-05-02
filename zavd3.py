def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}

    try:
        with open(input_file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) > 0:
                    ip = parts[0]
                    if ip in allowed_ips:
                        if ip in ip_counts:
                            ip_counts[ip] += 1
                        else:
                            ip_counts[ip] = 1

        with open(output_file_path, 'w') as out_file:
            for ip, count in ip_counts.items():
                out_file.write(f"{ip} - {count}\n")

    except FileNotFoundError:
        print("Помилка: вхідний файл не знайдено.")
    except IOError:
        print("Помилка при читанні або записі файлу.")


allowed = ["192.168.0.1", "10.0.0.2"]
filter_ips("apache_logs.txt", "output.txt", allowed)
print("Фільтрація завершена. Дані записано у 'output.txt'")
