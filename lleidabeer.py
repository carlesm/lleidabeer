import notifications as n
import brewery as b
import time
import yaml
import pprint

class LleidaBeer(object):
    """LLeidaBeer main class

    LleidaBeer is a digital, raspberry pi controlled brewery"""
    def __init__(self):
        super(LleidaBeer, self).__init__()

        self._get_configuration()

        self.notification_list = []
        notification = n.Notification("This is a test", 1)
        self.notification_list.append(notification)
        self.sensor_list = []
        self.channel = n.TelegramChannel(self.cfg["Telegram"]["Token"],
                                         self.cfg["Telegram"]["Users"])
        # Create Sensors
        self.sensor_list.append(b.TemperatureSensor())
        self.sensor_list.append(b.FlowSensor())

    def _get_configuration(self):
        f = open("lleidabeer.yaml","r")
        self.cfg = yaml.load(f)
        f.close()
        pprint.pprint(self.cfg)

    def main(self):
        while True:
            # Update Sensor Readings
            for sensor in self.sensor_list:
                sensor.update_value()

            for sensor in self.sensor_list:
                if sensor.has_alarm():
                    print("Alarm !!!!")
                    notification = n.Notification("Alarm",1)
                    self.notification_list.append(notification)
                    print(sensor)

            # Command processing
            #
            # Notifications
            for notification in self.notification_list:
                self.channel.send_notification(notification)
            time.sleep(5)


if __name__ == "__main__":
    lleidabeer = LleidaBeer()
    lleidabeer.main()
