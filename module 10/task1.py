from time import sleep, time
from threading import Thread
import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time_functions = time()


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')


end_time_functions = time()


print(f"Работа функций: {datetime.timedelta(seconds=end_time_functions - start_time_functions)}")


start_time_threads = time()


thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = Thread(target=write_words, args=(100, 'example8.txt'))


thread1.start()
thread2.start()
thread3.start()
thread4.start()


thread1.join()
thread2.join()
thread3.join()
thread4.join()


end_time_threads = time()


print(f"Работа потоков: {datetime.timedelta(seconds=end_time_threads - start_time_threads)}")



"""
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа функций: 0:00:35.352971
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков: 0:00:20.781444
"""