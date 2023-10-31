import json
import csv


def json_to_csv(json_file):
    # Открываем JSON файл для чтения
    with open(json_file, 'r', encoding='utf-8') as json_f:
        data = json.load(json_f)

    csv_name = str(list(data.keys())[0])
    csv_filename = csv_name + '.csv'

    data = list(data.values())[0]

    # Открываем CSV файл для записи
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_f:
        csv_writer = csv.writer(csv_f)    # содаём переменную связанную с файлом

        csv_writer.writerow(data[0].keys())  # запись заголовков
        for record in data:
            csv_writer.writerow(record.values())


json_filename = input("Введите имя JSON файла: ")
json_to_csv(json_filename)
