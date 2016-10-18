from getpass import getpass

import vk
from vk.exceptions import VkAuthError
from requests.exceptions import ConnectionError

APP_ID = 5661578  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input("Логин: ")
    return login


def get_user_password():
    password = getpass(prompt="Пароль: ")
    return password


def get_online_friends(login, password):
    vk.logger.disabled = True
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends = api.friends.get(fields=["online"])
    friends_online = filter(lambda friend: True if friend["online"] == 1 else False, friends)
    return friends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("  {0:s} {1:s}".format(friend["first_name"], friend["last_name"]))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except VkAuthError:
        print("ОШИБКА! Неправильный логин или пароль.")
    except ConnectionError:
        print("ОШИБКА! Проверьте подключение к интернету и попробуйте еще раз.")