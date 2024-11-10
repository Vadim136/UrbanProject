import json
import time

class Database:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add_user(self, username, password_hash, age):
        self.data[username] = {'password_hash': password_hash, 'age': age}
        self.save_data()

class VideoDatabase:
    def __init__(self, filename='video.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add_video(self, title, duration, adult_mode, time_now=0):
        self.data.append({
            'title': title,
            'duration': duration,
            'adult_mode': adult_mode,
            'time_now': time_now
        })
        self.save_data()

class User:
    """
    Класс пользователя содержащий атрибуты: пароль и логин
    """

    def __init__(self, username, password, password_confirm, age):
        self.username = username
        if password == password_confirm:
            self.password_hash = self.__hash__(password)
        else:
            raise ValueError("Пароли не совпадают")
        self.age = age

    def __hash__(self, password):
        return hash(password)

class Video:
    """
    Класс видео содержащий атрибуты: название, продолжительность, текущее время, режим 18+
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def to_dict(self):
        return {
            'title': self.title,
            'duration': self.duration,
            'time_now': self.time_now,
            'adult_mode': self.adult_mode
        }

    @staticmethod
    def from_dict(data):
        return Video(data['title'], data['duration'], data['time_now'], data['adult_mode'])

class UrTube:
    def __init__(self, video_filename='video.json'):
        self.users = []
        self.videos = self.load_videos(video_filename)
        self.current_user = None
        self.video_filename = video_filename

    def load_videos(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Video.from_dict(video_data) for video_data in data]
        except FileNotFoundError:
            return []

    def save_videos(self):
        with open(self.video_filename, 'w') as file:
            json.dump([video.to_dict() for video in self.videos], file)

    def log_in(self, nickname, password):
        password_hash = hash(password)
        for user in self.users:
            if user.username == nickname and user.password_hash == password_hash:
                self.current_user = user
                print(f'Вход выполнен, {nickname}')
                return
        print('Неверный логин или пароль.')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.username == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        user = User(nickname, password, password, age)
        self.users.append(user)
        self.current_user = user
        print(f'Пользователь {nickname} зарегистрирован и вошел в систему.')

    def log_out(self):
        self.current_user = None
        print('Выход выполнен.')

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
        self.save_videos()

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print('Видео не найдено.')
            return

        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу.')
            return

        print(f'Начало воспроизведения видео "{title}".')
        for i in range(video.time_now, video.duration):
            print(f'Воспроизведение на {i} секунде.')
            time.sleep(1)
        print('Конец видео.')
        video.time_now = 0
        self.save_videos()

if __name__ == '__main__':
    database = Database()
    video_database = VideoDatabase()
    urtube = UrTube()

    # Загрузка пользователей из базы данных
    for username, data in database.data.items():
        urtube.users.append(User(username, '', '', data['age']))
        urtube.users[-1].password_hash = data['password_hash']

    # Загрузка видео из базы данных
    urtube.videos = [Video.from_dict(video_data) for video_data in video_database.data]

    while True:
        choice = int(input('Выберите действие: \n1 - Вход\n2 - Регистрация\n3 - Выход\n4 - Добавить видео\n5 - Поиск видео\n6 - Смотреть видео\n7 - Выход\n'))

        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            urtube.log_in(login, password)

        if choice == 2:
            username = input('Введите логин: ')
            password1 = input('Введите пароль: ')
            password2 = input('Повторите пароль: ')
            age = int(input('Введите возраст: '))
            if password1 != password2:
                print('Пароли не совпадают, попробуйте еще раз.')
                continue
            urtube.register(username, password1, age)
            database.add_user(username, hash(password1), age)

        if choice == 3:
            urtube.log_out()

        if choice == 4:
            title = input('Введите название видео: ')
            duration = int(input('Введите продолжительность видео (в секундах): '))
            adult_mode = input('Видео 18+? (да/нет): ').lower() == 'да'
            video = Video(title, duration, adult_mode=adult_mode)
            urtube.add(video)
            video_database.add_video(title, duration, adult_mode)

        if choice == 5:
            search_word = input('Введите поисковое слово: ')
            videos = urtube.get_videos(search_word)
            if videos:
                print('Найденные видео:')
                for video in videos:
                    print(video)
            else:
                print('Видео не найдены.')

        if choice == 6:
            title = input('Введите название видео для просмотра: ')
            urtube.watch_video(title)

        if choice == 7:
            exit()

        print(database.data)
