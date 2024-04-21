import json
import requests
import os
import hashlib

# Создаем множества для лога успешно и неуспешно скачанных и проигнорированных файлов
successful_downloads = set()
unsuccessful_downloads = set()
ignored_downloads = set()

def download_files_from_json(file_location, server):
    """
    Функция скачивает файлы из JSON-файла с сервера

    file_location: Путь к папке, в которой будут храниться файлы
    server: Адрес сервера, с которого будут скачиваться файлы
    """
    # Получаем JSON-файлик с сервера
    json_data = requests.get('http://' + server + '/automodpack/')
    # Крадём из файла данные
    data = json_data.json()

    # Проходимся по всем файлам сервера
    for file_info in data['list']:
        # Создаём URL для скачивания файла
        url = 'http://' + server + '/automodpack/' + file_info['sha1']
        # Создаём путь к файлу
        filename = os.path.join(file_location, *file_info['file'].split('/'))
        # Проверяем, существует ли файл и совпадает ли его SHA1 с тем, что указан в JSON-файле
        # Если файл существует и его SHA1 совпадает, то пропускаем его
        print(f"Проверяю {file_info['file']}...")
        if os.path.exists(filename) and sha1_check(filename, file_info['sha1']):
            # Сообщаем о пропуске и добавляем в лог
            print(f"Файл {file_info['file']} уже существует и имеет правильный SHA1")
            ignored_downloads.add(filename)
            continue
        # Если файл не существует или его SHA1 не совпадает, то скачиваем его
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Качаю {file_info['file']}...")
            if not os.path.exists(os.path.dirname(filename)):
                # Создаём папки, если их нет
                os.makedirs(os.path.dirname(filename))
            with open(filename, 'wb') as f:
                # Запись файла
                f.write(response.content)
            # Проверяем, совпадает ли SHA1 скаченного файла с тем, что указан в JSON-файле
            if sha1_check(filename, file_info['sha1']):
                # Сообщаем об удачном скачивании и добавляем в лог
                print(f"Скачал {file_info['file']} удачно")
                successful_downloads.add(filename)
            else:
                # Сообщаем об неудачном скачивании и добавляем в лог
                print(f"Ошибка: SHA1 не совпадает для {file_info['file']} :(")
                unsuccessful_downloads.add(filename)
        else:
            # Сообщаем об неудачном скачивании и добавляем в лог
            print(f"Не удалось скачать {file_info['file']} :(")
            unsuccessful_downloads.add(filename)

def sha1_check(file_path, sha1_hash):
    """
    Проверяет, совпадает ли SHA1 файла с тем, что указан в JSON-файле
    
    file_path: Путь к файлу
    sha1_hash: SHA1, указанный в JSON-файле
    
    True, если совпадает
    False, если не совпадает
    """
    h = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            h.update(data)
    return h.hexdigest() == sha1_hash

server_IP = input("Айпи нужного майнкрафт-сервера: ")
# Specify the path to where downloaded files should be
mod_file_path = input('Путь куда скачать файлы (оставьте пустым чтобы скачать в папку с скриптом): ')
# Call the function to download files
script_dir = os.path.dirname(os.path.abspath(__file__))
if not mod_file_path:  # Check if the path is empty
    mod_file_path = script_dir

download_files_from_json(mod_file_path, server_IP)

# Записываем успешно, неуспешно и проигнорированные файлы в файл после завершения программы
with open('download_results.txt', 'wt') as log:
    log.writelines("Успешно скачанные файлы:\n")
    log.writelines([file + '\n' for file in successful_downloads])
    log.writelines("\nНеуспешно скачанные файлы:\n")
    log.writelines([file + '\n' for file in unsuccessful_downloads])
    log.writelines("\nПроигнорированные файлы:\n")
    log.writelines([file + '\n' for file in ignored_downloads])
    
# Выводим статистику скачивания
print(f"Статистика скачивания (подробнее см. лог в папке скрипта):")
print(f"Успешно скачано: {len(successful_downloads)} файлов")
print(f"Неуспешно скачано: {len(unsuccessful_downloads)} файлов")
print(f"Проигнорировано: {len(ignored_downloads)} файлов")

# Спрашиваем пользователя, хочет ли он удалить неуспешно скачанные файлы
delete_files = input("Хотите удалить неуспешно скачанные файлы? (да/нет): ")
if delete_files.lower() == 'да':
    for file in unsuccessful_downloads:
        os.remove(os.path.join(mod_file_path, file))