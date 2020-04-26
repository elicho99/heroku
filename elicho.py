


import sys
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


def start(update, context):
    user = update.message.from_user
    user_name = str(user.first_name)
    update.message.reply_text("Hello "+user_name+" send your assignment.")




def ass_doc(update, context):
    #print('geba')
    
    user = update.message.from_user
    user_name = str(user.first_name)
    #print('geba2')

    
    
    context.bot.send_message(chat_id=207887144, text=str(user.first_name) + " sent")
    #print('geba3')
    context.bot.send_document(chat_id=207887144, document=update.message.document)
    #print('geba4')
    update.message.reply_text('document sent')



def echo(bot, update):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(TOKEN,use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    
    dp.add_handler(CommandHandler("send", ass_doc))
 
    

    ttt_handler = MessageHandler(Filters.document, ass_doc)
    dp.add_handler(ttt_handler)

    dp.add_handler(MessageHandler(Filters.text, echo))
   
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
