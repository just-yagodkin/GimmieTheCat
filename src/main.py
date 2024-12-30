import os
import sys
import random
import subprocess
from telegram import Update, Bot
from telegram.ext import CommandHandler, CallbackContext, ApplicationBuilder

from utils import read_token

# ---------- Some variables ----------
# Basic color codes :)
RED = '\033[91m'
RESET = '\033[0m'

# Read TOKEN
TOKEN = read_token('token.txt')
if not TOKEN:
    print(f'Looks like TOKEN is {RED}None{RESET}. Please check is {RED}token.txt{RESET}')
    print(f'Stop execution!')
    sys.exit()

# Path to generation script
SCRIPT_PATH = 'src/gen.py'

# ---------- Main execution part ----------
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я здесь занимаюсь генерацией изображений. Отправь команду /cat и посмотри что получится 😼')

async def cat(update: Update, context: CallbackContext) -> None:
    # Generate an image
    subprocess.run(['python', SCRIPT_PATH])

    # Send an image
    with open('pics/gen_cat.png', 'rb') as photo:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cat", cat))
    application.run_polling()

if __name__ == '__main__':
    main()
