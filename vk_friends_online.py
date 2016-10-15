import vk


APP_ID = 5661578  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input("Логин: ")
    return login


def get_user_password():
    password = input("Пароль: ")
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends = api.friends.get(fields=["online"])
    friends_online = []
    for friend in friends:
        if friend["online"] == 1:
            friends_online.append(friend)
    return friends_online


def output_friends_to_console(friends_online):
    print("Сейчас онлайн {0:d} человек:".format(len(friends_online)))
    for friend in friends_online:
        print("  {0:s} {1:s}".format(friend["first_name"], friend["last_name"]))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        pass
    except:
        print("ОШИБКА! Проверьте подключение к интернету и попробуйте еще раз.")