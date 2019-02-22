import telepot
from telepot.loop import MessageLoop
import time

def handle(msg):
    print(msg)
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, 'TEST MESSAGE')


bot = telepot.Bot(TOKEN)
print(bot.getMe())

MessageLoop(bot, handle).run_as_thread()
print("OK. Listening")

while True is True:
    time.sleep(10)
