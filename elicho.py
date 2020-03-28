

import logging
import requests
import os
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


def start(update, context):
  
    update.message.reply_text('Hello student!')
    

def help(update, context):
     update.message.reply_text('Help!')
        
        

def doc(update, context):
    update.message.reply_text('Please Visit https://github.com/elicho99/cPlusPlus_LAB/')   
    
def photo(update, context):
    user = update.message.from_user
    
   
    context.bot.send_message(chat_id=207887144 ,text=str(user.first_name)+" sent")
    
    context.bot.send_document(chat_id=207887144 ,document=update.message.document)
    
    update.message.reply_text('document sent')

    return PHOTO
    
def echo(update, context):
   
    update.message.reply_text(update.message.text)


    
    

def main():
    
    updater = Updater("634656340:AAFL43JVLRzmLdwDFcqkw4jC1gN1l1UTeHg")

   
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("files", doc))
    dp.add_handler(CommandHandler("send", photo))

    
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    ttt_handler = MessageHandler(Filters.document,photo)
    dp.add_handler(ttt_handler)  
    
    
  
   
    updater.start_polling()

   
    updater.idle()


if __name__ == '__main__':
    main()
