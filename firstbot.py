from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import logging
updater = Updater(token= '1393597666:AAH3-QfBrtbU0r5nTk95yOX1MUOH3uDLyGI',use_context=True)
dispatcher = updater.dispatcher


class currentUser:

    def __init__ (self,user_id = None):
        self.__user_id = user_id
    
    def set_user_id(self,uid):
        self.__user_id = uid
    
    def get_user_id(self):
        return self.__user_id


user = currentUser()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    welcome_text = "Halo,Selamat datang!\nList-perintah:\n/info_pembayaran - Menerima info pembayaran\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)


def coba(update,context) :
    context.bot.send_message(chat_id = update.effective_chat.id,text = "Sudah coba!")


def info_pembayaran(update,context):
    text = "Silahkan input user id anda dengan format : 'UID-123XXX'"
    context.bot.send_message(chat_id = update.effective_chat.id,text = text)
    reply(update,context)


def reply(update,context):
    user_input = update.message.text
    if('UID' in user_input):
        user_input = user_input[3:]
        user.set_user_id(user_input)
        update.message.reply_text(give_uid(user_input))


def give_uid(user_input):
    
    answer = "ID Anda {}\nPaket : Indihome Prestige 100 Mbps \nTagihan bulan ini : Rp.1.750.000".format(user.get_user_id())
    return answer


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

coba_handler = CommandHandler('coba',coba)
dispatcher.add_handler(coba_handler)

info_handler = CommandHandler('info_pembayaran',info_pembayaran)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(MessageHandler(Filters.text, reply))
 

updater.start_polling()


