from wxpy import *

bot = Bot(cache_path=True)
#bot.file_helper.send('hello')
"""
tuling = Tuling(api_key='577cb440cd174aa5a732a0247815f2d3')
print('图灵机器人已经启动...')
my_friend = bot.friends().search('阿哩买买')[0]
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
embed()
"""
def send_msg(msg):
    my_friend = bot.friends().search('阿哩买买')[0]
    my_friend.send(msg)
