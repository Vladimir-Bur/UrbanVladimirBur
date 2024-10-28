import time

class User:
    nickname = None
    password = None
    age = 0

    def __init__(self, nickname : str, password, age : int):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    title = None
    duration = None

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        Video.title = self.title
        self.duration = duration
        Video.duration = self.duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user = User.nickname

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = password

        if self.nickname in UrTube.users:
            UrTube.current_user = self.nickname
        else:
            print(f'Вы не зарегистрированы в системе.')

        if hash(self.password) == User.password:
            User.nickname = self.nickname
        else:
            print(f'Введен неверный пароль')
            UrTube.log_out(self.nickname)

    def register(self, nickname, password, age):
        self.nickname = nickname
        User.nickname = self.nickname
        self.password = password
        User.password = hash(self.password)
        self.age = age
        User.age = self.age

        if self.nickname not in UrTube.users:
            UrTube.users.append(self.nickname)
            UrTube.log_in(self, nickname, password)
        else:
            print(f"Пользователь '{self.nickname}' уже существует.")

    def log_out(self):
        UrTube.current_user = None

    def add(self, *args):
        for arg in args:
            self.arg = arg
            if self.arg.title not in UrTube.videos:
                UrTube.videos.append(self.arg.title)
            else:
                continue

    def get_videos(self, text):
        get_result =[]
        self.text = text
        for video in UrTube.videos:
            if video.lower().__contains__(self.text.lower()):
                get_result.append(video)
            else:
                continue
        return get_result

    def watch_video(self, title):
        self.title = title

        if UrTube.current_user not in UrTube.users:
            print(f'Войдите в аккаунт, чтобы смотреть видео')

        elif User.age < 18:
                print(f'Вам нет 18 лет, пожалуйста покиньте страницу')

        else:
            if self.title in UrTube.videos:
                video_time = []
                for t in range(1, Video.duration + 2):
                    time.sleep(1)
                    if t == Video.duration + 1:
                        video_time.append('Конец видео')
                    else:
                        video_time.append(t)
                    print('\r', *video_time, end="")
                print('')
                video_time.clear()


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

