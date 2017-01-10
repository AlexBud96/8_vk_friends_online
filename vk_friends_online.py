import vk
import getpass

APP_ID = 5816289


def get_user_login():
    login = input('Введите ваш логин VK: ')
    return login


def get_user_password():
    password = getpass.getpass('Введите пароль в ВК: ')
    return password


def get_online_friends(login, password):

    session = vk.AuthSession(
         app_id=APP_ID,
         user_login=login,
         user_password=password,
         scope='friends'
     )
    api = vk.API(session)
    friends = api.friends.getOnline()
    if not friends:
        return []
    else:
        users_information = api.users.get(user_ids=friends)
        return users_information


def output_friends_to_console(friends_online):
    if friends_online:
        print('друзья онлайн : ')
        for friend in friends_online:
            print (friend['first_name'],friend['last_name'])
    else:
        print('Никто из ваших друзей не онлайн')

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)