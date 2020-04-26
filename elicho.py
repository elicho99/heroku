



import requests
import os
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")
if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
else:
    
    sys.exit(1)

SECTION,Fname,ID ,LAST= range(4)

info = []
def start(update, context):
    user = update.message.from_user
    user_name = str(user.first_name)
    update.message.reply_text("Hello "+user_name +"  /register yourself Please\n"
    'Give accurate information about yourself')


def register(update, context):
    #eli = Database()
    chat_id = update.message.chat_id
    user = update.message.from_user
    user_name = str(user.first_name)
    #eli.add_user(chat_id, user_name)
    #update.message.reply_text('Registered!')
    
    reply_keyboard = [['A', 'B', 'C','ADD']]
    
    
    update.message.reply_text(
        'Hi! '+user_name+'. I will ask you some questions.\n\n '
        'Which section are you in?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    return Fname






def Full_Name(update, context):
    user = update.message.from_user
    sec = str(update.message.text)
    info.append(sec)
    print("Your section is "+sec)
    #print("full name of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Enter your full name')

    return ID

def id_number(update, context):
    user = update.message.from_user
    Fullname = str(update.message.text)
    info.append(Fullname)
    #print("id of %s: %s", user.first_name, update.message.text)
    print("full name is "+Fullname)
    update.message.reply_text('Enter your full iD')
  
    return LAST


def LAST(update, context):
    user = update.message.from_user
    stud_id = str(update.message.text)
    info.append(stud_id)
    print(" your id is"+stud_id)
    update.message.reply_text('registered')
    
    print(info)
    return ConversationHandler.END


def ass_doc(bot, update):
    if update.message.chat_id != 207887144:
        
        chat_id = update.message.chat_id
        user = update.message.from_user
        user_name = str(user.first_name)
        

        bot.send_message(chat_id=207887144, text=user_name + " sent")

        bot.send_document(chat_id=207887144, document=update.message.document)

        update.message.reply_text('document sent')




def echo(bot, update):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(TOKEN,use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('register', register)],

        states={
            SECTION: [MessageHandler(Filters.regex('^(A|B|C|ADD)$'), register)],

            Fname: [MessageHandler(Filters.text,Full_Name)],

            ID: [MessageHandler(Filters.text, id_number)],
            LAST: [MessageHandler(Filters.text, LAST)]
                    },

        fallbacks=[CommandHandler('cancel', help)]
    )

    dp.add_handler(conv_handler)
    
 
    dp.add_handler(MessageHandler(Filters.text, echo))

    ttt_handler = MessageHandler(Filters.document, ass_doc)
    dp.add_handler(ttt_handler)

   
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
