#! /usr/bin/env python3
import config

import telegram

from telegram.ext import Updater, CommandHandler
updater = Updater(token=config.token)
dispatcher = updater.dispatcher

def bmi(bot, update):
    text = update.message.text
    texts = text.split(' ')
    try:
        height = float(texts[1])
        weight = float(texts[2])
        if (height > 3):
            height /= 100.0
        bmi = weight/height/height
        if (bmi > 30):
            outtext = 'The value is ridiculous. (It\'s %s)\nYou should input the weight as kilogram, not JIN!' % (str(bmi))
        else:
            outtext = str(weight/height/height)
    except ValueError:
        outtext = 'invalid input, format is: /bmi height(in cm or m) weight(in kg)'
    bot.sendMessage(update.message.chat_id, text=outtext)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

dispatcher.add_handler(CommandHandler("bmi", bmi))

updater.start_polling()

dispatcher.add_error_handler(error)

updater.idle()
