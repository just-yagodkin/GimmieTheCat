import os
import random
import subprocess
from telegram import Update, Bot
from telegram.ext import CommandHandler, CallbackContext, ApplicationBuilder

TOKEN = ''

# Путь к скрипту с генерацией
SCRIPT_PATH = 'src/gen.py'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я здесь занимаюсь генерацией изображений. Отправь команду /cat и посмотри что получится 😼')

async def cat(update: Update, context: CallbackContext) -> None:
    # Генерируем картинку
    subprocess.run(['python', SCRIPT_PATH])

    # отправляем картинку
    with open('pics/gen_cat.png', 'rb') as photo:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cat", cat))
    application.run_polling()

if __name__ == '__main__':
    main()
