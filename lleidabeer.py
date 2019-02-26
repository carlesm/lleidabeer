import notifications as n
import brewery as b

notification_list = []

if __name__ == "__main__":

    # Create Sensors
    sensor_list = []
    sensor_list.append(b.TemperatureSensor())
    sensor_list.append(b.FlowSensor())

    # Update Sensor Readings
    for sensor in sensor_list:
        sensor.update_value()

    for sensor in sensor_list:
        if sensor.has_alarm():
            print("Alarm !!!!")
            notification = n.Notification("Alarm",1)
            notification_list.append(notification)
            print(sensor)

    channel = n.TelegramChannel()
    for notification in notification_list:
        channel.send_notification(notification)
