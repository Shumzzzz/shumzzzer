import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from os import logggin, passs

login, password = str(logggin), str(passs)
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth()

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        msg = event.text.lower()
        if event.from_user and not (event.from_me):
            if msg == "1":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Здарова, Карл переехал в телеграм, вот ссылка: t.me/shumzzz !', 'random_id': 0})
            else:
            	vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Здарова, Карл переехал в телеграм, вот ссылка: t.me/shumzzz !', 'random_id': 0})