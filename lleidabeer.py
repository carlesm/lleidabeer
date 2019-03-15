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
        self.cmd_list = {}
        self._create_sensors()
        self.channel = n.TelegramChannel(self.cfg["Telegram"]["Token"],
                                         self.cfg["Telegram"]["Users"],
                                         self.cmd_list)

    def _create_sensor_type(self, sensor_type, sensor_class ):
        for ts in self.cfg['Sensors'][sensor_type]:
            if isinstance(ts, dict):
                name = list(ts.keys())[0]
                attri = ts[name]
            else:
                name = ts
                attri = dict()
            attri["factory"] = self
            self.sensor_list.append(sensor_class(name=name, **attri))


    def _create_sensors(self):
        # Create Sensors
        self.sensor_list = []
        stype = {
            "Temperature": b.TemperatureSensor,
            "FlowMeter": b.FlowSensor,
            'CO2Meter': b.CO2Sensor,
        }
        for k in stype:
            self._create_sensor_type(k, stype[k])


    # FIXME: subcmd shouldn't be none or deal with none
    # IDEA: instead of subcmd as string, deal with subcmd as list
    def register_command(self, cmdtext, cmdfunction, subcmd = None ):
        # TODO: All commands to lowercase
        print("DEBUG "+cmdtext+"*"+subcmd)
        if cmdtext not in self.cmd_list:
            self.cmd_list[cmdtext] = dict()
        if subcmd not in self.cmd_list[cmdtext]:
            self.cmd_list[cmdtext][subcmd] = list()
        self.cmd_list[cmdtext][subcmd].append(cmdfunction)

    def _get_configuration(self):
        with open("lleidabeer.yaml","r") as f:
            self.cfg = yaml.load(f)
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
