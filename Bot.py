import telebot

bot_token = '6219433801:AAHAz1PbC7FU3dsZp61MMnUoxSP20ZG-Zjk'
channel_id = '@backupedmattdesign'

bot = telebot.TeleBot(bot_token)

@bot.message_handler(content_types=['text', 'document', 'photo', 'audio', 'video'])
def forward_message(message):
    bot.forward_message(channel_id, message.chat.id, message.message_id)

bot.polling()
