import telebot
from model.User import User
import time

bot = telebot.TeleBot('1369607155:AAGV2w1z7nMLsvr0vCvoCxUOBOXk0tF0gYc')
attack = 0


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user = User(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    print(message.reply_to_message)
    if message.text == "мосгаз":
        bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь в борьбе с мос газом?")
    elif message.text == "/help_gaz":
        bot.send_message(message.chat.id, user.testUser())
        print(user.chekIndatabase())
    elif message.text == "/info_gaz":
        bot.send_message(message.chat.id, "Мос газ это враг всех Одесских чатов это чмо угрожает избиениями многим людям. Если у вас есть информация по этому человеку скиньте инфу этому боту")
    elif message.text == "АУФ" or message.text =="ауф" or message.text =="Ауф":
        bot.send_message(message.chat.id, "ПОДОЗРЕНИЕ НА МОС ГАЗ")
        #  bot.kick_chat_member(message.chat.id,message.from_user.id,int(time() + 30))
    elif message.text == "/attack":
        attack = 1
        bot.send_message(message.chat.id, "АТАКА БЛЯТЬ")
        print(attack)
       # print(time())


@bot.message_handler(content_types=['new_chat_members'])
def new_user(user):
    #bot.send_message(user.chat.id, "АТАКА БЛЯТЬ")
    print(user)
    bot.kick_chat_member(user.chat.id, user.from_user.id, int(time.time()+30))


# bot.send_message(user.chat.id, "Привет, чем я могу тебе помочь?")

bot.polling(none_stop=True, interval=0)
