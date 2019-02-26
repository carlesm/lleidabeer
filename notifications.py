import telepot
from telepot.loop import MessageLoop


class Notification(object):
    """Notification class, includes text and criticity

    @author Carles Mateu
    """
    def __init__(self, text="", criticity=0):
        super(Notification, self).__init__()
        self.text = text
        self.criticity = criticity

    # @param text The text of the Notification
    def set_text(self, text):
        """Sets the text of the notification
        """
        self.text = text

    def set_criticity(self, criticity):
        self.criticity = criticity


class Command(object):
    """Command"""
    def __init__(self):
        super(Command, self).__init__()

class Channel(object):
    """Channel Class"""
    def __init__(self):
        super(Channel, self).__init__()

class TelegramChannel(Channel):
    """docstring for TelegramChannel."""
    def __init__(self):
        super(TelegramChannel, self).__init__()
        self.bot = telepot.Bot("650160973:AAFSMG_dslaA0l7ibhYnmv8rLQtlHrEe-BE")
        MessageLoop(self.bot, self.handle).run_as_thread()

    def send_notification(self, notification):
        self.bot.sendMessage(141990140,"* "+str(notification.criticity)+" "+notification.text)

    def handle(self, msg):
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


class ScreenChannel(Channel):
    """docstring for Screen."""
    def __init__(self):
        super(ScreenChannel, self).__init__()

    def send_notification(self, notification):
        print("* "+str(notification.criticity)+" "+notification.text)


if __name__ == "__main__":
    screen = ScreenChannel()
    telegram = TelegramChannel()
    notification = Notification("This is a test", 1)
    screen.send_notification(notification)
    telegram.send_notification(notification)
