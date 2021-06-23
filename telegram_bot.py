import telebot

bot = telebot.TeleBot("botToken", parse_mode=None)

files_directory = "/home/ftpuser/"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "خوش آمدید")

@bot.message_handler(func=lambda m: True)
def send_chart_screenshot(message):
    converted_symbol_name = ''.join([format(ord(c),'x') for c in message.text])
    try:
        with open(files_directory + converted_symbol_name + '.jpg', 'rb') as screenshot:
            bot.send_photo(message.chat.id, screenshot, reply_to_message_id=message.message_id)
        with open(files_directory + converted_symbol_name + '.jpg', 'rb') as screenshot:
            bot.send_document(message.chat.id, screenshot, reply_to_message_id=message.message_id)
    except OSError:
        bot.reply_to(message, "متاسفانه این سهم وجود ندارد!")

bot.polling()
