#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import requests
import os
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello student!')
    #context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('user_photo.jpg', 'rb'))


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def doc(update, context):
    """Send a message when the command /help is issued."""
    #f = open('github_com.pdf','rb')
    
       
    update.message.reply_document(document=open('github_com.pdf', 'rb'))

PHOTO = 1    
    
def photo(update, context):
    update.message.reply_text('Great! Now, send me your assignemt on .pdf format please')
    user = update.message.from_user
    
    #os.chdir('stu_ass/')
   
    
    #photo_file = update.message.document
   # file_id = update.message.document
    newFile = context.bot.get_file(update.message.document)
    newFile.download(user.first_name+'.pdf')
    print('downloaded')
    #photo_file.download(user+'.pdf')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text('Chaww')

    return PHOTO
    
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

ANN = "Assignment Deadline is Saturday March 28"  
    
def ann(update, context):
    """Log Errors caused by Updates."""
    update.message.reply_text(ANN)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END
    
    
    

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("634656340:AAFL43JVLRzmLdwDFcqkw4jC1gN1l1UTeHg", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("announcements", ann))
    dp.add_handler(CommandHandler("files", doc))
    dp.add_handler(CommandHandler("send", photo))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    ttt_handler = MessageHandler(Filters.document,photo)
    dp.add_handler(ttt_handler)  
    
    TOKEN = "634656340:AAFL43JVLRzmLdwDFcqkw4jC1gN1l1UTeHg"
    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(TOKEN)
    # add handlers
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN) 
  
   # dp.add_handler([MessageHandler(Filters.document, photo), CommandHandler('send', photo)] )
    updater.bot.set_webhook("https://still-cove-84582.herokuapp.com/" + TOKEN)
    #updater.idle()

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
