class Database:
    def __init__(self):
        self.data = {}
    
    def add_user(self, username, password):
        self.data[username] = password



class User:
    """
    Класс пользователя содержащийатрибуты: пароль и логин
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password



if  __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Выберите действие: \n1 - Вход\n2 - Регистрация\n3 - Выход\n'))
        
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ') 
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                else:
                    print('Неверный пароль.')
            else:
                print('Пользователь не найден.') 

        if choice == 2:
            user = User(input('Введите логин: '), password1 := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if password1 != password2:
                print('Пароли не совпадают, попробуйте еще раз.')
                continue
            database.add_user(user.username, user.password)

        if choice == 3:
            exit()
        print(database.data)