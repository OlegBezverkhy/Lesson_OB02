class User:
    def __init__(self, user_id, name,access_level='user'):
        self.__name_name = name
        self.__user_id = user_id
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_user_name(self):
        return self.__name_name

    def get_user_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.__users_list = []

    def add_user(self, user):
       if isinstance(user, User):
           self.__users_list.append(user)
           print(f'User {user.get_user_name()} добавлен')
       else:
           print('Invdalid user object')

    def remove_user(self, user_id):
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                print(f'User {user.get_user_name()} удален')
                return
        print('User не найден')

    def display_user_list(self):
        print('Список пользователей:')
        for user in self.__users_list:
            print(f'ID пользователя: {user.get_user_id()} '
                  f'Имя пользователя: {user.get_user_name()} '
                  f'Уровень доступа пользователя: {user.get_user_access_level()}')


# Проверяем
# Создаем пользователей
admin = Admin('001', 'Иван')
user1 = User('002', 'Василий')
user2 = User('003', 'Петр')
user3 = User('004', 'Митрофан')

# Добавляем пользователей в список
print ('Добавление новых пользователей:')
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Выведем список полльзователей:

admin.display_user_list()
# Методы унаследованные от класса User вполне работают
print('Список администраторов:')
print(f'Администратор ID: {admin.get_user_id()} '
      f'Администратор Name: {admin.get_user_name()} '
      f'Администратор - уровень доступа: {admin.get_user_access_level()}')

# Удаление пользователя
print('Удаление пользователей')
admin.remove_user('003')
admin.display_user_list()

