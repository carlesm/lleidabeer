import telepot
from telepot.loop import MessageLoop
import time

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        command = msg['text']
        if command == '/temp':
            bot.sendMessage(chat_id, 'TEMPERATURE')
        elif command == '/control':
            keyboard = {'keyboard': [['Stop','Start','Idle']]}
            bot.sendMessage(chat_id,"Enter command", reply_markup=keyboard)
        elif command == 'Stop':
            # do something to Stop
            keyboard = {'hide_keyboard': True}
            bot.sendMessage(chat_id,"Stopping", reply_markup=keyboard)
        else:
            bot.sendMessage(chat_id, 'NOT UNDERSTOOD:' + command)

<<<<<<< HEAD
bot = telepot.Bot("650160973:AAFSMG_dslaA0l7ibhYnmv8rLQtlHrEe-BE")
=======

bot = telepot.Bot(TOKEN)
>>>>>>> 58ca8942108d718edb071ee2cbba67d525eac53f
print(bot.getMe())

MessageLoop(bot, handle).run_as_thread()
print("OK. Listening")

while True is True:
    time.sleep(10)
