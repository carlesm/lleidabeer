import telepot


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
        self.bot = telepot.Bot(TOKEN)
        # MessageLoop(self.bot, self.handle).run_as_thread()

    def send_notification(self, notification):
        self.bot.sendMessage(CHATID,"* "+str(notification.criticity)+" "+notification.text)


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
