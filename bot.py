import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Bot token environment variable se lega
TOKEN = os.environ.get('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(
        f'Hello {user.first_name}! 👋\n'
        f'Main GitHub se deploy kiya gaya hoon! 🚀\n'
        f'/help - Help ke liye'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 **GitHub Deployed Bot**

/start - Bot shuru kare
/help - Ye help message
/status - Bot status dekhaye

Koi bhi message type karo, main reply karunga!
    """
    await update.message.reply_text(help_text)

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot running successfully!\n🚀 Deployed from GitHub")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f'Hi {user_name}! You said: "{user_text}"')

def main():
    if not TOKEN:
        logging.error("BOT_TOKEN environment variable set nahi hai!")
        return
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logging.info("Bot starting...")
    application.run_polling()

if __name__ == '__main__':
    main()