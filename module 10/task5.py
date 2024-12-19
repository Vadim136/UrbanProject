import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
            

# Список названий файлов
filenames = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']


# Линейный вызов
if __name__ == '__main__':
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейный вызов: {time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))}")

# # Многопроцессный вызов
# if __name__ == '__main__':
#     start_time = time.time()
#     with Pool() as pool:
#         pool.map(read_info, filenames)
#     end_time = time.time()
#     print(f"Многопроцессный вызов: {time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))}")


"""
Линейный вызов: 00:00:05
Многопроцессный вызов: 00:00:02
"""