from Database import Database

import pandas as pd
import logging
import requests
import os
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

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
    logger.error("No MODE specified!")
    sys.exit(1)


def start(bot, update):
    eli = Database()
    chat_id = update.message.chat_id
    user = update.message.from_user
    user_name = str(user.first_name)
    eli.add_user(chat_id, user_name)
    update.message.reply_text('Hello student!')


def register(bot, update):
    eli = Database()
    chat_id = update.message.chat_id
    user = update.message.from_user
    user_name = str(user.first_name)
    eli.add_user(chat_id, user_name)
    update.message.reply_text('Registered!')


def att(bot, update):
    eli = Database()
    student_id = eli.select_user()
    student_name = eli.select_name()
    chat_id = update.message.chat_id
    pd.Series(student_name).to_csv("attendace.csv")
    bot.send_document(chat_id=207887144, document=open('attendace.csv', 'rb'))


def talk(bot, update):
    if update.message.chat_id == 207887144:

        eli = Database()
        student_id = eli.select_user()
        student_name = eli.select_name()
        chat_id = update.message.chat_id
        user = update.message.from_user
        user_name = str(user.first_name)
        msg = update.message.text
        for x in range(1, len(student_id)):
            bot.send_message(chat_id=student_id[x], text="Hi " + str(student_name[x]))
            bot.send_message(chat_id=student_id[x], text=msg)


def res(bot, update):
    if update.message.chat_id == 207887144:

        eli = Database()
        student_id = eli.select_user()
        student_name = eli.select_name()
        chat_id = update.message.chat_id
        user = update.message.from_user
        user_name = str(user.first_name)
        msg = update.message.text
        for x in range(1, len(student_id)):
            bot.send_message(chat_id=student_id[x], text="Hi " + str(student_name[x]))
            bot.send_document(chat_id=student_id[x], document=update.message.document)


def help(bot, update):
    update.message.reply_text('Help!')


def doc(bot, update):
    update.message.reply_text('Please Visit https://github.com/elicho99/cPlusPlus_LAB/')


def photo(bot, update):
    if update.message.chat_id != 207887144:
        eli = Database()
        chat_id = update.message.chat_id
        user = update.message.from_user
        user_name = str(user.first_name)
        eli.add_user(chat_id, user_name)

        bot.send_message(chat_id=207887144, text=str(user.first_name) + " sent")

        bot.send_document(chat_id=207887144, document=update.message.document)

        update.message.reply_text('document sent')
    else:
        eli = Database()
        student_id = eli.select_user()
        student_name = eli.select_name()
        chat_id = update.message.chat_id
        user = update.message.from_user
        user_name = str(user.first_name)
        msg = update.message.text
        for x in range(1, len(student_id)):
            # context.bot.send_message(chat_id=student_id[x] ,text="Hi "+str(student_name[x]))
            bot.send_document(chat_id=student_id[x], document=update.message.document)


def echo(bot, update):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("files", doc))
    dp.add_handler(CommandHandler("send", photo))
    dp.add_handler(CommandHandler("talk", talk))
    dp.add_handler(CommandHandler("register", register))
    dp.add_handler(CommandHandler("att", att))
    # dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_handler(MessageHandler(Filters.text, talk))

    ttt_handler = MessageHandler(Filters.document, photo)
    dp.add_handler(ttt_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
