import telebot
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! دستور adbwebkit رو بنویس (مثلاً devices یا dump).")

@bot.message_handler(func=lambda message: True)
def handle_command(message):
    cmd = message.text.strip()
    try:
        result = subprocess.check_output(f"python3 adbwebkit.py {cmd}", shell=True, stderr=subprocess.STDOUT)
        output = result.decode('utf-8')
        bot.reply_to(message, output if output else "دستوری اجرا شد ولی خروجی نداشت.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, "خطا:\n" + e.output.decode('utf-8'))

bot.polling()
