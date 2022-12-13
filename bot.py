# Telegram Module Imports
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# For hiding the Bot Token provided by Telegram
from dotenv import load_dotenv
import os

# Loading Credentials
load_dotenv('.env')

# Storing the Bot Token
updater = Updater(os.getenv('BOT_TOKEN'), use_context=True)

# Start Command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Welcome to NoobChirag69_Bot. Please write\
		/help to see the commands available.")

# Help Command
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :
	/youtube - To visit my YouTube Channel
	/linkedin - To visit my LinkedIn Profile
	/facebook - To visit my Facebook Profile
	/github - To visit my GitHub Profile""")

# Facebook
def facebook_url(update: Update, context: CallbackContext):
    update.message.reply_text("Visit => https://www.facebook.com/chirag2k")

# YouTube
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Visit => https://www.youtube.com/c/BADDESTCOVERS")

# LinkedIn
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("Visit => https://www.linkedin.com/in/chirag-chakraborty")

# GitHub
def github_url(update: Update, context: CallbackContext):
    update.message.reply_text("Visit => https://github.com/noobchirag69")

# Unknown Texts/Commands
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Not a valid command, Sorry!")
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, your command wasn't recognisable!")

# Function Handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('facebook', facebook_url))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# Running the Bot
updater.start_polling()