# imports 
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#Finals 
Token : Final = "6523955590:AAFb9J4LAtTO0zoiVirg3FbDE9jUL6HNsWA" # token of the bot is a Final Object
BOT_USERNAME: Final = "@Proto_hamedpro_bot" # BOts username

async def start_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello and whelcome")
    # creating a start_command for BOT
    
async def help_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("in this section there is gonna be \nBOt info")

async def custime_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("custome command for whatever needed later")


def handle_response(text:str) -> str:
    processing : str = text.lower()
    # python is casesensetive so i make the whole string into lowercase
    
    if "hello" in processing:
        return "hello"
    
    if "how are you" in processing :
        return "fine"
    
    if "elahe" in processing or "hamed" in processing:
        return "salam chetori"
    
    return "not defined" # this is a temporary handle_response

async def handle_message(update:Update, context : ContextTypes.DEFAULT_TYPE):
    text : str = update.message.text
    print(f"user {update.message.chat.id} is sending message")
    response :str = handle_response(text)
    print("BOT", response)
    await update.message.reply_text(response)
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"update {update} caused error {context.error}")
    
    
if __name__ == "__main__":
    print("Starting BOT")
    
    app = Application.builder().token(Token).build()
    # COMMANDS
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custome", start_command))
    # this is sort of like command binding in tkinter Buttons back at uni projects
    
    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    
    print("polling...") # this line is only for us to see some reaction in ide console nothing serious
    app.run_polling(poll_interval=2) # checking every two seconds for new message 
    
    
"""The Final object in the typing module of Python is a type annotation
that indicates that a variable or attribute should be considered read-only after it has been 
initialized. """
"""async is a keyword in Python that is used to define a coroutine function in an asynchronous program
In Python, a coroutine is a special type of function that can be paused and resumed at specific points 
during its execution, allowing other code to run in the meantime."""
"""The Update object in the python-telegram-bot library represents an incoming update from the 
Telegram Bot API. An update is a JSON-serialized object that contains information about a specific event
that occurred on the Telegram platform, such as a new message received by the bot or a user joining a group
chat. The Update object provides methods and properties to access this information."""
"""
SHOR SUMMARY :
The code starts with some import statements that import necessary modules for creating a Telegram bot using
the python-telegram-bot library. It defines two Final constants, Token and BOT_USERNAME, which store the
bot's token and username, respectively.
The code then defines several asynchronous functions that handle different types of bot commands and messages
. These functions use the telegram and telegram.ext modules to interact with the Telegram API.

The if __name__ == "__main__" block creates an instance of the Application class from the python-telegram-bot
library and sets the bot's token using the token method. It then adds several command and message handlers to
the bot using the add_handler method. Finally, it starts the bot using the run_polling method with a polling 
interval of 2 seconds.
Overall, this code creates a simple Telegram bot that can respond to user messages and commands with
predefined responses. The bot listens for incoming updates from the Telegram API and uses the defined 
handler functions to respond appropriately.

"""