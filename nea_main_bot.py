from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import sys
from nea_tools import twoHr_check, psi_check

TOKEN = sys.argv[1]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	                level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Hi!')


def help(bot, update):
	"""Send a message when the command /help is issued."""
	update.message.reply_text('Help!')

def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)

def twoHr(bot, update):
	"""Two hour rain check"""
	reply_keyboard = [['Sengkang', 'Hougang', 'Geylang', 'Kallang','Eunos']]
	update.message.reply_text( "Please select your location",reply_markup=ReplyKeyboardMarkup( reply_keyboard, one_time_keyboard=True) ) 

def psi(bot, update):
	reply_keyboard = [['North Region', 'South Region', 'Central Region', 'West Region', 'East Region']]
	update.message.reply_text( "Please select your region",reply_markup=ReplyKeyboardMarkup( reply_keyboard, one_time_keyboard=True) ) 


def textHandler(bot, update):
        text=update.message.text
        #bot.send_message(chat_id=update.message.chat_id, text="Status: Awake\nLast Motion Detected:"+mot_date+","+mot_time+"\nCircadian Rythm: Normal")
        if text == 'North Region':
		psi_check("rNO")
        elif text == 'South Region':
		psi_check("rSO")
        elif text == 'Central Region':
		psi_check("rCE")
        elif text == 'West Region':
		psi_check("rWE")
        elif text == 'East Region':
		psi_check("rEA")
   	elif text == 'Sengkang':
		update.message.reply_text( twoHr_check("Sengkang") )
        elif text == 'Hougang':
                update.message.reply_text( twoHr_check("Hougang") )
        elif text == 'Geylang':    
                update.message.reply_text( twoHr_check("Geylang") )
        elif text == 'Eunos':
                update.message.reply_text( twoHr_check("Eunos"))
        elif text == 'Kallang':    
                update.message.reply_text( twoHr_check("Kallang") )
	else:
                print 'Command Not Defined'

def main():
	"""Start the bot."""
	# Create the EventHandler and pass it your bot's token.
	updater = Updater(TOKEN)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("twoHr", twoHr))
	dp.add_handler(CommandHandler("psi", psi))
	dp.add_handler(MessageHandler(Filters.text, textHandler))

#	# on noncommand i.e message - echo the message on Telegram
#	dp.add_handler(MessageHandler(Filters.text, echo))

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
