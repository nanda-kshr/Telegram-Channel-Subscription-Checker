
from telethon import TelegramClient, events, Button
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import ChannelParticipantsRecent
import telebot
api_id = 12052562
api_hash = "apihash"
bot_token = "bottoken"
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

channel = "channelusername"
botykutty = telebot.TeleBot(bot_token)

@bot.on(events.NewMessage(incoming=True, pattern=r'\.channel'))
async def addChannel(event):
    global channel
    chat = await event.get_chat()
    chatid = chat.id
    reason = event.text[6:100]
    channel = reason
    await bot.send_message(chat,f"Successfully changed channel to `{channel}`")


@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def send(event):
    bot_chat = await event.get_chat()
    bot_pm_user_id = bot_chat.id
    user = await event.get_sender()
    first_name = user.first_name
    member = False
    print(str(botykutty.get_chat_member(channel,user).status))
    all_participants = []
    all_participants = await bot.get_participants(channel, aggressive=True)
    user_list = bot.iter_participants(entity=channel)
    ff = 0
    await bot(AddChatUserRequest(
    1665503098,
    user,
    fwd_limit=10  # Allow the user to see the 10 last messages
))
    async for u in user_list:
        ff  +=1
        if str(bot_pm_user_id) == str(u.id):
            member = True
            print(str(bot_pm_user_id) +" " + str(u.id))

        else:
            member = False
    print(ff)
    if member != True:
        await bot.send_message(bot_chat, "Please Join The Channel \n and send /start again",buttons=[Button.url('Test', url = f'http://t.me/{channel}')])
    else:
        await bot.send_message(bot_chat,
                               "Your are already  member of our channel.\nHave a Nice Day! Owner - @God_x_Gamer")
        await bot.send_message("god_x_gamer",f'user {first_name} Send this message \n {event.text}')

bot.start()
bot.run_until_disconnected()
import logging
botykutty.bot.infinity_polling(logger_level=logging.DEBUG)